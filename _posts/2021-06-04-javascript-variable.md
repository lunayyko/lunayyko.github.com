---
layout: post
category: javascript
tag: [기초, 나중에 살펴보기, 질문]
title: 코데카데미 자바스크립트 기초과정 요약 - 변수 06.04 TIL
---

let은 변수, const는 상수(바꿀 수 없는)인 변수이다.  
면접볼 때 면접관이 scope에 대해서도 말해보라고 했었다.  

<div class="message">
let과 const는 블록{} 범위이며(var는 함수 범위), let은 var와 마찬가지로 업데이트 될 수 있지만 블록 내에서 재선언을 할 수 없다.  
</div>

+var, let, const 모두 호이스팅되지만 let만 초기화(initialize)한다?



* 칼빈 293도일 때 섭씨와 화씨를 구해보자

```javascript
const kelvin = 293; //변하지 않는 상수
let celsius = kelvin - 273;
let fahrenheit = celsius * (9/5) + 32;
t = Math.floor(fahrenheit);
console.log('The temperature is '+t+' degrees fahrenheit.');
```


