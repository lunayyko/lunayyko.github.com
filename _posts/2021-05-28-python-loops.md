---
layout: post
category: python
tag: [기초, TIL, codecademy]
title: 코데카데미 파이썬 기초과정 요약 - 반복문
---

영어의 압박을 이겨내고 코데카데미의 파이썬 기초과정을 풀고 있다.   
앞의 내용을 숙지하지 못한 상태에서 뒤로가니 너무 어려워져서 그동안 배운 부분을 복습할 겸 기초과정을 요약하기로 했다.

# 반복문
## For loops

for loops을 돌리는데에는 두 가지 방법이 있는데, 똑같은 연산을 n번 수행하라고 하거나
해당 리스트의 모든 원소 i에 해당 연산을 수행하라고 할 수 있다.  

첫번째를 먼저 보자면 
``` python
for list in 3:
    print("아무거나 원하는거")

# 출력결과
# 아무거나 원하는거
# 아무거나 원하는거
# 아무거나 원하는거
```
뒤의 숫자를 list나 range로 갈음할 수 있다.
list는 변수를 묶어서 처리할 수 있도록 만들어진 목록 형식\[0,1,2]의 데이터 타입이다. 
예를 들어서 <strong>list = [0,1,2,3,4]</strong> 일때, 이 리스트의 길이는 5이기 때문에
해당 리스트를 in 뒤에 넣게되면 아래에 들여쓰여진 출력 명령을 5번 시행하라는 뜻이 된다.

``` python
for <temporary variable> in <list of length 5>:
    print("아무거나 원하는거")

# 출력결과
# 아무거나 원하는거
# 아무거나 원하는거
# 아무거나 원하는거
# 아무거나 원하는거
# 아무거나 원하는거
```

range 는 연속된 숫자로 이루어진 객체를 만드는 함수이다. 
``` python
print(list(range(3)))
[0, 1, 2]
```

range를 숫자나 리스트 대신 사용하면 아래와 같다.

``` python
for temp in range(5):
    print("Learning Loops"+str(temp+1))
# 출력결과
# Learning Loops1
# Learning Loops2
# Learning Loops3
# Learning Loops4
# Learning Loops5
# Learning Loops6
```

## While loops

while 반복문은 주어진 조건이 참인 동안에 연산을 수행하는 반복문이다.
``` python
countdown = 10
while countdown >= 0:
    #카운트다운이 0이상이 참인 동안에 연산을 수행
    print(countdown)
    countdown -= 1
print("발사!")

# 출력결과
# 10
# 9
# 8
# 7
# ...
# 2
# 1
# 발사!
```

## While loops: Lists

``` python
python_topics=["var","control flow","loops","modules","classes"]
length = len(python_topics)
#파이썬토픽스의 길이는 5
index = 0
#변수 선언

while index < length
    print("I am learning"+ python_topics[index])
    index += 1
    #한 번 실행할 때마다 인덱스 값에 1 을 더함
#출력결과
# I am learning var
# I am learning control flow
# I am learning loops
# I am learning modules
# I am learning classes
```

## Loop Control : Continue

앞서 말한 반복문의 두번째 사용예시로, 리스트 내의 모든 원소애 대해 연산을 수행해주는 반복문은 아래와 같이 쓴다.

``` python
ages = [12,38,34,26,21,19,67,17]
for item in ages:
    if item < 21:
        continue
    else
        print(item)
#결과
# 38
# 34
# 26
# 21
# 67
```

## 중첩된 반복문 Nested Loops 
``` python
sales_data = [[12,17,22],[2,10,3],[5,12,13]]
scoops_sold = 0
for location in sales_data
    for i in location 
    scoops_sold += i
print(scoops_sold)
#결과
#96
```

## 복습
```python
single_digits = list(range(10))
#single_digits = [0,1,2,3...8,9]
squares=[]
cubes=[]
for digit in single_digits:
    squares.append(digits**2)
    #제곱
    cubes.append(digits**3)
    #세제곱
print(squares)
#결과
# 0,1,4,9,16,25,36,49,64,81
```

<i class="fa fa-info-circle" aria-hidden="true"></i> 주의:* 반복문에서 주의할 점

``` python
for i in range(3):
    print(5)
#결과
# 5
# 5
# 5
```
5를 출력하라는 연산을 3번 반복한다

``` python
print(range(3)) # [0,1,2]
for i in range(3):
    print(i)
#결과
# 0
# 1
# 2
```
range(3)의 원소 i 를 모두 출력한다. 











