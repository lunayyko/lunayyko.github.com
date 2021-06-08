---
layout: post
category: 알고리즘
tag: [기초]
title: 파이썬과 자바스크립트 비교 - 백준 10430 나머지 06.05 TIL
---

파이썬과 자바스크립트의 차이를 살펴보고싶어서 알고리즘 백준에서 나머지를 구하는 문제를 살펴보았다.

## 문제

(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?  
(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?  
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

**입력**

첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

**출력**

첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
<br>

## 풀이

- 파이썬

```python
A,B,C = map(int,input().split())
# 입력받은 값들을 인트형으로 받아서 A, B, C 변수에 나누어 저장한다.
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
# sep으로 줄바꿈해준다
```

<br>

- 자바스크립트

```javascript
const fs = require("fs");
//파일 시스템 모듈을 사용한다
const input = fs.readFileSync("/dev/stdin").toString().split(" ");
//입력받는 값을 문자열로 만들고 공백으로 나눈다.
const A = parseInt(input[0]);
//첫번째 입력받은 값을 A에 저장한다.
const B = parseInt(input[1]);
const C = parseInt(input[2]);
//출력
console.log((A + B) % C);
console.log(((A % C) + (B % C)) % C);
console.log((A * B) % C);
console.log(((A % C) * (B % C)) % C);
```

한 줄짜리 문제라 언어를 비교하기는 어렵지만, 내 생각에는 파이썬을 잘 읽고 잘 쓰려면 생각을 더 해야될 것 같다. 알고리즘 풀 때는 파이썬이 더 쓰기 편할 것 같다. 아마 웹서비스를 만들때는 자바스크립트가 더 좋지 않을까?
