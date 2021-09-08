---
layout: post
category: django
tag: [입문, 위코드, TIL, 프로젝트]
title: 위코드 첫번째 프로젝트 탱고플레이트 1 ERD, models.py
---

## 망고플레이트 클론코딩 

### ERD 모델

![erd](/public/img/tangoplate_erd.png)


- 레스토랑, 장소, 카테고리, 가격대 테이블

레스토랑에는 아이디, 이름, 주소, 전화번호 이외에 필터 기능을 만들기 위한 위치 아이디, 카테고리 아이디, 가격대 아이디를 넣었고 메뉴테이블과 연결해서 레스토랑마다 가지고 있는 메뉴와 해당 메뉴의 가격이 나오도록 했다.

- 리뷰, 별점, 위시리스트 테이블

리뷰에는 레스토랑 아이디, 유저아이디, 리뷰 내용과 작성 날짜 및 수정날짜를 넣었다.
리뷰 한 개당 여러개의 사진이 들어갈 수 있도록 (일대다관계) 리뷰이미지 테이블을 따로 만들었다.  
별점 테이블에는 레스토랑 아이디, 별점, 유저아이디를 넣었다.  
<br>
별점만 줄 수도 있고 리뷰만 쓸 수도 있으니까 이렇게 잤는데 뷰를 짜다보니 리뷰와 별점이 한 테이블 안에 들어있지 않은 것이 좀 불편했다. 나중에 짤 때는 리뷰와 별점을 한 테이블에 넣고 리뷰를 남기려면 별점도 함께 입력해야 되도록 하는게 좋을 것 같다.

위시리스트에는 가고싶다가 클릭되었을때 열이 생성되고 가고싶다가 또 클릭되었을 때 해당 열이 지워지도록 레스토랑 아이디와 유저아이디를 넣었다.  

2021.08.13 -> 리뷰를 받고 별점을 리뷰테이블에 넣는걸로 수정했다. 테이블을 여러 개 만드는 것보다 컬럼을 여러 개 넣는 것이 비용이 덜 든다.

- 쿠폰(잇딜) 테이블

쿠폰 테이블에는 레스토랑 아이디, 가격, 설명, 사용기간을 넣고 쿠폰 역시 사진이 일대다관계로 연결될 것이라서 쿠폰 이미지 테이블을 따로 만들었는데 망고플레이트의 잇딜 페이지를 보면 잇딜1개당 사진이 1개 들어있어서 이미지를 쿠폰 테이블에 같이 넣었어도 되었을 것 같다.

### models.py

장고 앱 내에 coupons, restaurants, reviews, users 앱을 네개 만들고 각각 해당 모델을 넣었다. 

- users : User, Rating, WishList

```python
from django.db          import models

class User(models.Model):
    nickname     = models.CharField(max_length=50, null=True)
    email        = models.EmailField(max_length=200)
    password     = models.CharField(max_length=300)
    #비밀번호는 암호화되기 때문에 길게 주어야한다.
    phone_number = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'

class Rating(models.Model):
    user       = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    #참조하는 유저가 지워져도 별점 데이터는 남는다.
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    #참조하는 레스토랑이 지워지면 별점 데이터가 지워진다.
    rating     = models.IntegerField()

    class Meta:
        db_table = 'ratings'

class WishList(models.Model):
    user       = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    #참조하는 유저가 지워져도 위시리스트 데이터는 남는다.
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    #참조하는 레스토랑이 지워지면 위시리스트 데이터가 지워진다.

    class Meta:
        db_table = 'wishlist'
```

- restaurants : Restaurant, Menu, Location, Category, ServingPrice

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

class Menu(models.Model):
    restaurant     = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    item           = models.CharField(max_length=45)
    item_price     = models.DecimalField(max_digits= 10, decimal_places=0)
    #처음에 6으로 했더니 10만원이상이 입력이 안 되서 10으로 바꿨는데 PositiveIntegerField()로 했어도 될 것 같다. 

    class Meta:
        db_table = 'menus'

class Location(models.Model):
    area = models.CharField(max_length=45)

    class Meta:
        db_table = 'locations'

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class ServingPrice(models.Model):
    price = models.PositiveIntegerField()
    #가격이라서 양수 정수 필드를 사용한다.

    class Meta:
        db_table = 'serving_prices'

```

- reviews : Review, ReviewImage

```python
from django.db          import models

class Review(models.Model):
    user        = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    restaurant  = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True)
    created_at  = models.DateField(auto_now_add=True)
    #생성날짜는 자동으로 생기도록 했다.
    updated_at  = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    review     = models.ForeignKey('Review',on_delete=models.SET_NULL, null=True)
    image      = models.URLField(max_length=500)
    #500이면 충분하다고 생각했는데 url은 하도 길어서 길이 제한에 걸리는 경우가 종종 있었다.
    
    class Meta:
        db_table = 'review_images'
```

- coupon : Coupon, CouponImage

```python
from django.db          import models

class Coupon(models.Model):
    name           = models.CharField(max_length=40)
    restaurant     = models.ForeignKey('restaurants.Restaurant', on_delete=models.SET_NULL, null=True)
    price          = models.DecimalField(max_digits= 6, decimal_places=0)
    description    = models.CharField(max_length=500, null=True)
    start_date     = models.DateField()
    end_date       = models.DateField()

    class Meta:
        db_table = 'coupons'

class CouponImage(models.Model):
    coupon        = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True)
    image         = models.URLField(max_length=500)

    class Meta:
        db_table = 'coupon_images'
```

2주간 망고플레이트를 클론코딩하면서 시간상 잇딜부분은 구현하지 못했고 마지막으로 아래와 같은 erd를 사용하였다. 
![탱고플레이트 최종 erd]('/public/img/tango_erd.png')

1차에서는 1유저당 1식당에 1리뷰만 넣을 수 있게 했고, 1리뷰당 1리뷰이미지를 넣도록 했다.   
쿼리셋에서 맨 마지막 쿼리객체를 가져오는.last()라는 구문도 알게 되었고 restaurant.first_review() 이렇게 불러오기만 하면 되는 @property라는 것도 알게 되었고 list comprehension도 삼항연산자도 익숙해졌으니 2차프로젝트에서는 좀 더 실제 서비스에 가깝게 제한사항 없이 만들어보고 싶다.