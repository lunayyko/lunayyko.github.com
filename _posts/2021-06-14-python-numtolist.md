---
layout: post
category: python
tag: [기초, 나중에 살펴보기]
title: 파이썬 숫자,문자,리스트,맵 연습 06.14 TIL
---

## 주어진 숫자의 갯수와 모든 자리수의 합을 구해보자

### str, int 의 구분

* 과정  
``` python
x = 1988
#int형은 iterate할 수 없다.
arr = list(str(x))
#1988을 \[1,9,8,8] 로 만들려면 먼저 int를 str으로 바꾸고 리스트로 묶어준다.
print arr
# 출력 : ['1', '9', '8', '8'] (str형 : iterate가 가능하다)
print (len(arr))
# 리스트의 갯수를 구하는 len()을 사용해서 숫자의 갯수를 구할 수 있다.
# 출력 : 4
int_arr = map(int, arr)
# str은 더하기가 안 되서 해당 숫자를 모두 더하려면 모든 숫자를 다시 인트로 만들어줘야한다.
print(int_arr)
#<map object at 0x1039d7df0>
int_arr = list(map(int, arr))
#map은 찢기만 하는거라서 리스트에 다시 넣어줘야 한다.
print(int_arr)
# 출력 : ['1', '9', '8', '8'] (int형 : 연산이 가능하다)
answer = sum(int_arr)
print(answer)
# 출력 : 26 
```

* 짧은 코드
```python
x = 1988
print(sum(list(map(int,list(str(x))))))
# 출력 : 26 
```

