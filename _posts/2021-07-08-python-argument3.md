---
layout: post
category: python
tag: [기초, 위코드, TIL]
title: 파이썬 - 인수의 순서 및 위치
---

## 위치 인수와 가변 인수

아래의 함수를 실행하면 TypeError: func() missing 1 required keyword-only argument: 'age' 에러가 나게된다.

```python
def func_param_with_var_args(name, *args, age):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
 
func_param_with_var_args("정우성", "01012341234", "seoul", 20)
```

메소드를 호출할 때, 가변인수 이후 모든 인수를 가변인수로 인식하여 age인수에 아무 값도 들어오지 않았기 때문이다. 메소드를 호출할 때 인자 이름을 명시적으로 표기해주면 문제를 해결할 수 있다. 

```python
func_param_with_var_args("정우성", "01012341234", "seoul", age = 20)
```
아니면 아래와 같이 가변인수를 위치인수 뒤에 위치해야한다.

```python
def func_param_with_var_args(name, age, *args):
```

[출처 : 우공이산 블로그](https://hyun0k.tistory.com/entry/TIL-10-Function-Parameters)


## 위치 인수와 키워드 가변 인수

키워드 가변인수를 키워드 인수 앞에 쓰면 이렇게 신택스 에러가 난다.
![키워드 가변 인수의 위치 에러](/public/img/kwargs-error.png)

그래서 키워드 인수 address =0을 쓰고 그 뒤에 키워드 가변인수를 써줘야한다.

![인수의 올바를 위치 예시](/public/img/args-order.png)


## 위치 인수 > 디폴트 인수 > 가변인수 > 키워드 인수 > 키워드 가변인수

![인수의 위치와 순서](/public/img/python-function-definition-arguments-kind-and-order.jpeg)
 
모든 인수의 위치는 정리하자면 위와 같다.   
받게될 위치와 값이 정확한 인수들이 앞에 오고 가변적인 인수가 뒤에 온다.

## 주요 포인트 및 생각해볼 점

디폴트 인수와 키워드 인수는 똑같이 생겼다. 
함수를 직접 작성하다보면 이 개념들을 더 잘 이해할 수 있지 않을까?
