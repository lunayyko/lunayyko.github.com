---
layout: post
category: UX
tag: [ux]
title: 포트폴리오 리스트 유닛 디자인 업데이트
---

## 포트폴리오 리스트 유닛 바꾸기 전

![바꾸기 전](/public/img/portfolio_before.jpg){:width="200"}

## 포트폴리오 리스트 유닛 바꾼 뒤 (최종디자인)

![바꾼 뒤](/public/img/portfolio_after.png){:width="200"}


## 회고

유저에게 시각적 즐거움을 제공하고 흥미롭게 여길만한 투자정보를 미리 보여주고싶어서 시작한 기획이었는데
와이어프레임을 그리는 것은 금방 했는데 설득의 시간이 굉장히 오래 걸렸고 의사소통 과정이 부정적이었어서 이직을 생각하는 계기가 되었다.
빌드되는 과정에서 여러가지 정보가 추가되어서 유닛이 커지게 되었지만 이전보다 확실히 보기좋아서 뿌듯했다. 

## 스케치

첫 스케치
![첫 스케치](/public/img/first_sketch.png){:width="400"}

피그마
![피그마](/public/img/portfolio_figma.png){:width="400"}

디자인
![디자인](/public/img/portfolio_design.png){:width="400"}

## 사후평가
몽고DB와 SQL에서 주차별 포트폴리오 생성수, 포트폴리오 GNB 방문수를 확인한 결과 1.5배가량의 트래픽이 증가한 것을 확인할 수 있었다. 

<table>
  <thead>
    <tr>
      <th>주차</th>
      <th>포트폴리오 생성수</th>
      <th>포트폴리오 방문수(GNB)</th>
      <th>상세 클릭 빈도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>-1주차</td>
      <td>102</td>
      <td>566</td>
      <td>396</td>
    </tr>
    <tr>
      <td>1주차</td>
      <td>120</td>
      <td>803</td>
      <td>247</td>
    </tr>
    <tr>
      <td>2주차</td>
      <td>207</td>
      <td>849</td>
      <td>329</td>
    </tr>
    <tr>
      <td>3주차</td>
      <td>309</td>
      <td>974</td>
      <td>457</td>
    </tr>
  </tbody>
</table>


### 추출에 사용한 쿼리

처음에는 값이 맞게 나오지 않아서 내부 개발 직원들의 아이디를 조회 대상에서 제외했더니 값이 맞게 나왔다. 
몽고디비에는 날짜가 초형태로 저장되어있어서 sql에서 바꾸어서 집어넣었다. 

```sql
select unix_timestamp('2022-09-26')
```

```sql
select count(1) 
from db_portfolio.tb_idea a left join db_user.tb_user_info b 
								   on a.user_seq = b.user_seq
where REG_DT > '2022-10-17' and REG_DT < '2022-10-24' 
  and a.user_seq not in (73,385,8919,5035, 5015, 7516)
```

```sql
db.menu_view.find({'menu':'portfolio', 'reg_ts' : {$gte:1666537200, $lte:1667142000},'user_seq':{$nin:[72,73,385,5015,5035,7516,8919]}}).count()
```