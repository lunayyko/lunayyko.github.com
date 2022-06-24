---
layout: post
category: mysql
tag: [backend, mysql]
title: pk가 중복이 아닌 필드만 업데이트 하기(insert into values on duplicate key update 여러행 )
---

## 목적

pk가 중복이 아닌 경우에만 행을 업데이트하고 싶었다.
여러 행을 한 꺼번에 작업해야하는 경우에 아래와 같이 insert into 와 duplicate key update를 앞 뒤에 붙여서 한 번에 쓸 수 있다. 

## mysql 코드 

```sql
insert into db_community.tb_board_best (yymm, board_seq, SYMBOL, cmp_nm_kor, cmp_nm_eng, current_price, TARGET_PRICE, currency_cd, growth, PROFIT, SAFETY, DIVIDEND, OPINION,keypoint, category, logo, expect_return_val) VALUES 
('202206',16533, '078350.KQ','한양디지텍','hanyang digi','14200',26240,'KRW',5,3,3,2,4,'세상에는 어떤 변수가 일어날지 모른다. 모두가 된다 해도 망할 수 있으며 모두가 안된다 해도 흥할 수 있다. +능력 범위라는 것의 정확한 정의','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/DIS.png','14.0684410646388'),
('202206',16686, '010060.KS','OCI','oci','106000',110000,'KRW',3,3,2,1,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/078350.KQ.png','84.7887323943662'),
('202206',17444, '006400.KS','삼성SDI','samsung sdi co.,ltd.','508000',600000,'KRW',5,3,3,2,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/010060.KS.png','3.77358490566038'),
('202206',17468, '214270.KQ','FSN','fsn','7920',12000,'KRW',5,3,4,1,3,'광고 경기 회복에 따라 매출이 확대될 것으로 예상하며, 커머스 부문의 성장세와 신규 진출 블록체인 사업의 잠재력을 감안하면 현재의 주가는 저평가 되어있다고 생각함.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/006400.KS.png','18.1102362204724'),
('202206',17694, '217820.KQ','엔에스','ns','10250',19500,'KRW',5,3,3,0,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/214270.KQ.png','51.5151515151515'),
('202206',17721, '207940.KS','삼성바이오로직스','samsung biologics','829000',1026000,'KRW',5,4,3,1,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/217820.KQ.png','90.2439024390244'),
('202206',18213, '294570.KQ','쿠콘','coocon','55700',59000,'KRW',5,4,3,2,3,'1) 금융권을 넘어 기업들의 마이 데이터 사업 진출 2) 새 정부의 플랫폼 규제 완화에 따른 수혜 예상','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/207940.KS.png','23.7635705669481'),
('202206',18295, '060150.KQ','인선이엔티','insun ent','11500',15000,'KRW',2,2,5,0,3,'                     ','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/294570.KQ.png','5.9245960502693'),
('202206',18307, '013030.KQ','하이록코리아','hy-lokco','17850',21500,'KRW',4,3,4,3,3,'건설, 조선, 플랜트, 반도체 클린룸 등 앞으로 좋아질 산업에서 없어서는 안 될 최고의 기업. 그러나 수주 랜덤과 사이클이 있으며 매출 증가도 크게 늘어나지 않아 부담이 있지만 조선업의 재도약과 향후 수소 산업에 큰 역할을 할 것으로 기대.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/060150.KQ.png','30.4347826086957'),
('202206',18314, 'ASML','ASML 홀딩 NV ADR','asml holding','667.93',694.15,'EUR',2,5,4,3,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/013030.KQ.png','20.4481792717087'),
('202206',18456, '053580.KQ','웹케시','webcash','25300',46200,'KRW',3,4,4,2,4,'1) 리오프닝 수혜주 2) 사업 구조조정을 통한 영업레버리지 극대화 시작 ','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/ASML.png','3.92556106178792'),
('202206',18807, '299030.KQ','하나기술','hana technology co ltd','66400',86300,'KRW',5,3,4,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/053580.KQ.png','82.6086956521739'),
('202206',19366, '348210.KQ','넥스틴','nextin inc','65900',103500,'KRW',5,3,3,1,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/299030.KQ.png','29.9698795180723'),
('202206',19548, '083450.KQ','GST','gst','30250',66000,'KRW',3,5,5,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/348210.KQ.png','57.0561456752656'),
('202206',19720, '131390.KQ','원익피앤이','wonik pne','30000',44800,'KRW',5,4,4,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/083450.KQ.png','118.181818181818'),
('202206',20115, '019210.KQ','와이지-원','yg-1','8990',12500,'KRW',4,3,3,2,3,'제조업에 부는 신 제조업 혁명의 시대에 없어서는 안 될 슈퍼 중견 기업','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/131390.KQ.png','49.3333333333333'),
('202206',20403, '104460.KQ','디와이피엔에프','dyp&f','37100',50400,'KRW',4,3,3,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/019210.KQ.png','39.0433815350389'),
('202206',18985, '000490.KS','대동','daedong','16650',35800,'KRW',5,3,4,4,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/104460.KQ.png','35.8490566037736'),
('202206',20710, '003800.KQ','에이스침대','acebed','42000',52400,'KRW',2,3,5,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/000490.KS.png','115.015015015015'),
('202206',20794, '215000.KQ','골프존','golfzon','180500',260000,'KRW',4,5,4,2,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/003800.KQ.png','24.7619047619048'),
('202206',20765, '134790.KS','시디즈','sidiz','55700',67000,'KRW',2,2,4,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/215000.KQ.png','44.0443213296399'),
('202206',20747, 'DNA','깅코 바이오웍스 홀딩스 Class A','ginkgo bioworks holdings inc','2.71',4.41,'USD',5,2,2,1,3,'빌 게이츠와 코로나 이후 핫해진 캐시우드, 장기 투자로 유명한 베일리 기포드 등이 투자한 징코 바이오웍스는 합성생물학과 IT를 접목시켜 다양한 분야에서 사용 가능한 플랫폼을 만든 회사, 그들은 특히 장기펀드의 대가가 왜 투자를 했는지 알아보자!','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/134790.KS.png','20.2872531418312'),
('202206',21887, '012700.KQ','리드코프','leadcorp','8680',11700,'KRW',5,4,3,5,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/USA.png','62.7306273062731'),
('202206',21818, '035760.KQ','CJ ENM','cj enm','106200',205000,'KRW',5,4,4,2,4,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/012700.KQ.png','34.7926267281106'),
('202206',22157, '285130.KS','SK케미칼','skchem','127000',110000,'KRW',3,3,3,2,2,' 2021년 폭발적인 수익을 내면서 단기적으로 보여지는 지표는 좋아보일 수 있으나 해당 1년에 대한 지표로 판단하기 어려움이 있음 보수적인 목표주가를 잡은 것이기에 2021년 정도의 매출 영향력이 계속해서 이어지면서 성장하면 좋은 투자처가 될 수 있다는 의견','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/035760.KQ.png','93.0320150659134'),
('202206',22138, 'ILMN','일루미나','illumina inc','243.49',495.75,'USD',4,4,3,1,3,'유전자 분야는 정해진 미래이다. 시장이 안 좋은 지금이 유전자 기업에 대해 공부할 기회. 놓치지 말아요~','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/285130.KS.png','-13.3858267716535'),
('202206',22081, '026960.KS','동서','dongsuh','26800',16500,'KRW',1,3,4,3,1,'안정적인 기업은 사실이지만 주가의 상승 흐름을 기대하기는 어렵다는 판단 기업의 가치를 기준으로 판단했을 때는 현재 주가도 고평가가 되어있다고 생각하여 매도 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/ILMN.png','103.601790627952'),
('202206',22178, '170790.KQ','파이오링크','piolink','12450',15750,'KRW',3,3,5,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/026960.KS.png','-38.4328358208955'),
('202206',22228, '005380.KS','현대차','hyundaimtr','184000',280000,'KRW',5,4,4,3,3,'현대차의 주가는 차트를 통해서 현 위치를다시 한번 심층 분석을 통해서 제시를 해드리겠지만 지금 위치는 전반적으로괜찮은 위치에 있습니다. ','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/170790.KQ.png','26.5060240963855'),
('202206',22383, '005490.KS','POSCO홀딩스','posco holdings','294000',450000,'KRW',3,4,4,3,3,'안정적인 기업 그 자체에 철강 신소재 양산에 성공한 극저온용 고망간강이 엑슨모빌의 적합성 평가를 마쳐 협력을 하면서 계속해서 사업 영역을 확장해나가고 있으며 단순 지표로 계산했을 때 현재 주가가 많이 싸기 때문에 이러한 이익을 유지하거나 성장시킨다는 가정하에 매수 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/005380.KS.png','52.1739130434783'),
('202206',21396, '137400.KQ','피엔티','p&t','61200',71700,'KRW',5,4,4,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/005490.KS.png','53.0612244897959'),
('202206',21491, '112610.KS','씨에스윈드','cswind','57200',84000,'KRW',5,3,3,4,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/137400.KQ.png','17.156862745098'),
('202206',22384, '007070.KS','GS리테일','gs retail','26950',33552,'KRW',3,3,2,2,2,'1) 오프라인 매장 고객 선호도 높으며, 점포 수 대비 매출 우위  2) 퀵커머스- GS25/GS더프레쉬 물류 거점으로 활용한 퀵커머스 가능.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/112610.KS.png','46.8531468531469'),
('202206',22390, '001570.KS','금양','kumyang','4720',6030,'KRW',5,3,4,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/007070.KS.png','24.4972170686456'),
('202206',22513, '114090.KS','GKL','gkl','15400',20000,'KRW',4,3,3,1,3,'최근 리오프닝 관련해서 대표 기업으로 잘 알고 있는 종목으로서 중국인의 고객 비중이 높은 기업인 만큼 최근 코로나 봉쇄 해제 명령에 의해서 단계적 완화를 통해 내년부터는 충분한 이익 레버러지 효과를 발생할 것으로 견해','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/001570.KS.png','27.7542372881356'),
('202206',22616, '006400.KS','삼성SDI','samsung sdi co.,ltd.','508000',359000,'KRW',2,1,2,2,1,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/114090.KS.png','29.8701298701299'),
('202206',22682, '348370.KQ','엔켐','enchem','76800',112000,'KRW',5,4,5,2,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/006400.KS.png','-29.3307086614173'),
('202206',22736, 'K','켈로그','kellogg co','69.01',102,'USD',3,4,4,3,3,' 장기적으로 안정적인 수익과 배당흐름을 만들고 싶은 투자자와 보수적인 투자자 입장에서는 매력적인 투자처가 될 수 있다는 생각 분석 내용을 토대로 참고하시면 두마리 토끼를 잡을 수 있을 것이라는 판단에 매수 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/348370.KQ.png','45.8333333333333'),
('202206',22735, '012330.KS','현대모비스','mobis','216500',250000,'KRW',4,4,4,1,3,'전기차로의 전환에 있어서 국내굴지의 현대차와 기아차의 부품을 공급하던 모비스에게 잡음이 쏟아지고 있지만 회사나름에 자율주행등 미래에 대한 대비를 하고 있음에도 주가는 글로벌대비 저평가로 판단','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/K.png','47.8046659904362'),
('202206',22778, '065710.KQ','서호전기','seoho','19400',22000,'KRW',2,2,4,3,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/012330.KS.png','15.473441108545'),
('202206',22818, '047810.KS','한국항공우주','korea aerospace','56900',63000,'KRW',3,3,3,1,2,'미래 가치를 두고 보았을 때는 성공적인 항공우주 사업의 시작점이 이번 계기로 인해 스타트 된다면 투자 메리트가 있을 것으로 보이지만 현실적인 재무제표와 이미 기대감과 수급으로 올라있는 주가로 보았을 때 당장 투자하기에는 무리가 있다는 판단에 중립 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/065710.KQ.png','13.4020618556701'),
('202206',22868, 'QSR','레스토랑 브랜즈 인터내셔널','restaurant brands international inc.','51.44',72,'USD',2,4,5,5,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/047810.KS.png','10.7205623901582'),
('202206',22884, '047050.KS','포스코인터내셔널','posco international','24550',54900,'KRW',1,2,3,2,3,'개인적인 투자 관점에서는 매수를 권하지는 않지만 형식적인 계산 방법과 현재 상태를 유지한다는 가정하에는 현 주가가 저렴한 상태라고 판단으로 5년 내 목표 주가에 도달한다는 것을 기대하며 매수를 진행하는 것이 좋을 듯 곡물 관련은 투자 사업 4%대 밖에 되지 않기 때문에 무역 사업의 사이클이 돌아와서 수혜를 본다면 도달 할 수 있을 것이라 예상하며 매수 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/USA.png','39.9688958009331'),
('202206',22926, '108320.KQ','LX세미콘','lx semicon','122100',143500,'KRW',4,3,4,3,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/047050.KS.png','123.625254582485'),
('202206',23011, '119860.KQ','다나와','danawa','18000',38000,'KRW',2,4,3,3,3,'아는사람들은 아는 컴퓨터관련 전문 쇼핑몰. 꾸준한 실적이지만 주가는 시장의 오해인지 실제 경쟁자등의 문제로 하락중인것인지.. 중요한건 일단 이름만 봐도 8할은 하고 있다.','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/108320.KQ.png','17.5266175266175'),
('202206',22978, '000240.KS','한국앤컴퍼니','hankook & company co ltd','13600',17300,'KRW',4,3,4,4,3,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/119860.KQ.png','111.111111111111'),
('202206',23126, '064350.KS','현대로템','hyundai rotem','22150',14900,'KRW',2,2,2,1,1,'현재 수익성은 개선되고 있으며 흑자 전환을 함에 따라 가치는 괜찮아질 것으로 보여짐 하지만 현재 반영된 주가는 수급의 영향도 받지 않은 상태로 큰 상승을 하여 고평가된 상태이기 때문에 현재 주가는 건전하지 못하다는 판단에 매도 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/000240.KS.png','27.2058823529412'),
('202206',23151, '115310.KQ','인포바인','infovine','27650',20000,'KRW',2,4,4,2,1,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/064350.KS.png','-32.7313769751693'),
('202206',23208, '234080.KS','JW생명과학','jw lifescience','12800',17000,'KRW',3,3,3,3,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/115310.KQ.png','-27.6672694394213'),
('202206',23272, '094970.KQ','제이엠티','jmt','3630',5300,'KRW',3,3,4,2,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/234080.KS.png','32.8125'),
('202206',23313, '001120.KS','LX인터내셔널','lx int','38850',60000,'KRW',3,4,3,3,3,'매출과 영업이익의 성장세나 업황에 대한 현 시점의 흐름을 계속해서 이어갈 경우 충분히 투자 메리트가 있는 기업으로 보여지며 한시적인 성장세가 아닌 사업을 하고 있기 때문에 이점을 바탕으로 현재 적정주가 계산 시 매우 저평가 되어있는 상태이며 PER 또한 정상적은 재무제표를 토대로 계산된 지표이기 때문에 저평가가 확실한 상태라고 보여지기에 매수 의견 제시','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/094970.KQ.png','46.0055096418733'),
('202206',23574, '012700.KQ','리드코프','leadcorp','8680',9200,'KRW',3,2,3,4,2,'','B010801','https://cloudfront.alpha-bridge.kr/prod/image/logos/001120.KS.png','54.4401544401544')
on duplicate key update board_seq = values(board_seq)
```

위의 코드는 pk가 중복될 경우에 행의 다른 필드는 업데이트하지 않는다.  
기존에 있던 데이터들 중 중복된 데이터는 그대로 있고, 새로운 데이터만 입력되게 하려면 아래 블로그에 나와있는 것처럼 on duplicate key update 뒤에 컬럼을 명시해주어야한다.

https://kkangdda.tistory.com/53