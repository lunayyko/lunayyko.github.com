---
layout: post
category: django
tag: [입문, TIL]
title: 장고 게시판 CRUD 복습
---

복습을 위해서 장고에서 게시판 CRUD하는 것을 다시 해보았다.

## 장고 프로젝트 시작

- Miniconda 가상환경 생성 및 가상환경 activate

```shell
conda create -n 가상환경이름 python=3.8
conda activate 가상환경이름
conda info --envs #설정한 가상환경 리스트 확인
```
## 데이터베이스 생성

```shell
mysql -u root -p #마이sql시작
```

```sql
show databases; --mysql의 모든 db들 보여주기
use [데이터베이스이름]; --사용할 db골라주기
create database [데이터베이스이름] character set utf8mb4 collate utf8mb4_general_ci; --데이터베이스 생성 및 utf8설정(한중일)
show tables; --db안의 모든 테이블들 보여주기
```
mysql 나가기 키는 \q
컴퓨터에 mysql응용프로그램이 켜져있으면 터미널로 열리지 않을 수 있다. 

## 프로젝트 시작을 위한 python package 설치

```shell
pip install 패키지이름 #파이썬 패키지 설치

pip install Django #장고 설치
pip install mysqlclient # mysqlclient설치 (mysql 먼저 설치 필요!!!)
pip install django-cors-headers #CORS 해결을 위한 패키지

pip freeze #가상환경 패키지 리스트 확인
```

## 장고 프로젝트 생성

```shell
django-admin startproject 프로젝트이름 . #장고 프로젝트 생성
cd 프로젝트이름 #프로젝트 디렉토리로 들어감
python manage.py startapp 앱이름 #앱 생성(manage.py가 존재하는 디렉토리에서)
```
이때 프로젝트 다음에 점 기호(.)가 있음에 주의하자. 점 기호는 현재 디렉터리를 의미한다. 위 명령의 의미는 현재 디렉터리를 기준으로 프로젝트를 생성하겠다는 의미이다.  

.을 안 쓰면 현재 디렉터리 밑에 같은 이름의 앱 디렉터리가 생성되어 mysite/mysite와 같은 구조가 되어 버린다.

## settings.py 설정

```python
from pathlib        import Path #기존에 settings.py 에 있는 코드
from my_settings   import DATABASES, SECRET_KEY #my_settings.py에서 가져와야한다

#시크릿 키와 데이터베이스 변수는 my_settings파일을 만들어서 갈음한다.
SECRET_KEY = SECRET_KEY # 기존의 시크릿키 변수 삭제 후 대체
DATABASES = DATABASES # 기존의 데이터베이스 변수 삭제 필수!

ALLOWED_HOSTS = ['*'] #수정 : 모두 접속 가능

APPEND_SLASH = False #추가 : 슬래시 자동으로 삽입하지 않음

INSTALLED_APPS = [
    # 'django.contrib.admin', #admin도 
    # 'django.contrib.auth', #login auth도 직접 만들어쓸 예정이다
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # corsheaders 추가
    'products', #앱을 새로 만들면 여기에 추가해야한다
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', csrf 주석처리
    # 'django.contrib.auth.middleware.AuthenticationMiddleware', auth 주석처리
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', #corsheaders middleware 추가
]

# 데이터베이스 부분 삭제
# 뒷부분 생략

##CORS 부분 추가 
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
	#만약 허용해야할 추가적인 헤더키가 있다면?(사용자정의 키) 여기에 추가하면 됩니다.
)
```
위와 같이 settings.py를 추가 및 수정한다.

### my_setting.py 파일 추가 

시크릿 키와 디비정보가 깃에 공개적으로 노출되지 않도록 빼기 위해서  
manage.py있는 디렉토리에 my_setting.py라는 새 파일을 만들어서 추가한다. 

```python
#클라우드에 올리지 않는, 키를 보관하는 파일
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westarbucks_db',
        'USER': 'root',
        'PASSWORD': '', #원하는 db 비밀번호
        'HOST': '127.0.0.1', #데이터베이스의 IP주소, 이건 각자의 컴퓨터
        'PORT': '3306',
    }
}
SECRET_KEY ='_9^=58g2r*r(6@q7ugn!fxg-!fo48$7af9i4yn9-1$+...'
#setting.py에 있던 시크릿 키를 붙여넣음
```

### urls.py수정

```python
from django.urls import path

urlpatterns = [
]
```
## gitignore추가 (manage.py가 존재하는 디렉토리에)

소스를 공유하기 위해 깃을 사용하지만 올리고 싶은것 올리고 싶지 않은것, 올려서는 안되는 것들이 존재하고 이를 구분하기 위해 깃이 설치된 디렉토리에 `.gitignore`파일을 생성해서 관리해야 한다.  

gitignore.io

위의 사이트에서 사용하는 환경에 해당하는 키워드를 선택하면, 자동으로 .gitignore 파일에 정의할 요소들을 생성해준다.
> python,pycharm,visualstudiocode,vim,macos,linux,zsh

이 키워드들을 추가해서 파일을 만들고 마지막에 my_settings.py도 추가해준다.

보안관련파일과 크롤링파일
> my_settings.py (보안 관련 파일은 github에 업로드되면 안된다.) 

<details markdown="1">
<summary>git ignore 펼쳐서 보기/접기</summary>

```python

#보안관련파일과 크롤링파일을 위해서 추가하는 부분
my_settings.py
*.csv 
#아래부터 끝까지는 자동생성된 부분

# Created by https://www.toptal.com/developers/gitignore/api/python,pycharm,visualstudiocode,vim,macos,linux,zsh
# Edit at https://www.toptal.com/developers/gitignore?templates=python,pycharm,visualstudiocode,vim,macos,linux,zsh

### Linux

\*~

# temporary files which can be created if a process still has a handle open of a deleted file

.fuse_hidden\*

# KDE directory preferences

.directory

# Linux trash folder which might appear on any partition or disk

.Trash-\*

# .nfs files are created when an open file is removed but is still being accessed

.nfs\*

### macOS

# General

.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r

Icon

# Thumbnails

.\_\*

# Files that might appear in the root of a volume

.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share

.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### PyCharm

# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio, WebStorm and Rider

# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff

.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/\*\*/shelf

# AWS User-specific

.idea/\*\*/aws.xml

# Generated files

.idea/\*\*/contentModel.xml

# Sensitive or high-churn files

.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/\*\*/dbnavigator.xml

# Gradle

.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import

# When using Gradle or Maven with auto-import, you should exclude module files,

# since they will be recreated, and may cause churn. Uncomment if using

# auto-import.

# .idea/artifacts

# .idea/compiler.xml

# .idea/jarRepositories.xml

# .idea/modules.xml

# .idea/\*.iml

# .idea/modules

# \*.iml

# \*.ipr

# CMake

cmake-build-\*/

# Mongo Explorer plugin

.idea/\*\*/mongoSettings.xml

# File-based project format

\*.iws

# IntelliJ

out/

# mpeltonen/sbt-idea plugin

.idea_modules/

# JIRA plugin

atlassian-ide-plugin.xml

# Cursive Clojure plugin

.idea/replstate.xml

# Crashlytics plugin (for Android Studio and IntelliJ)

com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based Rest Client

.idea/httpRequests

# Android studio 3.1+ serialized cache file

.idea/caches/build_file_checksums.ser

### PyCharm Patch

# Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721

# \*.iml

# modules.xml

# .idea/misc.xml

# \*.ipr

# Sonarlint plugin

# https://plugins.jetbrains.com/plugin/7973-sonarlint

.idea/\*\*/sonarlint/

# SonarQube Plugin

# https://plugins.jetbrains.com/plugin/7238-sonarqube-community-plugin

.idea/\*\*/sonarIssues.xml

# Markdown Navigator plugin

# https://plugins.jetbrains.com/plugin/7896-markdown-navigator-enhanced

.idea/**/markdown-navigator.xml
.idea/**/markdown-navigator-enh.xml
.idea/\*\*/markdown-navigator/

# Cache file creation bug

# See https://youtrack.jetbrains.com/issue/JBR-2257

.idea/$CACHE_FILE$

# CodeStream plugin

# https://plugins.jetbrains.com/plugin/12206-codestream

.idea/codestream.xml

### Python

# Byte-compiled / optimized / DLL files

**pycache**/
_.py[cod]
_$py.class

# C extensions

\*.so

# Distribution / packaging

.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
_.egg-info/
.installed.cfg
_.egg
MANIFEST

# PyInstaller

# Usually these files are written by a python script from a template

# before PyInstaller builds the exe, so as to inject date/other infos into it.

_.manifest
_.spec

# Installer logs

pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports

htmlcov/
.tox/
.nox/
.coverage
.coverage._
.cache
nosetests.xml
coverage.xml
_.cover
\*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations

_.mo
_.pot

# Django stuff:

\*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:

instance/
.webassets-cache

# Scrapy stuff:

.scrapy

# Sphinx documentation

docs/\_build/

# PyBuilder

.pybuilder/
target/

# Jupyter Notebook

.ipynb_checkpoints

# IPython

profile_default/
ipython_config.py

# pyenv

# For a library or package, you might want to ignore these files since the code is

# intended to run in multiple environments; otherwise, check them in:

# .python-version

# pipenv

# According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.

# However, in case of collaboration, if having platform-specific dependencies or dependencies

# having no cross-platform support, pipenv may install dependencies that don't work, or not

# install all needed dependencies.

#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow

**pypackages**/

# Celery stuff

celerybeat-schedule
celerybeat.pid

# SageMath parsed files

\*.sage.py

# Environments

.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings

.spyderproject
.spyproject

# Rope project settings

.ropeproject

# mkdocs documentation

/site

# mypy

.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker

.pyre/

# pytype static type analyzer

.pytype/

# Cython debug symbols

cython_debug/

### Vim

# Swap

[._]_.s[a-v][a-z]
!_.svg # comment out if you don't need vector files
[._]\*.sw[a-p]
[._]s[a-rt-v][a-z]
[._]ss[a-gi-z]
[._]sw[a-p]

# Session

Session.vim
Sessionx.vim

# Temporary

.netrwhist

# Auto-generated tag files

tags

# Persistent undo

[._]\*.un~

### VisualStudioCode

.vscode/_
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
_.code-workspace

# Local History for Visual Studio Code

.history/

### VisualStudioCode Patch

# Ignore all local history of files

.history
.ionide

### Zsh

# Zsh compiled script + zrecompile backup

_.zwc
_.zwc.old

# Zsh completion-optimization dumpfile

_zcompdump_

# Zsh zcalc history

.zcalc_history

# A popular plugin manager's files

.\_zinit
.zinit_lstupd

# zdharma/zshelldoc tool's files

zsdoc/data

# robbyrussell/oh-my-zsh/plugins/per-directory-history plugin's files

# (when set-up to store the history in the local directory)

.directory_history

# MichaelAquilina/zsh-autoswitch-virtualenv plugin's files

# (for Zsh plugins using Python)

# Zunit tests' output

/tests/\_output/\*
!/tests/\_output/.gitkeep

# End of https://www.toptal.com/developers/gitignore/api/python,pycharm,visualstudiocode,vim,macos,linux,zsh
```
</details>

## 실행

```python
pythong manage.py runserver
```

## requirements.txt 추가

```python
pip freeze > requirements.txt
```
이렇게 manage.py가 있는 디렉토리에 설치된 라이브러리의 버전을 명시해준다.

```python
Django==3.2.6
django-cors-headers==3.7.0
mysql-client==0.0.1
PyMySQL==1.0.2 #맥 M1의 경우 설치한 파일
```
장고에서 자동으로 설치되는 것을 제외하고 직접 설치한 것들만 남겨주면 좋다.

## 디렉토리 구조

```python
(참고) 프로젝트 디렉토리 구조 구조
└── mysite
    ├── manage.py
    ├── my_settings.py
    ├── READEME.md
    ├── requirements.txt
    └── mysite
        ├── \__init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    └── myapp
        ├── \__init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        └── views.py

```

## Model.py

필요한 게시판의 데이터 관계도를 만들고 새로 생성된 앱의 models.py에 아래 migration을 넣어서 데이터베이스 토대를 만들어준다.

```python
#project > users > models.py
from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=40, null=True)
    #null=True를 넣으면 값이 들어오지 않아도 에러가 나지 않는다.
    email        = models.EmailField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)
    age          = models.PositiveIntegerField(null=True)
    phone_number = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'users' #디비 이름 네이밍 컨벤션 : 소문자 복수형

class Post(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    #User테이블의 id를 참조하는 'user_id'이름의 컬럼을 만든다.
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'posts'
```

## migration 만들고 migrate 실행하기

```python
python manage.py makemigrations 
#모델의 변경사항을 파악, 설계도 작성(하고나서 만들어진 파일을 잘 살펴본다)
python manage.py showmigrations 
#현재 migrations가 어떤 상태인지 살펴보기
python manage.py sqlmigrate [앱이름] [마이그레이션번호]
#실제 데이터베이스에 전달되는 SQL 쿼리문을 확인
python manage.py migrate 
#자동으로 migration을 실행
```
migration을 만드는 것과 migrate는 각각 
클래스에 맞게 설계도를 만들고 설계한대로 데이터베이스를 건설하겠다는 뜻이라고 할 수 있다. 

## SQL
```sql
select * from django_migrations; --장고 마이그레이션 보여주기
desc posts; --포스트 테이블이 잘 만들어졌는지 보여준다
```

## View.py 회원가입, 로그인 구현

```python
#mysite > users > views.py
import json, re, bcrypt, jwt

from django.views         import View
from django.http          import JsonResponse

from users.models         import User  

from my_settings          import SECRET_KEY, const_algorithm

class SignUpView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email           = data['email']
            password        = data['password']
            hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

            if User.objects.filter(email=email).exists():
                return JsonResponse({"MESSAGE": "EMAIL_ALREADY_EXIST"}, status=400)

            if not re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status=400)

            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", password):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status=400)

            User.objects.create(
                name     =   data.get('name'), #선택적으로 입력받을 때
                email    =   email,
                password =   hashed_password.decode('UTF-8'),
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)      
            email    = data['email']
            password = data['password']        

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE':'INVALID_VALUE'}, status = 401)

            if bcrypt.checkpw(password.encode('utf-8'),User.objects.get(email=email).password.encode('utf-8')):
                nickname = User.objects.get(email = email).nickname
                token = jwt.encode({'id':User.objects.get(email=email).id}, SECRET_KEY, algorithm=const_algorithm)
            
                return JsonResponse({'TOKEN': token, "EMAIL":email, "NICKNAME":nickname}, status = 200)

            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)
```

## View.py 게시글 기능 구현

```python
import json

from django.views   import View
from django.http    import JsonResponse

from django.core.paginator import Paginator

from posts.models   import Post  
from users.models   import User

class Post(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            Post.objects.create( #디비에 값을 추가
                user_id      = request.user.id, #요청을 수행하는 유저의 아이디 
                text     = data["text"]#입력받은 값
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request):
            posts = Post.objects.all() 
            #업로드모델에 따라 객체를 다 가져와서 저장

            #posts 페이징 처리
            page      = request.GET.get('page','1')
            #GET 방식으로 정보를 받아오는 데이터
            paginator = Paginator(posts, '10')
            #Paginator(분할될 객체, 페이지 당 담길 객체수)
            page_obj  = paginator.page(page)
            #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
            results = []

            for post in posts: #저장된 객체들을 한 개씩 돌면서
                results.append({
                    "user_id"    : post.user_id,#글 객체의 유저아이디
                    "text"       : post.text,
                    "created_at" : post.created_at,
                })
            return JsonResponse(({"results": results}, {'page_obj':page_obj}), status=200)

class PostModify(View):
    def patch(self,request, post_id):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=post_id)
            
            if post.user_id == request.user.id : #요청하는 유저가 글 쓴 사람이라면
                Post.objects.update( 
                    text     = data["text"]
                )
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
    def delete(self,request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.user_id == request.user.id:
                post.delete()
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

```

### 4. Urls.py 작성

클라이언트의 요청을 받아서 게시판 뷰를 호출할 수 있도록 urls.py 를 작성해야합니다.

```python
#상위 mysite프로젝트 폴더의 urls.py
from django.urls import path,include

urlpatterns = [
    path("users",include("users.urls")),
    path("post",include("post.urls"))
]
```
```python

#하위 post앱 폴더의 urls.py
from django.urls import path
from .views      import post

urlpatterns = [
    path("", Post.as_view()),
    path("<int:post_id>", PostModify.as_view())
]
```
POSTMAN을 이용해서 Headers에 Authorization값을 넣고 Body에 JSON형식으로 값을 넣어서 디비에 텍스트가 잘 입력된 모습을 볼 수 있다.
![업로드](/public/img/upload.png)
