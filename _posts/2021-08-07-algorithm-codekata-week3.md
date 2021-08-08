---
layout: post
category: algorithm(python)
tag: [입문, 위코드, TIL]
title: 코드카타 3주차 
---

## DAY1

### 문제
두 개의 input에는 복소수(complex number)가 string 으로 주어집니다.
복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.

input으로 받은 두 수를 곱해서 반환해주세요.
반환하는 표현도 복소수 형태의 string 이어야 합니다.

복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.

* 제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.

&nbsp

### 예제 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
설명: 
(1 + i) * (1 + i) = 1 + i + i + i^2 = 2i 
2i를 복소수 형태로 바꾸면 0+2i.

&nbsp

### 예제 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
설명: 
(1 - i) * (1 - i) = 1 - i - i + i^2 = -2i, 
-2i를 복소수 형태로 바꾸면 0+-2i.

&nbsp

### 예제 3:
Input: "1+3i", "1+-2i"
Output: "7+1i"
설명: 
(1 + 3i) * (1 - 2i) = 1 - 2i + 3i -6(i^2) = 1 + i + 6, 
7+i를 복소수 형태로 바꾸면 7+1i.

&nbsp

### 가정
input은 항상 a+bi 형태입니다.
output도 a+bi 형태로 나와야 합니다.

### 제출코드

```python
def complex_number_multiply(a, b):
    #(A+Bi)*(C+Di)
    list_a = a.split('+')
    A = int(list_a[0])
    B = int(list_a[-1][:-1])

    list_b = b.split('+')
    C = int(list_b[0])
    D = int(list_b[-1][:-1])

    num1 = str(A*C - B*D)
    num2 = str(A*D + B*C)

    return num1 +'+'+(num2 + 'i')
```

## DAY2

### 문제

숫자로 이루어진 배열인 nums를 인자로 전달합니다.

숫자중에서 과반수(majority, more than a half)가 넘은 숫자를 반환해주세요. 

예를 들어, 
```python
nums = [3,2,3]
return 3

nums = [2,2,1,1,1,2,2]
return 2
```

# 가정
`nums` 배열의 길이는 무조건 `2` 이상입니다.

### 사고과정

유니크한 숫자 세트 리스트 만들고, 각 숫자가 나온 개수를 카운트하고 두 개를 zip으로 묶어준다.
카운트가 과반수 이상이면 해당 키를 반환한다.

```python
import statistics

def more_than_half(nums):
    key_list = list(set(nums))
    value_list = []
    for i in key_list:
        value_list.append(nums.count(i))
    arr = list(zip(key_list, value_list))
    return key_list[value_list.index(max(value_list))]  
    # arr = {x:y for x,y in zip(key_list, value_list)}
```

자주나온 숫자를 많이 나온 순서대로 뽑아주는 카운터 내장함수를 사용하면 빠르고 간편하게 답을 찾을 수 있다.

```python
from collections import Counter

def more_than_half(nums):
  return Counter(nums).most_common(1)[0][0]
  # 카운터 매쏘드 내에 most_common함수를 사용하면 (n)개가 순서대로 출력됨
```

## DAY3

### 문제

s는 여러 괄호들로 이루어진 String 인자입니다.
s가 유효한 표현인지 아닌지 true/false로 반환해주세요. 

종류는 '(', ')', '[', ']', '{', '}' 으로 총 6개 있습니다. 아래의 경우 유효합니다.

한 번 괄호를 시작했으면, 같은 괄호로 끝내야 한다.
괄호 순서가 맞아야 한다.

예를 들어 아래와 같습니다.  

```python
s = "()"
return true

s = "()[]{}"
return true

s = "(]"
return false

s = "([)]"
return false

s = "{[]}"
return true
```

### 제출 코드

```python
def is_valid(string):
    paren_dict = {'(':')', '{':'}', '[':']'}
    temp = []
    for ch in string:
      if ch in list(paren_dict.keys()):
        #괄호가 열렸다면
        temp.append(ch)
        #열린 괄호를 템프에 넣는다
      else:
        #괄호가 열리지 않았다면
        if not temp:
          #템프리스트가 비어있다면(열린 적 없음)
          return False
        else:
          #템프리스트 안에 뭔가 들어있다면
          if ch != paren_dict[temp.pop()]:
            #템프리스트의 가장 마지막 원소를 빼낸 것이 parent_dict의 닫힌괄호와 짝이 맞지 않는다면
            return False
        if temp: #템프리스트 안에 내용물이 남아있다면
            return False
    return True
```

## DAY4

### 문제

`nums`는 숫자로 이루어진 배열입니다.

가장 자주 등장한 숫자를 `k` 개수만큼 return 해주세요.  

```python
nums = [1,1,1,2,2,3],
k = 2

return [1,2]

nums = [1]
k = 1

return [1]
```

### 제출코드

```python
def most_common(nums,k):
    num_list = []
    ans_list = []
    for i in set(nums):
        num_list.append(nums.count(i))  
    ans_list = list(zip(num_list, set(nums)))
    ans_list = sorted(ans_list)
    print(ans_list)
    answer = []
    for i in range(k):
        answer.append((ans_list.pop()[1]))
        print(answer)
    return answer
```

## DAY5

### 문제
인자인 height는 숫자로 이루어진 배열입니다.그래프로 생각한다면 y축의 값이고, 
높이 값을 갖고 있습니다. 

아래의 그래프라면 height 배열은 [1, 8, 6, 2, 5, 4, 8, 3, 7] 입니다.

![Graph](https://media.vlpt.us/images/khmin1017/post/5338b2d2-46cc-479a-8e0f-88aec95002f4/%EA%B7%B8%EB%9E%98%ED%94%84.png)

저 그래프에 물을 담는다고 생각하고, 물을 담을 수 있는 가장 넓은 면적의 값을 반환해주세요.  
### 가정
배열의 길이는 2이상입니다.

### 사고과정
첫번째로 위치한 높은 막대와 두번쨰로 위치한 높은 막대를 찾는다.
둘 사이의 거리 * 두번째로 높은 막대의 높이 : 담기는 물의 면적  
이라고 생각했는데 틀렸다.     
낮은 막대라도 면적이 더 넓을 수 있기 때문에 모든 두 막대 조합의 넓이를 구하고 그 중 가장 넓은 면적을 반환하는 것이 맞는 방법이다. 
### 제출코드

```python
def get_max_area(height):
    result = []

    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            if height[i] > height[j]:
                result.append(height[j]*(j-i))
            else:
                result.append(height[i]*(j-i))
    print(max(result))
    return max(result)
```