---
layout: post
category: mysql
tag: [backend, mysql]
title: pk가 중복이 아닌 필드만 업데이트 하기(insert into values on duplicate key update 여러행 )
---

## 목적

insert into values르ㄹ 사용해서 pk가 중복이 아닌 경우에만 행을 업데이트하고 싶었다.
여러 행을 한 꺼번에 작업해야하는 경우에 아래와 같이 insert into 와 duplicate key update를 앞 뒤에 붙여서 한 번에 쓸 수 있었다. 

## mysql 코드 

```sql
insert into db_community.tb_board_best (yymm, board_seq, SYMBOL, cmp_nm_kor, cmp_nm_eng, current_price, TARGET_PRICE, currency_cd, growth, PROFIT, SAFETY, DIVIDEND, OPINION,keypoint, category, logo, expect_return_val) VALUES 
('202206',16533, '078350.KQ','한양디지텍','hanyang digi','14200',26240,'KRW',5,3,3,2,4,'세상에는 어떤 변수가 일어날지 모른다. 모두가 된다 해도 망할 수 있으며 모두가 안된다 해도 흥할 수 있다. +능력 범위라는 것의 정확한 정의','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/DIS.png','14.0684410646388'),
('202206',16686, '010060.KS','OCI','oci','106000',110000,'KRW',3,3,2,1,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/078350.KQ.png','84.7887323943662'),
('202206',17444, '006400.KS','삼성SDI','samsung sdi co.,ltd.','508000',600000,'KRW',5,3,3,2,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/010060.KS.png','3.77358490566038'),
('202206',17468, '214270.KQ','FSN','fsn','7920',12000,'KRW',5,3,4,1,3,'광고 경기 회복에 따라 매출이 확대될 것으로 예상하며, 커머스 부문의 성장세와 신규 진출 블록체인 사업의 잠재력을 감안하면 현재의 주가는 저평가 되어있다고 생각함.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/006400.KS.png','18.1102362204724'),
('202206',17694, '217820.KQ','엔에스','ns','10250',19500,'KRW',5,3,3,0,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/214270.KQ.png','51.
on duplicate key update board_seq = values(board_seq)
```

위의 코드는 pk가 중복될 경우에 행의 다른 필드는 업데이트하지 않는다.  
다른 필드도 업데이트하려면 on duplicate key update 뒤에 컬럼을 명시해주어야한다.(참고:https://kkangdda.tistory.com/53)

replace into를 사용하고 싶었는데 그럼 행을 삭제하고 다시 추가하는 것이라고 해서 pk를 건드리지 않은 채로 놔두기 위해서 쓰지 않았다.

sql에서는 참고에 나와있는 것처럼 변수명으로 아름답게 해줄 수 없어서 아래와 같이 컬럼을 추가해주었다.  
개발을 하면서 노가다가 이렇게 적성에 잘 맞는지 깨닫고 있다.

```sql
insert into db_community.tb_board_best (yymm, board_seq, SYMBOL, cmp_nm_kor, cmp_nm_eng, current_price, TARGET_PRICE, currency_cd, growth, PROFIT, SAFETY, DIVIDEND, OPINION,keypoint, category, logo, expect_return_val) VALUES 
('202206',16533, '078350.KQ','한양디지텍','hanyang digi','14200',26240,'KRW',5,3,3,2,4,'세상에는 어떤 변수가 일어날지 모른다. 모두가 된다 해도 망할 수 있으며 모두가 안된다 해도 흥할 수 있다. +능력 범위라는 것의 정확한 정의','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/DIS.png','14.0684410646388'),
('202206',16686, '010060.KS','OCI','oci','106000',110000,'KRW',3,3,2,1,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/078350.KQ.png','84.7887323943662'),
('202206',17444, '006400.KS','삼성SDI','samsung sdi co.,ltd.','508000',600000,'KRW',5,3,3,2,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/010060.KS.png','3.77358490566038'),
('202206',17468, '214270.KQ','FSN','fsn','7920',12000,'KRW',5,3,4,1,3,'광고 경기 회복에 따라 매출이 확대될 것으로 예상하며, 커머스 부문의 성장세와 신규 진출 블록체인 사업의 잠재력을 감안하면 현재의 주가는 저평가 되어있다고 생각함.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/006400.KS.png','18.1102362204724'),
('202206',17694, '217820.KQ','엔에스','ns','10250',19500,'KRW',5,3,3,0,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/214270.KQ.png','51.5151515151515')
on duplicate key update yymm =values(yymm), symbol = values(symbol), cmp_nm_kor = values(cmp_nm_kor), cmp_nm_eng=values(cmp_nm_eng), current_price=values(current_price),
TARGET_PRICE=values(TARGET_PRICE),currency_cd=values(currency_cd), growth = values(growth), PROFIT = values(PROFIT), SAFETY=values(SAFETY), DIVIDEND=values(DIVIDEND), OPINION=values(OPINION), keypoint=values(keypoint),
category= values(category), logo=values(logo), expect_return_val=values(expect_return_val)
```