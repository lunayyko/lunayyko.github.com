---
layout: post
category: algorithm(python)
tag: [입문, 위코드, TIL]
title: 코드카타 1주차 
---

## DAY1

### 문제

`two_sum`함수에 숫자 리스트와 '특정 수'를 인자로 넘기면, 더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.


```
nums: 숫자 배열
target: 두 수를 더해서 나올 수 있는 합계
return: 두 수의 index를 가진 숫자 배열
```

예를 들어,

```
nums은 [4, 9, 11, 14]
target은 13 

nums[0] + nums[1] = 4 + 9 = 13 이죠?

그러면 [0, 1]이 return 되어야 합니다.
```

### 가정

`target`으로 보내는 합계의 조합은 배열 전체 중에 `2`개 밖에 없다고 가정하겠습니다.

### 제출코드

```python
def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if nums[i]+nums[j] == target:
        #주어진 수 둘의 조합이 합쳐서 target이 되는 경우 해당 수 출력
        return [i,j]
```

## DAY2

### 문제

reverse 함수에 정수인 숫자를 인자로 받습니다.

그 숫자를 뒤집어서 return해주세요.

x: 숫자

return: 뒤집어진 숫자를 반환!

예들 들어,

```
x: 1234
return: 4321
```

```
x: -1234
return: -4321
```

```
x: 1230
return: 321
```

### 제출 코드

```python
def reverse(number):
  if number > 0:
      return int(str(number)[::-1])
      #양수일때는 그냥 뒤집기
  if number < 0:
      return int('-'+str(number*-1)[::-1])
      #음수일때는 -뺐다가 붙임
  else:
      return 0 #0일때는 0
```

## DAY3

### 문제

String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

```
str: 텍스트
return: 중복되지 않은 알파벳 길이 (숫자 반환)
```

예를 들어,

```
str = "abcabcabc"
return 은 3
=> 'abc' 가 제일 길기 때문
```

```
str = "aaaaa"
return 은 1
=> 'a' 가 제일 길기 때문
```

```
str = "sttrg"
return 은 3
=> 'trg' 가 제일 길기 때문
```

### 제출코드

```python
def get_len_of_str(s):
    temp_list = []
    max_len = 0
    str_list = list(s)
    for i in str_list:
        if i in temp_list:
            temp_list=[]
            #2.해당 알파벳이 이미 리스트에 있다면 리스트를 비운다 
        temp_list.append(i)
        #1.처음 나오는 알파벳들을 리스트에 넣는다
        if len(temp_list) > max_len:
            max_len = len(temp_list)
            #3. 리스트의 길이가 현재까지 갱신된 최고 길이보다 길면 최고 길이를 갈음한다
    return max_len
```

## DAY4

### 문제

숫자인 `num`을 인자로 넘겨주면, 뒤집은 모양이 num과 똑같은지 여부를 반환해주세요.

```
num: 숫자
return: true or false (뒤집은 모양이 num와 똑같은지 여부)
```


예를 들어,

```
num = 123
return false 
=> 뒤집은 모양이 321 이기 때문
```

```
num = 1221
return true 
=> 뒤집은 모양이 1221 이기 때문
```

```
num = -121
return false 
=> 뒤집은 모양이 121- 이기 때문
```

```
num = 10
return false 
=> 뒤집은 모양이 01 이기 때문
```
### 제출코드

```python
def same_reverse(num):
  return str(num) == str(num)[::-1]
  #뒤집어서 같으면 True 다르면 False 반환
```

## DAY5

### 문제

strs은 단어가 담긴 배열입니다.

공통된 시작 단어(prefix)를 반환해주세요.  

예를 들어

```
strs = ['start', 'stair', 'step']
return은 'st'
```

```
strs = ['start', 'wework', 'today']
return은 ''
```

### 제출코드

```python
def get_prefix(strs):
    answer=[]
    strs = sorted(strs)
    #sort하면 a, ab, abc, ac 이렇게 정렬이 된다
    if strs == []:
      return ''
    #빈문자열 예외처리
    for i in range(len(strs[-1])):
        if strs[0][i] == strs[-1][i]:
          #첫문자와 마지막문자의 알파벳 비교
            answer.append(strs[0][i])
            #같으면 답에 넣는다 
        else:
          break
    return ''.join(answer)
```