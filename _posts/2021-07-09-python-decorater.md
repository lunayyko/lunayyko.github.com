---
layout: post
category: python
tag: [입문, TIL]
title: 데코레이터(decorator)
---

## Decorator

 decorator를 한마디로 얘기하자면, 대상 함수를 wrapping 하고, 이 wrapping 된 함수의 앞뒤에 추가적으로 꾸며질 구문 들을 정의해서 손쉽게 재사용 가능하게 해주는 것이다.

출처: https://bluese05.tistory.com/30 [ㅍㅍㅋㄷ]

함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다.  
일반적으로 함수의 전처리나 후처리에 대한 필요가 있을때 사용을 한다.  
또한 데코레이터를 이용해, 반복을 줄이고 메소드나 함수의 책임을 확장한다.  

출처: https://hckcksrl.medium.com/ 

## 예시1

```python
def welcome_decorator(self):
  def wrapper():
    return self() + "welcome to WECODE!"
  return wrapper


@welcome_decorator
def greeting():
    return "Hello, "

print(greeting())
```
## 예시2
example.py
```python
class Decorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('전처리')
        print(self.function(*args, **kwargs))
        print('후처리')

@Decorator
def example():
    return '클래스'

#example() 실행
'''''''''
전처리
클래스
후처리
'''''''''
```

## 장고에서의 예시3

```python
from django.http import HttpResponse

def only_admin(f):
    def check(request, *args, **kwargs):
        try:
            if request.user.admin is not True:
                return JsonResponse({
                    'status': False,
                    'message': 'admin permission is required'
                })
        except:
            return JsonResponse({
                'status': False,
                'message': '\'sign in\' is required'
            })
        return f(request, *args, **kwargs)
    return check


@only_admin
def add_target(request):
    return HttpResponse('')
```
