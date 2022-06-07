---
layout: post
category: backend
tag: [backend]
title: 포스팅 예약발행 
---

## 목적

원하는 시간에 포스팅을 발행한다.

### 초본

```python
/batch/v3_1/batch_reserve_publish.py

import pandas as pd
import pymysql
from apis.v3_1.community import save_board_data
from datetime import datetime
from config.config_db import DataBaseConfig as con_DB
from configuration    import server_name, send_slack

def reserve_publish(conn):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = f"""
        select reserve_dt, reserve_seq
          from db_community.tb_board_reserve
         where del_yn = 0
    """
    df_reserve = pd.read_sql(sql, conn)

    reserve_list = []

    now = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

    for row in df_reserve:
        if now == row[0]:
            reserve_list.append(row[1])

    for reserve_seq in reserve_list:
        sql = f"""
            select category, title, contents, user_seq, video_yn, video_link
              from db_community.tb_board_reserve
             where reserve_seq = {reserve_seq}
        """
        cursor.execute(sql)
        args = cursor.fetchone()

        user_seq = args['user_seq']
        title = args['title']

        save_board_data(conn, args, 'post')

        send_slack(f' {now}에 {user_seq}번 유저가, \n'
                   f' {title} , \n'
                   f' 글을 예약발행했습니다',
                   f' tangopick_{server_name}_reserve')
    return True

if __name__ == '__main__':
    conn = pymysql.connect(**con_DB.tangopick_db_config(read=False)[0])
    reserve_publish(conn)
    conn.commit()
    conn.close()

```

### 피드백

함수 밖에서 시간을 받아서 해당 시간에 예약발행해야하는 건만 sql에서 뽑는것이 좋겠다.
예외처리구문을 사용해서 fail나는 건을 잡아서 3분 후 다시 돌려주고, 2번 fail나는 경우 슬랙을 발송한다.

### 중간 수정본 

```python
import pymysql
from apis.v3_1.community import save_board_data
from datetime            import datetime
from config.config_db    import DataBaseConfig as con_DB
from configuration       import server_name, send_slack

def reserve_publish(conn, now):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = f"""
        select reserve_dt, reserve_seq, category, title, contents, user_seq, is_public, video_yn, video_link, comm_seq 
          from db_community.tb_board_reserve
         where reserve_dt = '{now}' and del_yn = 0
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    cnt = 0
    fail_cnt = 0

    try:
        for args in rows:
            #발행할 때 없어야되서 삭제
            args.pop('reserve_dt')

            save_board_data(conn, args, 'POST')
            cnt = cnt+1

            #발행하면 예약에서 삭제
            delete_sql = f"""
                update db_community.tb_board_reserve
                 where reserve_seq = {args['reserve_seq']}
                   set del_yn = 0, del_dt = {now} 
            """
            cursor.execute(delete_sql)
            print(args['reserve_seq'],'삭제되었습니다')

    except Exception as e:
        print(str(e))
        fail_cnt = fail_cnt + 1

    if cnt != 0:
        send_slack(f' {cnt}개의 포스팅이 \n'
                   f' {now}에 예약발행되었습니다 \n',
                   f' tangopick_{server_name}_reserve')

    if fail_cnt != 0:
        send_slack(f' {fail_cnt}개 실패했습니다 \n',
                   f' tangopick_{server_name}_reserve')

    return True

if __name__ == '__main__':
    conn = pymysql.connect(**con_DB.tangopick_db_config(read=False)[0])

    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:00')
    now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:00')

    reserve_publish(conn, now)
    conn.commit()
    conn.close()
```

### 수정사항

몽고디비를 연결해서 게시글 작성할 때 입력된 태그를 저장한다.


### 최종본 

```python 
import pymysql
from pymongo import MongoClient
import copy
from datetime             import datetime
from config.config_db     import DataBaseConfig as con_DB
from config.config_doc_db import DocumentDB as con_DocDB
from configuration        import server_name, send_slack
from apis.v3_1.community  import save_board_data


def reserve_publish(conn, conn_mongo, now):
    #몽고DB user 데이터베이스에 연결
    doc_db = conn_mongo.user
    #Mysql연결
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = f"""
        select reserve_dt, reserve_seq, category, title, contents, user_seq, is_public, video_yn, video_link, comm_seq 
          from db_community.tb_board_reserve
         where reserve_dt = '{now}' and del_yn = 0
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    cnt = 0
    fail_cnt = 0

    try:
        for args in rows:
            #발행할 때 없어야되서 삭제
            args.pop('reserve_dt')

            #발행
            result = save_board_data(conn, args, 'POST')
            contents = result['contents']

            #태그 몽고디비 저장
            board_contents = {'contents': contents, 'board_seq': result['board_seq']}
            success = save_doc_db(db='community', table='board_contents', key='board_seq', args=board_contents,
                                  method='POST')
            success = save_doc_db(db='community', table='board', key='board_seq', args=result, method='POST')
            print(f'doc_db 저장 완료')

            if success:
                sql = f"""
                update db_community.tb_community
                set upd_ts = unix_timestamp()
                where comm_seq =  {args['comm_seq']}
                """
                cursor.execute(sql)

            # 비속어 검사
            # validate_board.delay(result)

            #슬랙 발송시 표시되는 발행된 게시글 갯수
            cnt = cnt + 1

            #발행하면 예약에서 삭제
            delete_sql = f"""
                update db_community.tb_board_reserve 
                   set del_yn = 1, del_dt = now()
                 where reserve_seq = {args['reserve_seq']} 
            """
            cursor.execute(delete_sql)
            print(args['reserve_seq'],'삭제되었습니다')

    except Exception as e:
        print(str(e))
        fail_cnt = fail_cnt + 1

    if cnt != 0:
        send_slack(f' {cnt}개의 포스팅이 \n'
                   f' {now}에 예약발행되었습니다 \n',
                   f' tangopick_{server_name}_reserve')

    if fail_cnt != 0:
        send_slack(f' {fail_cnt}개 실패했습니다 \n',
                   f' tangopick_{server_name}_reserve')

    return True

def save_doc_db(db, table, key, args, method):
    database = conn_mongo[db]
    collection = database[table]

    if method == 'DELETE':
        collection.delete_one({"_id": args[key]})
        print('doc_db 삭제 성공')
        return

    post_id = None
    # print('args', args)
    doc_dict = copy.deepcopy(args)
    doc_dict['_id'] = int(args[key])
    doc_dict['del_yn'] = 0

    if method == 'POST':
        post_id = collection.insert_one(doc_dict)
        print(f'doc_db {table} 저장 성공', post_id)
    else:
        post_id = collection.save(doc_dict)
        print(f'doc_db {table} 수정 성공', post_id)

    return True

if __name__ == '__main__':
    conn = pymysql.connect(**con_DB.tangopick_db_config(read=False)[0])
    conn_mongo = MongoClient(**con_DocDB.DOC_DB_INFO, **{'retryWrites': False})

    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:00')
    now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:00')

    reserve_publish(conn, conn_mongo, now)
    conn.commit()
    conn.close()
```

### 회고

몽고디비를 연결하는 내용이 알고나니 매우 쉬웠는데 모를 때는 정말 어렵게 느껴졌었다. 