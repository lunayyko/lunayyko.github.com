---
layout: post
category: algorithm(python)
tag: [입문, 위코드, TIL]
title: 코드카타 4주차 
---

# DAY1

## 문제
양수 N을 이진법으로 바꿨을 때, 연속으로 이어지는 0의 갯수가 가장 큰 값을 return해 주세요.

- 이어지는 0은 1과 1사이에 있는 것을 의미합니다.
- 이런 것을 binary gap 이라고 합니다.

예를 들어,

```
input: 9
output: 2
설명: 9의 이진수는 1001 입니다. 
1과 1사이에 있는 0은 2 이므로, 2를 return
```
```
input: 529
output: 4
설명: 529의 이진수는 1000010001 입니다. 
1과 1사이에 있는 연속된 0의 수는 4와 3입니다.
이 중 큰 값은 4이므로 4를 return
```
```
input: 20
output: 1
설명: 20의 이진수는 10100 입니다. 
1과 1사이에 있는 연속된 0의 수는 1 뿐입니다.
(뒤에 있는 0은 1사이에 있는 것이 아니므로)
```
```
input: 15
output: 0
설명: 15의 이진수는 1111 입니다. 
1과 1사이에 있는 0이 없으므로 0을 return
```
```
input: 32
output: 0
설명: 32의 이진수는 100000 입니다. 
1과 1사이에 있는 0이 없으므로 0을 return
``` 

### 제출코드

```python
def solution(N):
    arr = []
    count = 0
    max_count = 0
    arr = list(bin(N)[2:])
    for i in arr:
        if i == '0':
            count += 1
        if i == '1':
            if count > max_count:
                max_count = count
            count = 0
    print(max_count)
    return max_count
```

# DAY2

### 문제

prices는 배열이며, 각 요소는 매일의 주식 가격입니다.
만약 한 번만 거래할 수 있다면 = 사고 팔 수 있다면, 제일 큰 이익은 얼마일까요?

예를 들어,
```
Input: [7,1,5,3,6,4]
Output: 5
```
설명: 2일(가격=1)에 샀다가 5일(가격=6)에 사는 것이 6-1이라 제일 큰 수익
7-1=6 은 안 되는거 아시죠? 먼저 사야 팔 수 있습니다.

```
Input: [7,6,4,3,1]
Output: 0
```
설명: 여기서는 매일 가격이 낮아지기 때문에 거래가 없습니다. 그래서 `0`

## 제출 코드

```python
# 제일 작은 수를 먼저 찾고
# 배열을 그 뒤로 자름
# 자른 배열 안에서 가장 큰 값을 찾고
# 큰 값 - 작은 값 출력 
def maxProfit(prices):
    idx_min = prices.index(min(prices))
    new_arr = prices[idx_min:]
    return max(new_arr) - min(prices)
```

# DAY3

### 문제

다음과 같이 input이 주어졌을 때,
같은 알파벳으로 이루어진 단어끼리 묶어주세요.

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

output에서 순서는 상관없습니다.

## 사고과정

```python
# unique set 리스트를 만들어서
# 해당하는 셋 리스트의 키값에 딕셔너리 밸류값으로 넣고 밸류만 출력 -> 잘 안됨
# unique set 리스트와 비교해서 같으면 새 리스트에 넣기

def groupanagrams(strs):
    strs_list = []
    unique_list = []
    answer_dict = {}
    for i in strs:
        strs_list.append(i)
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)
```
여기까지 쓰고 이후에 2시간정도 고민했는데 풀지 못해서 다른 블로그를 찾아봤다.

## 제출코드

[출처 - Python: 알고리즘 - 딕셔너리 자료형](https://velog.io/@wltjs10645/Python-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%9E%90%EB%A3%8C%ED%98%95)

```python
def groupAnagrams(strs):
    counter = {}

    for s in strs:
        # 정렬된 문자열을 key로 만들어준다.
        key = ''.join(sorted(s))
 
        if key not in counter:
            counter[key] = []
        # 그리고 문자열을 해당 key에 할당해준다.
        counter[key].append(s)
     
    result = []
    for key in counter:
        result.append(counter[key])
     
    return result 
```

# DAY4

### 문제

숫자로 이루어진 리스트 nums를 인자로 주면,
그 안에서 어떤 연속적인 요소를 더했을 때 가장 큰 값이 나오나요?
가장 큰 값을 찾아 return해주세요.

```
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
```
설명: [4,-1,2,1] 를 더하면 6이 가장 크기 때문

### 제출답안
```python
def maxSubArray(nums):
  answers = []
  for m in range(0,len(nums)):
    for n in range(0,len(nums)):
      answers.append(sum(nums[m:n+1]))
      #m부터 n까지 합한 값 중에
  print(max(answers))
  #가장 큰 값을 출력
  return max(answers)
```

### 모범답안

```python
def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1] 
            print(nums)
    return max(nums)
```