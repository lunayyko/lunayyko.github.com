---
layout: post
category: django
tag: [입문, 위코드, TIL]
title: 장고 CRUD2 영화와 배우
---

# 장고 CRUD2 추가 과제 영화와 배우

![영화와 배우 ERD](/public/img/movie_erd.png)

## GET

2. 등록된 배우 목록을 리턴해주는 GET 메소드를 구현해주세요.
    - 배우의 이름, 성, 그리고 출연한 영화 제목 목록
3. 등록된 영화 목록을 리턴해주는 GET 메소드를 구현해주세요.
    - 영화의 제목, 상영시간, 출연한 배우 목록 (이름만)

## migration을 위한 models.py작성

```python
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    movie = models.ManyToManyField('Movie')
    class Meta:
        db_table='actors'
    def __str__(self):
        return self.first_name + self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    class Meta:
        db_table='movies'
    def __str__(self):
        return self.title
```

## migration 만들고 migrate 실행하기

sqlmigrate했을 때 나오는 구문은 아래와 같다.
```sql
-- Create model Movie
CREATE TABLE `movies` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `title` varchar(45) NOT NULL, 
    `release_date` date NOT NULL
    );

-- Create model Actor
CREATE TABLE `actors` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `first_name` varchar(45) NOT NULL, 
    `last_name` varchar(45) NOT NULL, 
    `birth_date` date NOT NULL
    );

CREATE TABLE `actors_movie` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `actor_id` bigint NOT NULL, `movie_id` bigint NOT NULL
    );

ALTER TABLE `actors_movie` ADD CONSTRAINT `actors_movie_actor_id_movie_id_01924769_uniq` UNIQUE (`actor_id`, `movie_id`);
ALTER TABLE `actors_movie` ADD CONSTRAINT `actors_movie_actor_id_1cdc8fdb_fk_actors_id` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`);
ALTER TABLE `actors_movie` ADD CONSTRAINT `actors_movie_movie_id_a197a03f_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`);
```
장고에서 manytomanyfield를 썼더니 포린키 actor_id, movie_id로 구성된 중간테이블이 자동으로 만들어졌다.

IntegerField뒤에 ()를 빼먹어서 아래와 같은 에러가 자꾸 났다.    
SyntaxError: EOL while scanning string literal  

### 쿼리셋을 이용한 shell에서의 CREATE

```shell
>>>from movie.models import Movie, Actor

>>> Movie.objects.create(title='good will hunting', running_time=127, release_date='1993-05-21')
<Movie: good will hunting>

>>> Movie.objects.create(title='martian', running_time=151, release_date='2015-10-08')
<Movie: martian>

>>> Actor.objects.create(first_name='Jessica', last_name='Chastain', birth_date='1977-03-24')
<Actor: JessicaChastain>  
#데이터가 알아서 성과 이름을 붙여서 저장해주는게 신기하다

>>> Movie.objects.create(title='miss sloane', running_time=132, release_date='2017-02-02')
<Movie: miss sloane>

>>> Actor.objects.create(first_name='Matt', last_name='Damon', birth_date='1970-10-08')
<Actor: MattDamon>
#ManytoManyfield를 사용해서 연결시켜주면 직접 Actor데이터에 movie_id를 넣을 수 
#없고 movie.set을 사용해서 넣어줘야한다고 한다.

>>> m1 = Movie.objects.get(id=1)
>>> a2 = Actor.objects.get(id=2)
>>> m1.actor.add(a2)
#AttributeError: 'Movie' object has no attribute 'actor'
#나는 Actor클래스에 ManyToManyField를 넣어줬기 때문에 
# movie에 actor를 넣어줄 수 없고 actor에 movie를 넣어줘야한다.
>>> a2.movie.add(m1)
>>> Actor.objects.get(id=1).movie.add(Movie.objects.get(id=3))
```
영화와 배우 테이블에 데이터 삽입하고 연결한 결과
![영화와 배우 테이블에 데이터 삽입하고 연결한 결과](/public/img/movie_db1.png)

영화와 배우 중간테이블에 데이터 삽입된 결과
![영화와 배우 중간테이블에 데이터 삽입된 결과](/public/img/movie_db2.png) 

# View 작성하기

1. 등록된 배우 목록을 리턴해주는 GET 메소드를 구현해주세요.
    - 배우의 이름, 성, 그리고 출연한 영화 제목 목록

2. 등록된 영화 목록을 리턴해주는 GET 메소드를 구현해주세요.
    - 영화의 제목, 상영시간, 출연한 배우 목록 (이름만)

```python
# movie > views.py
import json

from django.http import JsonResponse
from django.views import View

from movie.models import Movie, Actor

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results=[]
        for actor in actors:
            for movie in actor.movie.all():
            # 해당 배우가 출연한 영화를 모두 가져온다.
                results.append(
                {
                    "name" : actor.first_name + ' ' + actor.last_name,
                    "starred in" : movie.title 
                }
        )
        return JsonResponse({'result':results}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results=[]
        for movie in movies:
            results.append(
            {
                "title" : movie.title,
                "running time" : movie.running_time
            }
        )
        return JsonResponse({'result':results}, status=200)
```
```shell
http -v GET 127.0.0.1:8000/movie/actor
```
![결과1](/public/img/result1.png)


## urls.py

client로 부터 데이터 요청을 받으면 우선 제일 부모 폴더에 있는 urls.py로 받는다.

movie_project(상위 프로젝트 폴더) > urls.py
```python
from django.urls import path

urlpatterns = [
    path('movie', include('movie.urls'))
]
# 부모 urls.py, server로 movie 앱을 사용하겠다는 요청이 오면 movie로 보내주는 역할을 한다.
```
movie_project > movie(내부 앱 폴더) > urls.py
```python
from django.urls   import path
from movie.views     import MovieView, ActorView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view()),
    #as_view는 해당 경로까지 온 요청이 어떤 method인지 판단해주는 함수이다.
]
```

## GET으로 데이터베이스 JSON파일 형식으로 출력

```shell
http -v GET 127.0.0.1:8000/movie/movie
```
![전체 디비 출력](/public/img/movie_db.png)
 
## 주요 포인트 및 생각해볼 점

테이블끼리 넘나들면서 데이터를 가져오는 뷰를 작성하는 부분이 너무 헷갈려서  
쉘에서 쿼리셋을 치는 부분부터 다시 연습해봐야겠다.

[장고 쿼리셋 API 문서](https://docs.djangoproject.com/en/3.2/ref/models/querysets)    

[장고 ManyToMany 관계 문서](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/)

## 추가 쿼리셋 연습문제

1. 제시카 차스테인이 출연한 영화들을 리스트로 출력
```shell
>>> a0 = Actor.objects.get(id = 1)
>>> <Actor: JessicaChastain>

>>> a0.movie.all()
>>> <QuerySet [<Movie: martian>, <Movie: miss sloane>, <Movie: interstella>]>

>>> {movie.title for movie in a0.movie.all()}
>>> {'interstella', 'martian', 'miss sloane'}

>>> Movie.objects.filter(actor__id=1)
#역참조할 때는 밑줄을 두 개 
>>> <QuerySet [<Movie: martian>, <Movie: miss sloane>, <Movie: interstella>]>
```

2. 인터스텔라에 출연한 배우들 리스트 출력
```python
>>> Movie.objects.filter(title='interstella')
<QuerySet [<Movie: interstella>]>

>>> m1 = Movie.objects.get(title='interstella')
#위의 filter는 쿼리셋이기 때문에 변수로 쓰려면 get으로 한 개만 받아서 넣어줘야한다.

>>> m1.actor_set.all()
#역참조할 때는 _set 추가
>>> <QuerySet [<Actor: JessicaChastain>, <Actor: TimotheeChalamet>]>

>>> {actor.first_name +' '+ actor.last_name for actor in m1.actor_set.all()}
>>> {'Jessica Chastain', 'Timothee Chalamet'}
```



