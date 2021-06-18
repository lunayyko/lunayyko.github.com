---
layout: post
category: python
tag: [기초, 나중에 살펴보기, TIL]
title: 파이썬 숫자,문자,리스트,맵 연습
---

## 주어진 숫자의 길이와 모든 자리수의 합을 구해보자

* 짧은 코드
    ```python
    x = input() #x값을 입력받는 부분
    print(len(list(str(x)))) #길이
    print(sum(list(map(int,list(str(x)))))) #자리수의 합
    ```

* 풀이 과정
    ``` python
    x = 1988 #예를 들어 1988을 입력받았다
    #입력받을 때 str로 받고 싶으면 x = str(input())
    #int형은 iterate할 수 없기 때문에 1988을 [1,9,8,8] 로 만들려면 
    #먼저 int를 str으로 바꾸고 리스트로 묶어준다.
    arr = list(str(x))
    print arr
    # 출력 : ['1', '9', '8', '8'] 
    print (len(arr))
    # 리스트의 갯수를 구하는 len()을 사용해서 숫자의 개수(길이)를 구할 수 있다.
    # 출력 : 4
    int_arr = map(int, arr)
    # str은 연산이 안 되서 해당 숫자를 모두 더하려면 모든 숫자를 다시 인트로 만들어줘야한다.
    print(int_arr)
    #이렇게 하면 이게 나온다. <map object at 0x1039d7df0> 
    #저장된 메모리 위치일까?
    int_arr = list(map(int, arr))
    #map은 찢기만 하는거라서 리스트에 다시 넣어줘야 한다.
    print(int_arr)
    # 출력 : ['1', '9', '8', '8'] 
    answer = sum(int_arr)
    print(answer)
    # 출력 : 26 
    ```

## 백준 입력값 받는 부분 

알고리즘 백준에서 변수 입력받는 부분이 항상 헷갈려서 정리해봤다.
프로그래머스에서는 이런 고민을 안 해도 되서 좋은데 문제가 더 어렵다.  

```python
#변수 한 개 입력받음
a = input() 

#변수 두 개 한 줄에 입력받음
a, b = input().split() 

#변수 여러 개 n 줄에 걸쳐 입력받음
for _ in range(n): 
    a = int(input())

#변수 여러개 한 줄에 입력받음
arr = list(map(int, input().split()))
```
