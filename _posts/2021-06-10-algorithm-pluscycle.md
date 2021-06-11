---
layout: post
category: 알고리즘
title: 백준 더하기 사이클 06.10 TIL
---

[백준 더하기 사이클 문제](https://www.acmicpc.net/problem/1110) 

**사고 과정**

전의 두 숫자를 더한 값의 일의 자리가 새 숫자의 일의 자리가 되고  
전의 두 숫자 중 일의 자리가 새 숫자의 십의자리가 되는 사이클을 만들었다.

```python
n = int(input())

while true
    counter = i
    i++
    n = n[1]+(n[0]+n[1])[1]  
    if n == n:
        break
    print(counter)
```

물론 작동하지 않는다.  

**답안**

```python
num = int(input())
check = num #같은 값이지만 새 변수로 만들어야했다.
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    #new_num을 num에 넣어서 num이 계속 돌아가게 한다
    if new_num == check:
        break
print(count)
```
10분정도 고민하고 바로 답을 찾아보고 있는데 답을 너무 빨리 보는건가 싶다가도  
쉬운 문제지만 힌트 없이 풀려면 너무 진척이 없을 것 같다.     
앞의 쉬운 문제들은 조금 시간이 지난 뒤에 다시 풀어보면 좋지않을까싶다.    