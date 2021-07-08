---
layout: post
category: python
tag: [기초, 나중에 살펴보기, TIL]
title: 파이썬 - 가변 인수(*args), 키워드 인수(**kwargs)
---

전 포스팅에서 키워드인수, 디폴트 인수에 대해 간단하게 다루었는데 이번에는 가변인수와 가변 키워드인수에 대해서 자세히 살펴본다.

# 가변 인수 (variable length arguments) *args

가변인수는 인수가 몇 개 들어올 지 모르는 상태에서 여러 개가 들어와도 처리할 수 있도록 하는 인수이다.  

```python
def f(x, *args):
    ...
```
별표를 붙여서 가변인수임을 나타내고 이름은 마음대로 정해도 된다.  

아래 함수를 살펴보면 고정 인수(또는 위치 인수)가 1개, 그리고 가변인수가 사용되었다.  
그러면 함수는 반드시 넘겨야하는 고정 인수를 나열하고, 나머지는 튜플 형식으로 한꺼번에 받는다.

```python
def function(a, *args): 
    print(a, args) 

function(1) # 1 () 
function(1,2) # 1 (2,) 
function(1,2,3,4,5) # 1 (2, 3, 4, 5) 
function(1,2,3,4,5,'a','b',[6,7,8],{'a':3, 'b':8}) 
# 1 (2, 3, 4, 5, 'a', 'b', [6, 7, 8], {'a': 3, 'b': 8})
```
출처: [매일 꾸준히, 더 깊이](https://engineer-mole.tistory.com/97)

가변인수는 개수가 정해져있는 위치 인수 뒤에 써주어야하고 1개만 사용할 수 있다.

## 언패킹

```python
x = [10, 20, 30]
print_numbers(*x)
10
20
30
```

리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서 print_numbers(10, 20, 30)과 똑같은 동작이 된다. 말 그대로 리스트의 포장을 푼다는 뜻이다.
[출처: 코딩 도장](https://dojang.io/mod/page/view.php?id=2345)

# 키워드 인수 (Keyword Arguments)

키워드 인수는 복습하자면 인수에 이름을 붙여준 것이다.

키워드 인수를 사용하면,   
1. 키워드 인수를 사용하면 디폴트 값을 가진 인수를 빼고 쓸 수 있다.
2. 읽기 쉽게 인수의 위치를 바꿀 수 있다.
3. 이름을 붙여줌으로서 각 인수가 나타내는 것이 무엇인지 더 분명히 알 수 있다.  

아래 함수는 output_file 과 contents 문자열을 받아서 압축파일을 만드는 함수이다.

```python
def write_gzip_file(output_file, contents):
    with GzipFile(None, 'wt', 9, output_file) as gzip_out:
        gzip_out.write(contents)
```
위치 인수 대신 키워드 인수를 사용하면 아래와 같이 쓸 수 있다.

```python
def write_gzip_file(output_file, contents):
    with GzipFile(fileobj=output_file, mode='wt', compresslevel=9) as gzip_out:
        gzip_out.write(contents)
```

첫번째 인수는 디폴트 값으로 None을 가지고 있는 파일이름 인수이다. 파일 객체 또는 파일이름 둘 다가 아닌 둘 중 하나만 GzipFile에 넘겨주면 되기 때문에 첫번째 인수로 쓰였던 파일이름이 필요하지 않다. -> 잘 모르겠음
compresslevel도 디폴트값이 9이기 때문에 써주지 않아도 된다.

```python
def write_gzip_file(output_file, contents):
    with GzipFile(fileobj=output_file, mode='wt') as gzip_out:
        gzip_out.write(contents)
```
우리가 이름지어진 인수(키워드 인수)를 사용했기 때문에 두 개의 인수를 생략하고 인수들을 읽기 좋은 순서로 재배치해줄 수 있었다. fileobj가 mode보다 중요하기 때문에 앞에 써주었다.

## *의 사용 : 위치 인수말고 키워드 인수만 입력받고 싶을 때

위치인수가 아닌 키워드 인수만 받고 싶을 때는 *뒤에 아무것도 붙이지 않고 써주면 된다. 

```python
from random import choice, shuffle
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = UPPERCASE.lower()
DIGITS = "0123456789"
ALL = UPPERCASE + LOWERCASE + DIGITS

def random_password(*, upper, lower, digits, length):
    chars = [
        *(choice(UPPERCASE) for _ in range(upper)),
        *(choice(LOWERCASE) for _ in range(lower)),
        *(choice(DIGITS) for _ in range(digits)),
        *(choice(ALL) for _ in range(length-upper-lower-digits)),
    ]
    shuffle(chars)
    return "".join(chars)
```

이 함수는 이름이 써져있는 인수(키워드 인수)만 받을 수 있다. 
```python
>>> random_password(upper=1, lower=1, digits=1, length=8)
'oNA7rYWI'
>>> random_password(upper=1, lower=1, digits=1, length=8)
'bjonpuM6'
>>> random_password(1, 1, 1, 8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: random_password() takes 0 positional arguments but 4 were given
```

출처 : https://treyhunner.com/2018/04/keyword-arguments-in-python/


# 가변 키워드 인수 (variable length keyword arguments) **kwargs

파이썬은 다른 프로그래밍 언어와 달리 함수가 받아들이는 인수의 이름을 알 수 있다. (키워드 인수를 쓸 수 있다)

```python
def f(x, y, **kwargs):
    ...
```
'**'오퍼레이터는 함수로 하여금 여러 개의 키워드 인수를 받아들이도록 한다. 

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
``` 
주어진 인수들은 **뒤에 쓰인 인수의 이름에 딕셔너리 형태로 저장된다.(키:값 두 개가 있어야 하니까) 

```python
def foo(a, b, *varargs, **kwargs):
    #가변인수와 함께 쓸 때는 가변인수 뒤에 키워드 가변인수를 쓴다.  
    print(a, b, varargs, kwargs)

## Call foo
foo(2, 9, 12, 34, x=3, name="bob")

## 출력값
2 9 (12, 34) {'x': 3, 'name': 'bob'}
```

복잡한 인수일수록 뒤로 가는 것 같다. 

## 디폴트 인수 (Default Arguments)
디폴트 인수는 값을 넣지 않고 호출했을 때 특정 값이 출력되도록 하는 인수이다.   

![위코드 - 디폴트인수](/public/img/wecode_default_param.jpeg)

출처: 위코드

함수를 정의할 때 default value parameter를 non-default value parameter 앞에 정의하면 안되는 이유1
```python
def multiply(a=2,b):
    print(a*b)

multiply(2)
```
메소드를 위와 같이 정의하면 SyntaxError: non-default argument follows default argument 가 발생한다. 그 이유는 만약에 메소드를 호출할 때 인자값을 1개만 전달하면 생략된 인자가 a 인지 b 인지 알 수가 없기 때문이다. 따라서 b 에도 기본값을 지정해주거나 기본값을 지정해준 인자를 맨 뒤로 이동시켜 메소드를 정의하면 문제를 해결할 수 있다.

```python
def multiply(a,b=2):
    print(a*b)

>> multiply(2)
4
```
[출처: 우공이산 블로그](https://hyun0k.tistory.com/entry/TIL-10-Function-Parameters)

함수를 정의할 때 default value parameter를 non-default value parameter 앞에 정의하면 안되는 이유2
```python
def remove_x(word, x='i'):
	return ''.join(word.split(x))

remove_x('mississippi')
'msssspp'
```
첫번째 함수는 내가 받을 인수가 word에 해당한다는 것이 확실하다.
```python
def remove_x(x='i', word):
	return ''.join(word.split(x))
SyntaxError: non-default argument follows default argument
``` 
두번째 함수는 내가 받은 인수가 i를 디폴트로 가지는 x인수 인지 word인수 인지 확실하지 않다.