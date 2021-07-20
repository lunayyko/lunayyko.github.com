---
layout: post
category: django
tag: [입문, 위코드, TIL]
title: 장고 CRUD2 주인과 강아지
---

위코드에서 CRUD 두번째 세션을 마치고 과제인 주인과 강아지를 하면서 진행 과정을 써보았다.

# 장고 CRUD2 과제 주인과 강아지

![주인과 강아지 ERD](/public/img/owner_erd.png)

## POST

각 기능을 서로 다른 클래스로 구현해주세요.

1. 신규 주인 등록
2. 강아지 등록 (주인정보 필요)

위 기능을 구현 후 직접 **httpie** 를 활용하여 주인 2명의 정보와 각 주인 당 2~3마리의 강아지 정보를 데이터베이스에 저장해주세요.

## GET

각 기능을 서로 다른 클래스로 구현해주세요.

1. 주인 리스트
    - 이름, 이메일, 나이 포함
2. 강아지 리스트
    - 이름, 나이, 주인 이름 포함
3. 주인 리스트 **(1번 코드에 추가)**
    - 이름, 나이 포함, **키우는 강아지 리스트 (이름, 나이 포함)**

# 진행 과정

## 초기 세팅 진행

- Miniconda 가상환경 생성 및 가상환경 activate
```shell
conda create -n dog python=3.8
conda activate dog
```
- Database 생성
```python
mysql -u root -p #마이sql시작
```
```sql
mysql> create database dog character set utf8mb4 collate utf8mb4_general_ci;
```
- 프로젝트 시작을 위한 python package 설치
```shell
pip install Django #장고 설치
pip install mysqlclient # mysqlclient설치 (mysql 먼저 설치 필요!!!)
pip install django-cors-headers #CORS 해결을 위한 패키지
```
- 장고 프로젝트 생성
```shell
django-admin startproject dog_owner #프로젝트 생성
cd dog #프로젝트 디렉토리로 들어감
python manage.py startapp dog #앱 생성(manage.py가 존재하는 디렉토리에서)
```

## 프로젝트 폴더(dog_owner)의 settings.py 설정

<details markdown="1">
<summary>setting.py파일 펼치기/접기</summary>

```python
from pathlib        import Path #기존에 settings.py 에 있는 코드
from my_settings   import DATABASES, SECRET_KEY

SECRET_KEY = SECRET_KEY
DATABASES = DATABASES
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 'django.contrib.admin', #admin도 
    # 'django.contrib.auth', #login auth도 직접 만들어쓸 예정이다
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # 추가
    'products', #새로 만든 앱 이름 추가
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', #추가
]
##CORS
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
        'NAME': 'dog',
        'USER': 'root',
        'PASSWORD': '',
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
</details>

## gitignore추가 (manage.py가 존재하는 디렉토리에)

<details markdown="1">
<summary>git ignore 펼쳐서 보기/접기</summary>

```python

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

#보안관련파일과 크롤링파일
my_setting.py
*.csv 

```
</details>

## 실행

```python
pythong manage.py runserver
```

# CRUD 2

## migration을 위한 models.py작성

```python
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    age = models.BigIntegerField
    class Meta: 
        db_table = 'owners' 
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, default='')
    age = models.BigIntegerField
    class Meta:
        db_table='dogs'  
    def __str__(self):
        return self.name
```

## migration 만들고 migrate 실행하기

```python
python manage.py makemigrations 
#모델의 변경사항을 파악, 설계도 작성(하고나서 만들어진 파일을 잘 살펴본다)
python manage.py showmigrations
#현재 migrations가 어떤 상태인지 살펴보기
python manage.py sqlmigrate dog 0001
#실제 데이터베이스에 전달되는 SQL 쿼리문을 확인
python manage.py migrate 
#자동으로 migration을 실행
```

sqlmigrate했을 때 나오는 구문은 아래와 같다.
```sql
BEGIN;
--
-- Create model Owner
--
CREATE TABLE "owners" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(45) NOT NULL, 
    "email" varchar(254) NOT NULL
    );
--
-- Create model Dog
--
CREATE TABLE "dogs" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(45) NOT NULL, 
    "owner_id" bigint NOT NULL REFERENCES "owners" ("id") DEFERRABLE INITIALLY DEFERRED
    );
CREATE INDEX "dogs_owner_id_b381d414" ON "dogs" ("owner_id");
COMMIT;
```
DEFERRABLE INITIALLY DEFERRED는 제약조건을 커밋할 때까지 연기하는거라고 하는데 아직 몰라도 될 것 같다.

## 에러

장고에는 원래 sqllite3가 있는데 위코드 커리큘럼에서 이걸 제거하고 mysql에 연결해주는 과정이 있었다. 그걸 하면서 settings.py에서 아래 코드를 지우고 DATABASES = DATABASES로 바꿨었는데 dog 장고앱을 만들면서 아래부분을 안 지웠더니 마이그레이션 이후에도 계속 mysql에 테이블이 생기지 않는 에러가 나서 2시간정도 고생하다가 다행히 학우분께서 이걸 찾아주셨다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#settings.py에서 이걸 지워야된다
```

### CREATE

```python
python manage.py shell 
```
```shell
>>>from dog.models import Dog, Owner
>>> Owner.objects.create(name='명주', email='abc@gmail.com')
<Owner: 명주>
>>> Owner.objects.create(name='경훈', email='123@gmail.com')
<Owner: 경훈>
>>> Owner.objects.create(name='은영', email='567@gmail.com')
<Owner: 은영>
>>> Dog.objects.create(name = '삼월', owner_id=1)
<Dog: 삼월>
>>> Dog.objects.create(name = '허순이', owner_id=2)
<Dog: 허순이>
>>> Dog.objects.create(name = '맹구', owner_id=2)
<Dog: 맹구>
```
![dog 테이블](/public/img/dog_db.png) 

### READ

```shell
>>> Dog.objects.all()
<QuerySet [<Dog: 삼월>, <Dog: 허순이>, <Dog: 맹구>]>
>>> Owner.objects.values()
<QuerySet [{'id': 1, 'name': '명주', 'email': 'abc@gmail.com'}, {'id': 2, 'name': '경훈', 'email': '123@gmail.com'}, {'id': 3, 'name': '은영', 'email': '567@gmail.com'}]>
>>> Dog.objects.values_list()
<QuerySet [(1, '삼월', 1), (2, '허순이', 2), (3, '맹구', 2)]>
```

# CRUD2

```
brew install httpie
```
httpie는 파이썬으로 개발된 http 클라이언트 유틸리티로 개발 및 디버깅 용도로 사용 가능하다.   
curl에 비해서 사용이 쉽고 가독성이 좋다. 

## View 작성하기

### READ

자원(resource)를 읽어 올 때, http method 중에 GET method를 사용합니다. url만 사용합니다.

```python
# dog>views.py
import json

from django.http import JsonResponse
from django.views import View

from dog.models import Dog, Owner
class DogView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        results=[]
        for dog in dogs:
            results.append(
            {
                "name" : dog.name,
                "owner" : dog.owner.name
            }
        )
        return JsonResponse({'result':results}, status=200)

class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()
        results=[]
        for owner in owners:
            results.append(
            {
                "name" : owner.name,
                "email" : owner.email,
                "dogs" : owner.dog.name
            }
        )
        return JsonResponse({'result':results}, status=200)
```

client로 부터 데이터 요청을 받으면 우선 제일 부모 폴더에 있는 urls.py로 받는다.

```python
#dog_owner(상위 프로젝트 폴더) > urls.py
#상위 프로젝트 폴더 dog_owner가 dog앱 안의 urls을 바라보게 만들어줌
from django.urls import path, include

urlpatterns = [
    path('dog', include('dog.urls'))
]
```
여기가 부모 urls.py 이다. 여기는 server로 오는 요청을 경로를 처리하는 파일이라고 생각하면 된다.
> localhost:8000/dog  
위의 경로로 dog app을 사용하겠다는 요청이 오면 다시 상세 app으로 보내주는 역할을 한다. 그 역할을 하는 것이 바로 include 이다. 그러면 그 해당 app 의 urls.py로 보내준다.  
근데 처음 startapp 으로 app 을 생성했을 때 urls.py는 존재하지 않는다. 그렇기 때문에 dog app 안에 새로 생성해줘여한다.

```python
#dog(하위 앱 폴더, urls.py새로 만들어주어야함) > urls.py
#하위 앱 폴더 dog에서 DogView를 연결
from django.urls   import path
from dog.views     import OwnerView, DogView
#OwnerView, DogView 는 view.py로부터 get, post 기능을 수행하는 클래스를 import해온다.

urlpatterns = [
    path('/dog', DogView.as_view()),
    path('/owner', OwnerView.as_view()),
    #as_view는 해당 경로까지 온 요청이 어떤 method인지 판단해주는 함수이다.
]
```

둘을 바꿔 넣어서 에러가 났었는데 동료분께서 찾아주셨다..!!

```python 
#url의 위치
.
├── manage.py
├── products
│   ├── models.py
│   ├── urls.py (없음, 새로 생성해야함)
│   └── views.py
└── westarbucks
    └── urls.py : main urls.py (부모, 요청 url 분석을 가장 먼저 하는 위치)
```

### CREATE

POST방식으로 개와 주인 데이터를 추가해보자.

```python
# dog>views.py
import json

from django.http import JsonResponse
from django.views import View

from .models import Dog, Owner

class OwnerView(View):
    def post(self, request):
        data  = json.loads(request.body)
        #view는 받아온 json 데이터를 template의 html 파일로 전달하고 템플릿으로 전달된 json 데이터는 자바스크립트에 의해 활용할 수 있는 형태로 다시 받아온다. 자바스크립트를 통해서 json 데이터를 자유롭게 사용할 수 있다.
        name = data['name']
        email= data['email']
        Owner.objects.create(name = name, email=email)        
        return JsonResponse({'Message':'Created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results=[]
        for owner in owners:
            dogs = [{"이름":dog.name} for dog in Dog.objects.filter(owner_id=owner.id)]
            #for문부터 읽어서, model에서 owner의 포린키 아이디(owner_id)가 오너의 아이디(owner.id)와 일치하는 개들을 filter로 불러와서 "이름": 값 형태로 dogs라는 변수에 저장한다.
            results.append(
            {
                "name" : owner.name,
                "email" : owner.email,
                "dog_list" : dogs
            }
        )
        return JsonResponse({'result':results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        owner = Owner.objects.get(name = data['owner'])
        # 프론트에서 준 데이터에서 오너의 이름을 가져오고 그거를 owner라는 변수에 대입 /Objects 출력
        dog = Dog.objects.create(name = name, owner = owner)
        return JsonResponse({'Message':'Created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results=[]
        for dog in dogs:
            results.append(
            {
                "name" : dog.name,
                "owner" : dog.owner.name
            }
        )
        return JsonResponse({'result':results}, status=200)
```
/dog/dog 해야되는걸 모르고 한시간정도 헤메였는데 한성봉님의 블로그를 보고 알게되었다.
[한성봉님의 블로그](https://velog.io/@ssaboo/TIL-no.49-Wecode-day.16Tue-django-C.R.U.D-2)

## POST 로 주인과 강아지 추가
```shell
http -v POST 127.0.0.1:8000/dog/dog name="땅콩" owner="경훈"
```
![주인과 강아지 추가](/public/img/post1.png)

## GET으로 데이터베이스 JSON파일 형식으로 출력

```shell
http -v GET 127.0.0.1:8000/dog/owner 
```
![전체 디비 출력](/public/img/dog_json.png)
 
## 주요 포인트 및 생각해볼 점

이 부분은 나는 다른 분 블로그를 보고 안 썼으면 정말 몰랐을 것 같다.
```python
dogs = [{"이름":dog.name} for dog in Dog.objects.filter(owner_id=owner.id)]
#for문부터 읽어서, model에서 owner의 포린키 아이디(owner_id)가 오너의 아이디(owner.id)와 일치하는 개들을 filter로 불러와서 "이름": 값 형태로 dogs라는 변수에 저장한다.
```