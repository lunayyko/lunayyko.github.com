---
layout: post
category: mysql
tag: [backend, mysql]
title: 여러 테이블 상하로 붙여서 view생성하기
---

## 목적

여러 테이블에 나눠져있는 연결되지 않은 정보를 한 개의 뷰로 모아서 볼 수 있도록 하고 싶었다.


## mysql 코드 

```sql
create view 최근2달신고 as
select 'comment', a.comment_seq 신고받은번호, u.nickname 신고자, a.reg_dt 신고일, g.comment 내용, a.REPORT_TYPE, a.REPORT_REASON
  from db_community.tb_board_comment_report a left join db_user.tb_user_info u
                                                     on u.user_seq = a.user_seq
                                              left join db_community.tb_board_comment g
                                                     on a.COMMENT_SEQ = g.comment_seq
 where a.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)  
union all
select 'board', b.board_seq, u.nickname, b.reg_dt, h.TITLE, b.REPORT_TYPE, b.REPORT_REASON
  from db_community.tb_board_report b left join db_user.tb_user_info u
                                             on u.user_seq = b.user_seq
                                      left join db_community.tb_board h
                                             on b.BOARD_SEQ = h.board_seq
 where b.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'portfolio', c.idea_seq, u.nickname, c.reg_dt, i.idea_nm, c.REPORT_TYPE, c.REPORT_REASON
  from db_portfolio.tb_idea_report c left join db_user.tb_user_info u
                                            on u.user_seq = c.user_seq
                                     left join db_portfolio.tb_idea i
                                             on c.idea_SEQ = i.IDEA_SEQ
 where c.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'portfolio_comment', d.comment_seq, u.nickname, d.reg_dt, j.comment, d.REPORT_TYPE, d.REPORT_REASON
  from db_portfolio.tb_idea_comment_report d left join db_user.tb_user_info u
                                                    on u.user_seq = d.user_seq
                                             left join db_portfolio.tb_idea_comment j
                                                    on d.comment_SEQ = j.IDEA_SEQ
 where d.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY)
union all
 select 'community', e.comm_seq, u.nickname, e.reg_dt, k.TITLE, e.REPORT_TYPE, e.REPORT_REASON
  from db_community.tb_community_report e left join db_user.tb_user_info u
                                                 on u.user_seq = e.user_seq
                                          left join db_community.tb_community k
                                                 on e.COMM_SEQ = k.comm_seq
 where e.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY) 
union all
 select 'user', f.report_user_seq, u.nickname, f.reg_dt, f.user_seq, f.REPORT_TYPE, f.REPORT_REASON
  from db_user.tb_user_report f left join db_user.tb_user_info u
                                       on u.user_seq = f.report_user_seq
                                left join db_user.tb_user_info l
                                       on u.user_seq = f.user_seq
 where f.reg_dt > DATE_ADD(now(), INTERVAL -60 DAY);

select * from 최근2달신고;
```

이렇게 실행하면 아래와 같이 정리되어 나온다. 
 
![신고내역](/public/img/report.png)
