---
layout: post
category: python
tag: [기초, 나중에 살펴보기, TIL, codecademy]
title: 코데카데미 파이썬 기초과정 요약 - 리스트의 이해
---

## 리스트의 이해 List Comprehension

* 점수 리스트에 모두 10씩 더해보자
    ``` python
    grades = [85,90,42,50,64]
    scaled_grades = [grade+10 for grade in grades]
    print(scaled_grades)
    #결과
    # [95,100,52,60,74]
    ```
* 키 리스트에서 161을 넘는 키만 출력해보자
    ``` python
    heights=[161,164,156,170]
    can_ride_coaster = [height for height in heights if height > 161]
    print(can_ride_coaster)
    #결과
    # [164,170]
    ```
* old_list 중에서 어떤 조건에 맞는 것을 골라서 new_list에 넣어보자  
    ``` python
    new_list = [old_list[i] for i in range(len(old_list)) if different_list[i]<0]
    ```
    이 구문은 old_list의 모든 index 중에 0보다 작은 것들을 new_list에 넣게된다.  
    지금 와서 보니 different_list는 무엇을 의미하는지 모르겠다. -> 06.11 리스트 상관없이 조건식으로 넣어놓은 것 같다 

* 리스트 생성하기

    ```python
    numbers=[]
    for n in range(1,10+1):
        numbers.append(n)
    #위의 코드는 아래의 코드와 같다.
    numbers = [x for x in range(10)]
    ```

    ```python
    random_list = [random.randint(1,100) for i in range(101)]
    #1부터 100을 포함한 숫자 중 랜덤하게 숫자 100개를 뽑아 리스트를 만든다. 
    ```
## Indices

``` python
first_name = "Bob"
first_name[1:]
#결과
ob
```

``` python
favorite_fruit = "blueberry"
print(favorite_fruit[-3:])
#결과
rry
```