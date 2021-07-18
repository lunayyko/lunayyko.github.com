---
layout: post
category: django
tag: [입문, 위코드, TIL]
title: 장고 설정, CRUD1
---

# 장고 설정

## 장고 프로젝트 시작

- conda 가상환경 생성 및 가상환경 activate

```shell
conda create -n 가상환경이름 python=3.8
condo activate 가상환경이름
conda info --envs #설정한 가상환경 리스트 확인
```

- 프로젝트 시작을 위한 python package 설치

```shell
pip install 패키지이름 #파이썬 패키지 설치
pip install mysqlclient # mysqlclient설치
pip install django-cors-headers #CORS 해결을 위한 패키지
pip freeze #가상환경 패키지 리스트 확인
python -m pip install Django #장고 설치
```

- 장고 프로젝트 생성

```shell
django-admin startproject 프로젝트이름 #프로젝트 생성
python manage.py startapp 앱이름 #앱 생성(manage.py가 존재하는 디렉토리에서)
```

## settings.py 설정

```python
from pathlib        import Path #기존에 settings.py 에 있는 코드
from my_settings   import DATABASES, SECRET_KEY

SECRET_KEY = SECRET_KEY
DATABASES = DATABASES
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
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

추가 및 수정

### my_setting.py 파일 추가 (manage.py있는 디렉토리에)

```python
#클라우드에 올리지 않는, 키를 보관하는 파일
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westarbucks_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1', #데이터베이스의 IP주소, 이건 각자의 컴퓨터
        'PORT': '3306',
    }
}
SECRET_KEY ='_9^=58g2r*r(6@q7ugn!fxg-!fo48$7af9i4yn9-1$+bw(i'
#setting.py에 있던 시크릿 키를 붙여넣음
```

### urls.py수정

```python
from django.urls import path

urlpatterns = [
]
```

## 데이터베이스 생성

- mysql 데이터베이스 생성

```shell
mysql -u root -p #마이sql시작
```

```sql
create database 데이터베이스이름 character set utf8mb4 collate utf8mb4_general_ci; --utf8설정
show databases; --db보여주기
use wecode_23 쉘 명령어인가..? --사용할 db골라주기
show tables; --테이블들 보여주기
select * from django_migrations; --장고 마이그레이션 보여주기
desc products; --프로덕츠 내림차순으로 보여주기
```

mysql 나가기 키는 \q

## gitignore추가 (manage.py가 존재하는 디렉토리에)

toptal.com/developers/gitignore 에서 python,pycharm,visualstudiocode,vim,macos,linux,zsh을 추가해서 파일을 만들어 넣다.

<summary>git ignore 펼쳐서 보기</summary>

<div markdown="1">
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
```
</div>

## 실행

```python
pythong manage.py runserver
```

# CRUD 1

## ERD테이블

![스타벅스 페이지의 ERD](/public/img/starbucks_erd.png)
스타벅스 페이지를보고 데이터 관계도를 만들고 이를 보고 생성된 앱의 models.py에 migration을 만들어준다.

## migration

```python
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    #id는 장고가 자동으로 만들어주니까 클래스 객체에 안 넣어도 됨
    class Meta: #테이블 이름 지정
        db_table = 'menus' #안 쓰면 products_menus라고 컬럼이름 자동 생성
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, default='')
    #default에러가 떠서 디폴트를 추가했다 #외래키 쓸 때 장고가 알아서 _id를 붙여서 데이터베이스에 넘겨서 _id를 안 써도 된다.
    class Meta:
        db_table='categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    korean_name = models.CharField(max_length=45, default='')
    english_name = models.CharField(max_length=45, default='')
    description = models.TextField(max_length=300, default='')
    isnew = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) #cascade : 부모개체가 사라지면 자식도 사라지도록
    class Meta:
        db_table = 'products'
    def __str__(self):
        return self.name

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'
    def __str__(self):
        return self.name

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    products = models.ManyToManyField('Product', through='AllergyProduct')
    class Meta:
        db_table = 'allergies'

class AllergyProduct(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'allergies_products'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    size_ml = models.CharField(max_length=45,  null=True)
    size_fluid_ounce = models.CharField(max_length=45,  null=True)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'nutritions'
    def __str__(self):
        return self.name
```

## migration 만들고 migrate 실행하기

```python
python manage.py makemigrations #모델의 변경사항을 파악, 설계도 작성
python manage.py showmigrations products 0001 #현재 migrations가 어떤 상태인지 살펴보기
python manage.py sqlmigrate #실제 데이터베이스에 전달되는 SQL 쿼리문을 확인
python manage.py migrate #자동으로 migration을 실행
```

makemigration 클래스에 맞게 설계도를 만듦(설계도 확인)  
migrate 설계한대로 데이터베이스에 적용시키겠다(건설?)

## 쉘에서 CRUD하기

### CREATE

장고에서 미리 있는 models.Model을 이용해서 Person.objects.create 매쏘드를 이용해서 데이터를 만들 수 있다.

```python
python manage.py shell #파이썬에서 쉘 열기
>>>from products.models import Product
#쉘에서 장고를 연결해주려면 import해야함, 시작 전 작성한 모델 클래스 import
>>> products.object.create(name = “강경훈”, age =20) #이런식으로 쿼리셋 작성
exit() #쉘 종료하기
```

### READ

get은 쿼리셋을 1개, all(전부)과 filter는 쿼리셋을 많이 불러올 수 있고 쿼리셋에 담겨온 데이터들은 for문을 사용할 수 있다. filter는 쿼리셋을 0개 불러올 수도 있다.

## UPDATE

쿼리셋을 먼저 불러와야 update를 사용할 수 있다.  
어떤 모델매쏘드가 어떤 데이터타입을 어떻게 반환하는지 알아야한다.
