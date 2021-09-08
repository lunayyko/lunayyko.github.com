---
layout: post
category: django
tag: [입문, 위코드, TIL, 프로젝트]
title: 위코드 두번째 프로젝트 험블벅 1 ERD, view 코드
---

## 텀블벅 클론코딩 

### ERD 모델

![erd](/public/img/humblebug_erd.png)


- 프로젝트 테이블

프로젝트에 필요한 정보를 모두 넣었다.

- 후원(Patron) 테이블, 후원옵션(Option) 테이블

프로젝트마다 후원 옵션이 여러개 있고 유저가 후원을 하게 되면 후원테이블에 프로젝트 아이디, 옵션 아이디가 들어가도록 했다.  
그런데 나중에 옵션 선택 후원 외에 금액을 추가해서 후원할 수 있는 기능을 추가구현해서 total_amount라는 컬럼을 추가해서 사용했다. 

### ProjectListView

- 필터 + limit, offset + 쿼리셋 최적화 코드가 들어가있다.

```python
class ProjectListView(View):
    def get(self, request):
        today = datetime.now()
        category_id = request.GET.get("categoryId")

        q = Q()

        if category_id:
            q &= Q(category_id = category_id)
        
        limit        = int(request.GET.get('limit', 12))
        #받는 limit값이 없으면 디폴트로 12개까지 부터 보여준다
        offset       = int(request.GET.get('offset', 0))
        #받는 offset값이 없으면 디폴트로 0개 부터 보여준다

        #하이라이트
        projects = Project.objects.annotate(total=Sum('patron__total_amount'), count=Count('patron')).prefetch_related('tag').select_related('user', 'category').filter(q).order_by('created_at')[offset:offset+limit]
        #패트론 테이블에서 레스토랑 아이디별로 total_amount컬럼 값을 합쳐서 저장하고 가상의 컬럼 patron__total_amount에 저장한다. 
        #정참조하는 user, category테이블의 내용을 골라서 가져오고 역참조하는 tag테이블의 내용을 미리 가져와서
        #q값(카테고리 아이디)으로 필터하고 예전에 만들어진 것부터 0부터12개 객체를 projects에 저장한다.  

        projects = [{
                'tag'             : [{'id':tag.id, 'name':tag.tag} for tag in project.tag.all()],
                'name'            : project.name,
                'id'              : project.id,
                'user_id'         : project.user_id,
                'user'            : project.user.nickname,
                'remaining_time'  : (project.end_date.replace(tzinfo=None) - today).days,
                #
                'main_image_url'  : project.main_image_url,
                'category_name'   : project.category.name,
                "aim_amount"      : project.aim_amount,
                'payment_date'    : project.end_date.strftime("%Y년 %m월 %d일"),
                #
                'collected_amount': project.total,
                'percentage' : '%.f%%'%(project.total/project.aim_amount*100) if project.total else '0%',
                #
                "created_at"      : project.created_at,
                "end_date"        : project.end_date, 
                "description"     : project.description
            } for project in projects]
            
        return JsonResponse({"project" : projects}, status=200)
```
