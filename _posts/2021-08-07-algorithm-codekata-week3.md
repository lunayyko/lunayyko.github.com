---
layout: post
category: algorithm(python)
tag: [입문, 위코드, TIL]
title: 코드카타 3주차 
---

# DAY1

### 문제
두 개의 input에는 복소수(complex number)가 string 으로 주어집니다.
복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.

input으로 받은 두 수를 곱해서 반환해주세요.
반환하는 표현도 복소수 형태의 string 이어야 합니다.

복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.

* 제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.

### 예제 1:
Input: "1+1i", "1+1i"  
Output: "0+2i"  
설명:   
(1 + i) * (1 + i) = 1 + i + i + i^2 = 2i   
2i를 복소수 형태로 바꾸면 0+2i.  

### 예제 2:
Input: "1+-1i", "1+-1i"  
Output: "0+-2i"  
설명:   
(1 - i) * (1 - i) = 1 - i - i + i^2 = -2i,   
-2i를 복소수 형태로 바꾸면 0+-2i.  

### 예제 3:
Input: "1+3i", "1+-2i"  
Output: "7+1i"  
설명:   
(1 + 3i) * (1 - 2i) = 1 - 2i + 3i -6(i^2) = 1 + i + 6,   
7+i를 복소수 형태로 바꾸면 7+1i.  

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

# DAY2

### 문제

문자로 구성된 배열을 input으로 전달하면, 문자를 뒤집어서 return 해주세요.

* 새로운 배열을 선언하면 안 됩니다.
* 인자로 받은 배열을 수정해서 만들어주세요.

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## 제출 코드

```python
def reverse_string(s):
    print (list(reversed(s)))
    return list(reversed(s))
```

# DAY3

### 문제

양수로 이루어진 m x n 그리드를 인자로 드립니다.  
상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.

한 지점에서 우측이나 아래로만 이동할 수 있습니다.  

Input:
[
&nbsp;&nbsp;  [1,3,1],
&nbsp;&nbsp;  [1,5,1],
&nbsp;&nbsp;  [4,2,1]
]

Output: 7  

설명: 1→3→1→1→1 의 합이 제일 작음  

## 제출코드

이 문제는 풀지 못하고 다른 블로그를 찾아봤다.

https://velog.io/@langssi/Python-Code-Kata-Day13

```python
def min_path_sum(grid):
  m = len(grid)
  n = len(grid[0])
    
  ### 1
  for i in range(1, n):
      grid[0][i] += grid[0][i-1]
  for i in range(1, m):
      grid[i][0] += grid[i-1][0]
        
  ### 2
  for i in range(1, m):
      for j in range(1, n):
          grid[i][j] += min(grid[i-1][j], grid[i][j-1])
  return grid[-1][-1] 
```

# DAY4

### 문제

주어진 숫자 배열에서, 0을 배열의 마지막쪽으로 이동시켜주세요.
원래 있던 숫자의 순서는 바꾸지 말아주세요.

* 새로운 배열을 생성해서는 안 됩니다.

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### 제출코드

```python
def move_zeroes(nums):
    num_of_zero = nums.count(0)
    for i in range(num_of_zero):
      nums.remove(0)
      nums.append(0)
    return nums
```

# DAY5 재귀 알고리즘

오늘은 재귀알고리즘에 대한 문제입니다.
재귀(recursion)란, 자신을 정의할 때 자기 자신을 호출하는 방법을 뜻합니다. 프로그래밍의 함수정의에서 많이 사용됩니다.

예)
```python
def countdown(n):
  print(n)
  countdown(n-1)

countdown(10);
```
countdown 함수는 받은 인자를 출력합니다.
그런데 위의 함수를 실행하면 10에서 시작해서 무한으로 마이너스 값까지 내려갑니다.

그래서 재귀함수는 아래의 절차가 꼭 필요합니다.
언제 멈출것인가?

위를 고려해 0이 되면 더이상 재귀를 이어나가지 않도록 종료 조건을 추가하겠습니다.

```python
def countdown(n):
  print(n)
  
  if (n == 0):
    return None
  
  countdown(n-1)

countdown(10);
```

재귀의 이론은 위와 같이 아주 간단합니다. 
재귀를 더 공부하고 싶은 분은 인터넷에 재귀 문제를 찾아 더 풀어보셔도 좋고, 알고리즘 책에서 재귀 부분만 더 읽으셔도 좋습니다.
### 문제
재귀를 사용하여 팩토리얼(factorial)을 구하는 함수를 구현해주세요.
팩토리얼이란 1에서부터 n까지의 정수를 모두 곱한것을 말합니다.

1! = 1
2! = 1 * 2
5! = 1 * 2 * 3 * 4 * 5
### 제출코드

```python
def factorial(n):
    if n <= 1:
      return 1
    return n * factorial(n-1)
```