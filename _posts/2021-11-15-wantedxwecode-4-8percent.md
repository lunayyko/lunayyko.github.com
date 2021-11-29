---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제4 8퍼센트(입출금거래내역)
---

# 과제 설명 요약
- 구현 기간 : 21.11.01(17시) ~ 21.11.13 (10시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment4) 참조

# 모델링

![모델링](/public/img/8percent_modeling.png)


# 사용한 기술 설명

DRF와 sqlite로 입금, 출금, 거래내역 조회를 구현하는 프로젝트에서 로그인, 회원가임, 유저정보 조회와 배포환경설정을 맡아서 구현했다.

DRF에서 Class Based View를 처음 사용했는데 만들어져 있는 기능을 자동으로 가져다 쓸 수 있는 것이 편했다.

Docker로 배포해본 적이 없어서 막연히 어려울 것 같다고 생각하고 있었는데 팀장분께서 컴포즈파일의 구성요소를 자세히 설명해주셔서 금방 이해할 수 있었다. 

# 내가 작성한 코드 / 기억에 남는 코드

```python
#users > model.py
from django.db                  import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


#BaseUserManager를 상속받아서 유저메니저 클래스가 유저를 생성하게된다
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            name  = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

#AbstractBaseUser에서 기본으로 만들어져있는 모델의 유저필드들을 받은 뒤 커스텀해서 사용한다
class User(AbstractBaseUser):
    email      = models.EmailField(max_length=255, unique=True)
    name       = models.CharField(max_length=20)
    is_admin   = models.BooleanField(default=False)
    username   = models.CharField(max_length=10, default='', null=True, blank=True)

    objects = UserManager()

    #유저네임대신 이메일로 로그인한다
    USERNAME_FIELD  = 'email'
    #은행업무이기 때문에 실명을 꼭 받도록했다.
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'users'
```


```python
#users > view.py
from rest_framework             import generics
from rest_framework.generics    import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth        import get_user_model

from .permissions               import IsOwner
from users.models               import User
from .serializers               import RegisterUserSerializer, UserSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class   = RegisterUserSerializer

#유저정보를 조회하는 코드, RetrieveAPIView를 사용해서 코드를 쓰지 않아도 자동으로 1개 객체의 정보를 조회하는 기능이 구현된다.  
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset           = get_user_model().objects.all()
    serializer_class   = UserSerializer
    permission_classes = [IsOwner]
```

```yml
#docker-compose.yml 파일
version: "3"
services: 
  wantedlab-backend: #컨테이너
    container_name: wantedlab-backend #docker compose run 했을 때 뜨는 이름
    build: 
      context: .
      dockerfile: ./Dockerfile-deploy #직접 빌드해서 쓸 도커파일 지정
    depends_on:
      - wantedlab_deploy_db #밑에 나오는 
    restart: always #커맨드가 터지면 다시 올릴거냐
    environment: # 시크릿키 직접 안쓰고 여기서 가져오겠다 하기 위한 환경설정
      SQL_HOST: wantedlab_deploy_db # 이렇게 쓰면 이 컨테이너의 아이피로 됨 
      SQL_PORT: 5432
      DJANGO_SETTINGS_MODULE: wantedlab.settings.deploy
    env_file: 
      - .dockerenv.deploy.backend
    command: #컨테이너가 커지면 실행되는 명령어
      - bash #터미널
      - -c #이걸 써야 여러줄 쓸 수 있다
      - | #이걸 써야 여러줄 쓸 수 있다
        python manage.py wait_for_db_connected -t 120 
        python manage.py migrate
        python manage.py collectstatic
        gunicorn wantedlab.wsgi:application --bind 0.0.0.0:8000
    volumes: #위 : 필요한 명령어를 쭉 치고 구니콘은 진짜 서버 돌리는 용, wantedlab이 프로젝트명(폴더명) 나머지는 구니콘 명령어
      - .:/usr/src/app/ # 이 컴터의 위치와 : 도커의 위치 동기화(도커파일의 워킹 디렉토리 설정해놓은 것 WORKDIR) 

  wantedlab_deploy_db: #이 컨테이너가 실행될 때까지 기다린다
    container_name: wantedlab_deploy_db
    image: postgres # 도커 허브에서 받아서 쓰는 포스트그레스 이미지
    restart: always
    volumes: #포스트그레스 이미지대로 세팅한거, 이렇게 데이터를 저장해줘야 컨테이너가 다운되도 데이터가 안 날아감
      - ./postgresql/data:/var/lib/postgresql/data
    environment: #포스트그래스 아이디 비번
      - POSTGRES_INITDB_ARGS=--encoding=UTF-8
      - TZ="Asia/Seoul"
    env_file:
      - .dockerenv.deploy.db

  wantedlab_nginx: #컨테이너
    image: nginx #엔지닉스는 스태틱 웹서버 구니콘은 다이나믹 웹서버 
    container_name: wantedlab_nginx
    volumes:
      - ./config/nginx:/etc/nginx/conf.d
      - ./static:/static
    ports:
      - "8021:8021" #로컬 : 쏴주는 포트끼리 연결
    environment:
      - TZ="Asia/Seoul"
    depends_on:
      - wantedlab-backend
```

이렇게 도커 컴포즈 yml파일을 만든 뒤 아래 명령어로 실행시켜서 도커를 이용해 띄우는 서버와 디비를 연결시킨다.

```
docker-compose -f docker-compose-deploy.yml up
```


# 프로젝트 후기

DRF로 특정 기능을 혼자서 구현한 것은 처음이었는데 개념을 이해하거나 세팅하는데는 시간이 오래 걸렸는데 정작 코드를 쳐서 내용을 구현하는 것은 정말 금방 끝났다.

하지만 유저를 생성하는 클래스의 경우 내부에서 어떻게 작동하는지 모르겠어서 이후의 프로젝트에서 계속 drf의 유저생성에 관련해서 어려움을 겪었다. 

공식문서 번역본의 예제 코드를 참고해서 작성했다.
https://kimdoky.github.io/django/2018/07/06/drf-Generic-views/


