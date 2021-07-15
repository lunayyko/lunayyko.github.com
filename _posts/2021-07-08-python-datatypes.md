---
layout: post
category: python
tag: [기초, 위코드, TIL]
title: 파이썬 - 튜플, 리스트, 셋, 딕셔너리(tuple, list, set, dictionary)
---


## 튜플 (1,2,3)

튜플은 변경이 불가능한 인자의 나열이고 메모리를 아끼거나 실수로 오염시키지 않기 위해 사용하는 원형의 데이터 타입이다.

```python
a = 1,2,3
print(a)
#(1,2,3)
```

## 리스트 \[1,2,2,3]

리스트는 튜플과 같지만 변형이 되는 자료형이다. 

## 셋 {1,2,3}

셋은 중복되지 않은 유니크한 값들만 들어있는 집합의 자료형이다. 

## 딕셔너리 {1:'일'}

딕셔너리는 키와 값이 한 쌍으로 이루어진 자료형이다.
## 파이썬에서 (), {}, []의 차이점
```python
  arr = [] # 빈 배열을 만들 때 []사용  
  arr = [1,2,3,4] #원소가 있는 배열을 만들 때 []사용  
  arr[3] #배열의 3번째 원소에 접근할 때 []사용  

  mytuple = () #빈 튜플 생성할 때 ()사용  
  mytuple = (1,2,3,4) # 원소가 있는 튜플을 만들 때 ()사용  
  mytuple[3] # 튜플의 원소에 접근할 때 []사용  

  mydictionary = {} #빈 딕셔너리 생성 시 {}사용  
  mydictionary = {"mouse":3, "penguin":5}  
  mydictionary["mouse"] # key("mouse")에 대응하는 value(3)에 접근할 때 사용  
  mydictionary["cat"] = 1 # key("cat")에 대한 value(1) 생성  
```
  [출처: 해시코드 - () [] {}의 차이와 사용해야 할 곳](https://hashcode.co.kr/questions/4118/%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%99%80-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC-%ED%95%A0-%EA%B3%B3)

# 적용 예시

-리스트   
JSON 포맷에서 사용된다    
배열을 변형할 때 유용한다    
데이터베이스에서 사용된다  

-튜플  
SQL쿼리로 데이터베이스에 값을 넣을 때 사용된다  
예: (1.’sravan’, 34).(2.’geek’, 35)  
괄호 체커에서 사용된다. -> ?  

-셋  
유니크한 값을 찾을 때 사용한다  
오퍼레이션끼리 더할 때 사용한다 -> ? 교집합 합집합할 떄?  

-딕셔너리  
리스트로부터 데이터 프레임을 만들어낼때 사용  
JSON에서 사용된다

[출처1: 코리팁스](https://corytips.tistory.com/161)  
[출처2: 긱스포긱스](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)