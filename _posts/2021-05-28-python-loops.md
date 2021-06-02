---
layout: post
title: 코데카데미 파이썬 기초과정 요약 - 반복문 05.28 TIL
---

영어의 압박을 이겨내고 코데카데미의 파이썬 기초과정을 풀고 있다. 앞의 내용을 숙지하지 못한 상태에서 뒤로가니 너무 어려워져서 그동안 배운 부분을 복습할 겸 기초과정을 요약하기로 했다.

# 반복문 Loops
## For loops

먼저, list는 변수를 묶어서 처리할 수 있도록 만들어진 목록 형식의 데이터 타입이다. 
예를 들어서 <strong>list = [0,1,2,3,4]</strong> 이면 이 리스트의 길이는 5이고 해당 리스트를 for loops 에서 in 뒤에 넣게되면 아래에 들여쓰여진 출력 명령을 5번 시행하라는 뜻이 된다.

``` python
for <temporary variable> in <list of length 5>:
    print("아무거나 원하는거")
```
``` c
//출력결과
아무거나 원하는거
아무거나 원하는거
아무거나 원하는거
아무거나 원하는거
아무거나 원하는거
```

두번째로, range 는 연속된 숫자로 이루어진 객체를 만드는 함수이다. 
``` python
>>>print(list(range(3)))
[0, 1, 2]
```

range를 사용하면 리스트를 갈음할 수 있다.

``` python
for temp in range(5):
    print("Learning Loops"+str(temp+1))
```

``` c
//출력결과
Learning Loops1
Learning Loops2
Learning Loops3
Learning Loops4
Learning Loops5
Learning Loops6
```

## While loops

``` python
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("발사!")
```
``` c
//출력결과
10
9
8
7
...
2
1
발사!
```

## While loops: Lists

``` python
python_topics=["var","control flow","loops","modules","classes"]
length = len(python_topics)
#파이썬토픽스의 길이는 6이 되겠다.
index = 0
#변수 선언

while index < length
    print("I am learning"+ python_topics[index])
    index += 1
    #한 번 실행할 때마다 인덱스 값에 1 을 더함
```

``` python
#출력결과
I am learning var
I am learning control flow
I am learning loops
I am learning modules
I am learning classes
```

## Loop Control : Continue

``` python
ages = [12,38,34,26,21,19,67,17]
for item in ages:
    if item < 21:
        continue
    else
        print(item)
```

``` python
#결과
38
34
26
21
67
```

## 중첩된 반복문 Nested Loops 
``` python
sales_data = [[12,17,22],[2,10,3],[5,12,13]]
scoops_sold = 0
for location in sales_data
    for i in location 
    scoops_sold += i
print(scoops_sold)
```
``` python
#결과
96
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
```
``` python
#결과
0,1,4,9,16,25,36,49,64,81
```

<i class="fa fa-info-circle" aria-hidden="true"></i> 주의:* 반복문에서 주의할 점

``` python
for i in range(3):
    print(5)
#결과
5
5
5
```

``` python
for i in range(3):
    print(i)
#결과
0
1
2
```










