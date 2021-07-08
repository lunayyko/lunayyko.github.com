---
layout: post
category: python
tag: [입문, 프로젝트, TIL]
title: sys.argv를 이용해 숫자맞추기 게임 만들기
---

## sys.argv 

파이썬으로 작성된 파일을 실행할 때 인수(argument, 인자값)를 받아서 처리를 해야 되는 경우가 있다. 예를 들어, 로컬과 개발 등의 환경이 서로 달라서 인자값을 줘야 한다던지 같은 파일을 다른 목적으로 처리를 해야 할 때 인자값을 줄 수가 있을 것이다. 이럴때 파이썬에서는 sys.argv에 값을 담아 처리를 할 수 있게 된다.

```shell
#커맨드를 통해 hello.py 파일에 neo값을 주고 실행한다.
python3 hello.py neo
```
hello.py파일에서 sys를 임포트한다.
```python
import sys
print(sys.argv)
```
hello.py파일에서 sys.argv를 출력해보면 아래와 같이 나온다.

```shell
(base) C:\python>python hello.py neo ['hello.py', 'neo']
```
첫번째는 파일 이름, 두번째부터 입력된 인수값들이 나온다. 

출처: https://needneo.tistory.com/95 [네오가 필요해]

## sys.argv 를 이용한 숫자맞추기 게임을 만들어보자

[유데미 - complete python developer zero to mastery](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) 과정에서 만들었다.

```python
from random import randint
#random모듈에서 임의의 수를 뽑아주는 randint함수를 임포트한다
import sys
#sys모듈을 임포트한다
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
#1번째 수와 2번째 수 사이의 임의의 수를 뽑아서 answer변수에 저장한다.
#sys.argv를 사용함으로서 1번째 수와 2번째 수 매개변수를 다른 파일에서 가져올 수 있다.
while True:
    try: # 예외처리 try, except
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        #1번째 수와 2번째 수 사이의 수를 추측하세요 : 수를 입력받아서 guess변수에 저장
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            #0에서 11사이의 정수가 아닌 다른 것을 입력한 경우
            print('hey bozo, I said 1~10')
    except ValueError:
        #정수가 아닌 다른 것을 입력한 경우
        print('please enter a number')
        continue
```

주의 할 점은 guess의 위치가 while문 안에 들어있다는 것이다.  
sys.argv를 사용함으로서 인수값을 받거나 다른 파일에서 가져올 수 있었다.
