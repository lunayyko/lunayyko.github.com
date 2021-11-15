---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제3 Wantedlab
---

# 과제 설명 요약
- 구현 기간 : 21.11.08(17시) ~ 21.11.10 (10시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY) 참조

# 사용한 기술 설명

# 내가 작성한 코드 / 기억에 남는 코드

헤더에서 언어를 받는 부분에서 

```python
class CompanySearchAPIView(views.APIView):

    def get(self, request):
        search  = request.GET.get('query', None)
        results = []

        if search is None:
            return response.Response(results, status=status.HTTP_200_OK)

        #
        language = request.headers.get('x-wanted-language', 'ko')

        c = {f'company_name__{language}__icontains': search}

        companies = Company.objects.filter(**c)
        company_serializer = CompanySerializer(companies, many=True)

        results = [{
             "company_name" : company['company_name'][language]
        } for company in company_serializer.data]

        return response.Response(results, status=status.HTTP_200_OK)
```


# 프로젝트 후기

