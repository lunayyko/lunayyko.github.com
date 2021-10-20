---
layout: post
category: django
tag: [입문, 위코드, TIL, 프로젝트]
title: 위코드 첫번째 프로젝트 탱고플레이트 2 RESTful API, property등, , 최종 구현 영상
---

## 탱고플레이트 최종 구현 영상


## view의 분류 기준

처음에 뷰 하나당 기능을 하나씩 넣었기 때문에 기능을 기준으로 뷰가 분류되는 것일까 생각했다. 
장고 공식문서에 보면 이렇게 나와있다.

> 각각의 뷰는 파이썬 함수(클래스 기반의 뷰에서는 매쏘드)로서 대변되고 장고는 URL요청에 따라 뷰를 선택하게 될 것이다.

프로젝트를 진행하다보니 뷰를 리소스 기준으로 나누는 것이 URI를 봤을때 어떤 기능인 지 알 수 있게(restful한 API) 작성하기 좋았다.  
예를 들어서 처음에는 레스토랑앱과 리뷰 앱을 따로 만들었는데 리뷰 페이지는 식당페이지에 붙어있었으니, 리뷰를 식당 앱에 같이 넣었으면 좋았겠다. 아래의 구조가 최적화된 뷰의 구조일 것 같다. 

![추천 엔드포인트](/public/img/view_endpoint.png)

*** 참고 RESTful API 작성 기준 ***

<table>
  <thead>
    <tr>
      <th>리소스</th>
      <th>POST</th>
      <th>GET</th>
      <th>PUT</th>
      <th>DELETE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>/customers</td>
      <td>새 고객 만들기</td>
      <td>모든 고객 검색</td>
      <td>고객 대량 업데이트</td>
      <td>모든 고객 제거</td>
    </tr>
    <tr>
      <td>/customers/1</td>
      <td>Error</td>
      <td>고객 1에 대한 세부 정보 검색</td>
      <td>고객 1이 있는 경우 고객 1의 세부 정보 업데이트</td>
      <td>고객 1 제거</td>
    </tr>
    <tr>
      <td>/customers/1/orders</td>
      <td>고객 1에 대한 새 주문 만들기</td>
      <td>고객 1에 대한 모든 주문 검색</td>
      <td>고객 1의 주문 대량 업데이트</td>
      <td>고객 1의 모든 주문 제거</td>
    </tr>
  </tbody>
</table>

[출처: RESTful web API 디자인](https://docs.microsoft.com/ko-kr/azure/architecture/best-practices/api-design)

## 탱고플레이트 최종 uri (RESTful API)

```python
#상위 프로젝트
urlpatterns = [
    path("users",include("users.urls")),
    path("",include("restaurants.urls")),
    path("restaurant",include("reviews.urls")),
]
#user 앱
urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/restaurant/<int:restaurant_id>/wish', WishView.as_view()), 
    path('/wishlist', WishListView.as_view()),
    path("/signin/kakao/callback", KakaoSignIn.as_view()),
]
#review 앱
urlpatterns = [
    path('/<int:restaurant_id>/review', ReviewView.as_view()),
    path('/<int:restaurant_id>/review/<int:review_id>', ReviewView.as_view()),
]
#restaurant 앱
urlpatterns = [
    path("restaurant/<int:restaurant_id>", RestaurantDetailView.as_view()),
    path("", RestaurantListView.as_view()),
    path("search", SearchView.as_view()),
]
```

## 기억에 남는 코드 및 로직 

### 쿼리셋 .last()
```python
"restaurant_img" : restaurant.review_set.last().reviewimage_set.last().image,
```
쿼리셋 안의 여러 객체 중 마지막 객체를 불러온다.

### aggregate
```python
"rating"      : restaurant.review_set.all().aggregate(Avg('rating'))
```
이렇게 하면 리뷰테이블의 별점 컬럼의 모든 별점값의 평균을 구해주는데 자동으로 {rating__avg : 5} 이런식으로 반환되서 키값을 원하는 이름으로 바꾸고 숫자5만 받고 싶으면 아래와 같이 쓰면 된다. 

```python
"rating"         : restaurant.review_set.all().aggregate(rating = Avg('rating'))['rating']
```

### annotate
```python
"wish_count"     : WishList.objects.filter(restaurant_id = restaurant_id).annotate(cnt=Count('user_id')).count(),
```
위시리스트 테이블에서 레스토랑 아이디가 해당 값인 경우 컬럼을 한 개 더 만들어서 유저 아이디의 갯수를 세서 새로 만든 컬럼에 보여준다.

### property 데코레이터 : 함수를 속성값으로 사용할 수 있게 해줌 
```python
from django.db    import models

class Restaurant(models.Model):
    name            = models.CharField(max_length=45)
    address         = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=50, null=True)
    location        = models.ForeignKey('Location',on_delete=models.CASCADE)
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    serving_price   = models.ForeignKey('ServingPrice', on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurants'
    
    @property
    def latest_review(self):
        if not self.review_set.exists():
            return None

        return {
            "id"          : self.review_set.last().id,
            "user_id"     : self.review_set.last().user_id,
            "user_name"   : self.review_set.last().user.nickname,
            "description" : self.review_set.last().description,
            "image"       : self.review_set.last().reviewimage_set.last().image
        }
```
레스토랑 뷰에서 한 레스토랑의 가장 최근 리뷰를 불러오는 쿼리셋이 복잡해지고 있었는데 모델에서 이렇게 함수를 선언하고 
@property 데코레이터로 속성(프로퍼티)으로 만들어놓으면 restaurant.latest_review 이런 식으로 바로 쓸 수 있다.

### transaction.atomic
```python
class ReviewView(View):
    @login_decorator
    @transaction.atomic
    def post(self, request, restaurant_id):
        try:
            data    = json.loads(request.body)
            user    = request.user

            if Review.objects.filter(user_id = user.id, restaurant_id=restaurant_id).exists():
                return JsonResponse({'MESSAGE':'REVIEW_EXIST'}, status=400)

            with transaction.atomic():
                review = Review.objects.create(
                    restaurant_id = restaurant_id,
                    user_id       = user.id,
                    description   = data['description'],
                    rating        = data['rating'],
                )

                with transaction.atomic():
                    ReviewImage.objects.create(
                        review_id = review.id,
                        image     = data['image'],
                        )

            return JsonResponse({'MESSAGE':'SUCCESS'},status = 201)
    
        except KeyError:
            return JsonResponse({'MESSAGE':'ERROR_INPUT_VALUE'}, status=404) 
```
리뷰와 리뷰이미지 테이블 2군데에 객체를 생성하는데 transaction.atomic을 사용하면 두 코드 중 하나가 실패했을 경우 첫번째 리뷰 객체만 생성되는 것이 아니라 첫번째가 롤백되서 둘 다 생성하지 않게된다. 


### 비회원처리

```python
def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token           = request.headers.get("authorization", None)
            if not token: # 토큰이 없으면 
                request.user = None #유저값에 none을 저장한다
            else:
                user            = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                request.user    = User.objects.get(id = user['id'])

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=400)

        except ObjectDoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)

    return wrapper 

```
그런데 이렇게 처리하니까 프론트엔드에서 비회원은 header를 전달하지 않고 회원은 header를 전달하도록 짜야했는데 그 부분을 어떻게 할 수 있는지 모르겠다.