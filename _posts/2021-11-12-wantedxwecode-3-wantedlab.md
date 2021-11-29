---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제3 Wantedlab(다국어회사이름검색)
---

# 과제 설명 요약
- 구현 기간 : 21.11.08(17시) ~ 21.11.10 (10시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY) 참조

아래와 같은 형태로 저장되어있는 데이터에서 헤더에서 받은 언어 설정값을 통해 회사를 검색하는 부분을 담당했다.

```python
company_name : {
    'ko': '라인',
    'en': 'Line',
    'ja': 'ライン'
}
```

# 모델링

다른 언어도 추가될 수 있도록 만들라는 전제가 있어서 확장성을 고려해서 JSONField를 사용하기로 했다.
![JSON](/public/img/json.png)
# 사용한 기술 설명
팀에서 세 분은 DRF를 사용할 줄 알았고 나와 지원님은 몰랐어서 이번 과제를 통해서 DRF를 공부하고 적용해보기로 했다. DRF를 바로 공부하고 바로 적용하는 것이 어려웠지만 태우님께서 공부할 수 있게 단계별로 DRF를 적용하는 코드를 보여주시고 지원님도 도와주셔서 세팅을 할 수 있었다.

# 내가 작성한 코드 / 기억에 남는 코드

헤더에서 언어를 받는 부분에서 처음에는 
```python
if request.headers['X-Wanted-Language'] is False:
            language = 'ko'
        else :
            language = request.headers['X-Wanted-Language']
```
이렇게 작성했는데 쿼리스트링(검색값)이 아예 없는경우에는 if문 작동까지가지도 못하고 500에러가 발생해서 팀장분께서 아래와 같이 리팩토링해주셨다.   

```python
class CompanySearchAPIView(views.APIView):

    def get(self, request):
        search  = request.GET.get('query', None)
        results = []

        if search is None:
            return response.Response(results, status=status.HTTP_200_OK)

        language = request.headers.get('x-wanted-language', 'ko')

        #JSON구조에 따라 depth 안 쪽으로 들어가서 company_name : { ko : 여기를 검색 } 하도록 함    
        c = {f'company_name__{language}__icontains': search}

        companies = Company.objects.filter(**c)
        company_serializer = CompanySerializer(companies, many=True)

        results = [{
             "company_name" : company['company_name'][language]
        } for company in company_serializer.data]

        return response.Response(results, status=status.HTTP_200_OK)
```


# 프로젝트 후기

팀원분들에 비해서 내가 정말 많이 부족하다는걸 느꼈다..! 배우는 속도가 느려서 내가 개발자가 될 수 있을까 의구심이 들었지만 내가 공부를 더 하면 될 일이고, 일단 백엔드를 3년간 열심히 해봐야겠다고 생각한다. 함께 프로젝트를 하는 팀원 분들이 정말 잘하고 열심히 하셔서 배울 점이 많다. 