---
layout: post
category: python
tag: [기초, 위코드, TIL]
title: 파이썬 - 모듈(Module)과 패키지(Package)
---

# 모듈

모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다. 

![파이썬과 모듈](/public/img/python-sys.png)

파이썬 안에는 여러가지 모듈이 있는데, os모듈을 이용하면 운영체제에서 파일을 생성하거나 경로를 변경하는 등의 작업을 할 수 있다. 

# sys 모듈

sys : System-specific parameters and functions.  
sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.  

[파이썬 공식문서](https://docs.python.org/ko/3/library/sys.html?highlight=sys%20modules#sys.modules)

## sys.module

import된 모듈과 패키지들을 딕셔너리 형태로 저장하고 있고 파이썬이 모듈이나 package를 찾기위해 가장 먼저 확인하는 곳이다.  
한 번 import된 모듈과 package들은 파이썬이 또 다시 찾지 않아도 되도록 하는 기능을 가지고 있다.

## sys.path

모듈을 찾을 때 참조하는 경로를 문자열 요소를 가진 리스트 형태로 저장한 것이다. 파이썬이 모듈과 패키지를 찾을 때 가장 마지막으로 보는 곳이다.

### 파이썬은 sys 모듈의 위치를 어떻게 찾을 수 있을까?

1. 전에 import했던 정보들을 저장해놓는 sys.modu.les를 확인하고
2. 파이썬에서 제공하는 공식 라이브러리들(built-in modules)을 확인한 뒤 
3. 각 경로들을 포함하고 있는 sys.path(list)에서 하나 하나 확인 과정을 거친다.

## Absolute path와 relative path

절대 위치는 최상위 디렉토리에서 시작해서 모듈 및 패키지의 시작부터 끝까지 생략, 축약되지 않고 명확히 명시된 경로를 표현해주는 것이고 상대 위치는 현재 파일의 위치를 기준으로 경로를 표현해주는 것이다.

## calculator 패키지 만들기

주어진 코드대로 패키지를 만들고 실행하면 다음과 같은 에러가 나온다.

![계산기 패키지 경로 에러](/public/img/calculator-package-error.png)

>ImportError: attempted relative import with no known parent package

상위패키지를 못 찾아서 발생하는 에러다. main은 항상 절대경로를 이용해야한다.
## add_and_multiply.py에서 multiply함수를 절대경로와 상대경로도 각각 임포트 해보고 main 모듈과 차이점을 생각해보고 결과를 출력해 보세요.

add_and_multiply.py 는 패키지 안에 들어있는 모듈이기 때문에 절대경로와 상대경로 모두 실행되며, main.py는 패키지 안에 들어있지 않기 때문에 상대경로는 실행이 안되고 절대경로만 실행이 된다.
## __init__.py의 역할

해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다. python3.3 버전부터는 __init__.py 가 없어도 패키지로 인식한다. 하지만 하위호환을 위해 생성하는 것이 안전하다.
