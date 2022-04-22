---
layout: post
category: mysql
tag: [backend, mysql]
title: 테이블 여러개 가로로 붙이기
---

## 목적

여러 테이블에 나눠져있는 연결되지 않은 정보를 한 개의 뷰로 모아서 볼 수 있도록 하고 싶었다.


## mysql 코드 

```sql
create view 신고건수 as
select 'comment', a.comment_seq 신고받은번호, u.nickname 신고자, a.reg_dt 신고일 
  from db_community.tb_board_comment_report a left join db_user.tb_user_info u
                                                     on u.user_seq = a.user_seq
 where a.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)  
union all
select 'board', b.board_seq, u.nickname, b.reg_dt
  from db_community.tb_board_report b left join db_user.tb_user_info u
                                             on u.user_seq = b.user_seq
 where b.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'portfolio', c.idea_seq, u.nickname, c.reg_dt
  from db_portfolio.tb_idea_report c left join db_user.tb_user_info u
                                            on u.user_seq = c.user_seq
 where c.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'portfolio_comment', d.comment_seq, u.nickname, d.reg_dt
  from db_portfolio.tb_idea_comment_report d left join db_user.tb_user_info u
                                            on u.user_seq = d.user_seq
 where d.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'community', e.comm_seq, u.nickname, e.reg_dt
  from db_community.tb_community_report e left join db_user.tb_user_info u
                                            on u.user_seq = e.user_seq
 where e.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY) 
union all
 select 'user', f.user_seq, u.nickname, f.reg_dt
  from db_user.tb_user_report f left join db_user.tb_user_info u
                                            on u.user_seq = f.user_seq
 where f.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY);
                                                                                    

select * from 신고건수;
```

## 결과 화면 출력

![신고 뷰 모음 결과 화면](/public/img/report_result.png)
