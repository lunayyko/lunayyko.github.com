---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제5 휴먼스케이프(임상실험정보 검색)
---

# 과제 설명 요약
- 구현 기간 : 21.11.15(17시) ~ 21.11.17 (10시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment5) 참고

# 사용한 기술 설명

임상정보인 [공공데이터](https://www.data.go.kr/data/3074271/fileData.do#/API%20%EB%AA%A9%EB%A1%9D/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887)를 API로 받고 변경 내역이 있는 부분을 포함하여 검색할 수 있도록 하는 과제에서 상세 임상정보 조회 API, 스웨거를 담당했고 테스트케이스를 처음으로 작성했다. 

가장 어려웠던 API의 실시간 DB동기화는 팀장님이 작성하셨고 아래의 회고 글에 들어가면 로깅을 포함한 구현 설명을 읽을 수 있다. 
[태우님의 휴먼스케이프과제 블로그 글](https://velog.io/@burnkim61/%ED%94%84%EB%A6%AC%EC%98%A8%EB%B3%B4%EB%94%A9-%EA%B3%BC%EC%A0%9C-5)

# 모델링

![디비](/public/img/humanscape_db.png)
API로 받게되는 공공데이터가 위와 같은 형태로 되어있었고, 이 형태 그대로 디비에 업로드하였다. 이 디비를 보고 과제번호와 과제이름, 학과(ex.소아과)와 담당기관, 연구종류와 임상시험단계 컬럼을 검색에 포함하는 것이 좋을 것 같다고 결정했다. 자세한 기준은 아래와 같다. 
![모델링](/public/img/humanscape_modeling.png)

# 컬럼별 검색 기능 구현 내역

|이름(필드명)   |필드 타입                   |필터링 가능/필요 여부 |lookup_expression|
|-------|-------------------------|--------------------|--------------------|
|과제명(name) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|과제번호(number) |Char (unique)    |X (수집한 임상정보에 대한 API에서 처리) |X  |
|연구기간(period) |Char    |X (데이터가 통일성이 없음) |X  |
|연구범위(range) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|연구종류(code) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|연구책임기관(institute) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|임상시험단계(stage) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|전체목표연구대상자수(target_number) |Integer    |O |lte, gte (최소/최대 대상자 수)  |
|진료과(office) |Char    |O |icontains (입력된 값을 포함하는 경우)  |
|생성일(created_at) |Date    |X (우리 데이터베이스에 객체 생성된 시점 값이므로 필터링 필요없음) |X |
|업데이트일(updated_at) |Date    |X (수집한 임상정보 리스트 API에서 처리) |X |

rest_framework 라이브러리에서 제공하는 SearchFilter를 사용해 검색 기능을 구현했다.

# 내가 작성한 코드 / 기억에 남는 코드

```python
#research > views.py
#import 부분 생략

#method_decorator를 사용하면 함수가 아닌 Class에 스웨거를 넣을 수 있다.
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id ="연구 데이터 상세 조회",
    operation_description ="연구 번호를 입력하세요\n\n" +
                            "예시 : C160008",
    responses    = {
        "201": "SUCCESS",
        "404": "NOT_FOUND",
        "400": "BAD_REQUEST",
    }
))
class ResearchRetrieveView(RetrieveAPIView):
    queryset            = ResearchInformation.objects.all()
    serializer_class    = ResearchInformationSerializer
    lookup_field        = 'number'

#스웨거상에서 함수가 아닌 클래스에 예시를 넣는 방법을 시간상 못 찾아서 설명 부분에 같이 넣었다. 
@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_id ="연구 데이터 검색",
    operation_description = "전체 연구 데이터를 필터 및 검색합니다.\n\n"
                            "필터 : 과제명(name), 연구기간(range), 연구종류(code), 연구책임기관(institute), 임상시험단계(연구모형)(stage), 연구책임기관(institute), 임상시험단계(stage), 전체목표연구대상자수(target_number), 진료과(office), 최고 연구기간(min_target_number), 최대 연구기간(max_target_number)의 필터 및 개별 검색 가능\n\n" +
                            "전체 검색 : search 값에 검색하고 싶은 단어 입력" +
                            "(과제명, 과제번호, 연구기간, 연구종류, 연구책임기관, 임상시험단계(연구모형), 진료과 중 검색 가능)\n\n" +
                            "정렬 : 업데이트된 날짜 역순으로 기본 정렬, 기준으로 정렬하고 싶은 컬럼의 키값을 ordering에 입력하세요\n\n" +
                            "예시 : \n" +
                            "{\n"+
                                "id: 10,\n"+
                                "name: 제2형 당뇨병 임상연구네트워크 구축사업\n"+
                                "number: C140014\n"+
                                "period: 120개월\n"+
                                "range: 국내다기관\n"+
                                "code: 관찰연구\n"+
                                "institute: 경희대학교병원\n"+
                                "stage: 코호트\n"+
                                "target_number: 700\n"+
                                "office: Endocrinology\n"+
                                "created_at: 2021-11-16\n"+
                                "updated_at: 2021-11-16\n"+
                            "}",
    responses    = {
        "201": "SUCCESS",
        "404": "NOT_FOUND",
        "400": "BAD_REQUEST",
    }
))
#이렇게 drf내부의 서치뷰를 사용하면 아래컬럼을 모두 포함하는 검색을 구현할 수 있다. 
class SearchResearchView(ListAPIView):
    queryset            = ResearchInformation.objects.all()
    serializer_class    = ResearchInformationSerializer
    filter_backends     = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class     = ResearchFilter
    ordering            = ['-updated_at']
    search_fields       = ['name', 'number', 'range', 'code', 'institute', 'stage', 'office']
```

```python
#research > tests.py
from rest_framework         import status
from rest_framework.test    import APITestCase

from research.models        import ResearchInformation

from django.core import serializers


class ResearchRetrieveTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        ResearchInformation.objects.create(
            name="조직구증식증 임상연구 네트워크 구축 및 운영(HLH)",
            number="C130010",
            period="3년",
            range="국내다기관",
            code="관찰연구",
            institute="서울아산병원",
            stage="코호트",
            target_number="120",
            office="Pediatrics",
            created_at="2021-11-16",
            updated_at="2021-11-16"
        )
        ResearchInformation.objects.create(
            name="대한민국 쇼그렌 증후군 코호트 구축",
            number="C130011",
            period="6년",
            range="국내다기관",
            code="관찰연구",
            institute="가톨릭대 서울성모병원",
            stage="코호트",
            target_number="500",
            office="Rheumatology",
            created_at="2021-11-16",
            updated_at="2021-11-16",
        )
        ResearchInformation.objects.create(
            name="Lymphoma Study for Auto",
            number="C100002",
            period="1년",
            range="단일기관",
            code="국내연구",
            institute="가톨릭대 서울성모병원",
            stage="Case-only",
            target_number="200",
            office="Hematology",
            created_at="2021-11-16",
            updated_at="2021-11-16"
        )

    #처음에는 검색 결과가 문자열로 그대로 일치하도록 작성하려고했는데 여의치 않아서 객체로 비교하도록 했다.
    def test_detail_view_success(self):
        response = self.client.get('/researches/C100002')
        
        expected_data_id = ResearchInformation.objects.get(number='C100002').id

        self.assertEqual(response.json()['id'], expected_data_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail_view_fail(self):
        response = self.client.get(
            '/researches/C140111'
            )

        self.assertEqual(response.json(), {"detail" : "Not found."})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
```


# 프로젝트 후기

나는 과제번호로 임상정보를 조회하는 기능을 담당했는데 쉬운 기능이라 빨리 끝나서 세원님이 필터를 구현하는 것을 옆에서 같이 보다가 필터기능을 작성했다면 아주 간단한 방법으로 여러개의 컬럼을 포함하는 검색 기능을 추가 구현할 수 있다는 것을 발견해서 알려드렸다. 저렇게 search_fields라는 한 줄로 원하는 컬럼을 전부 검색할 수 있다는 사실이 신기했고 저번 프로젝트에서 퓨어 장고로 구현했던 것보다 너무나 쉽고 간편해서 놀라웠다. 하지만 성능적인 측면에서 좋은 선택인지 알아봐야할 것 같다. 

