---
layout: post
category: javascript
tag: [기초, 나중에 살펴보기, 질문]
title: 코데카데미 자바스크립트 기초과정 요약 - 변수 06.04 TIL
---

let은 변수, const는 상수(바꿀 수 없는)인 변수이다.  
면접볼 때 면접관이 scope에 대해서도 말해보라고 했었는데 대답을 제대로 못한 적이 있다. (이불킥...)

<div class="message">
let과 const는 블록{} 범위이며(var는 함수 범위), let은 var와 마찬가지로 업데이트 될 수 있지만 블록 내에서 재선언을 할 수 없다.  
</div>

* var, let, const 모두 호이스팅되지만 let만 초기화(initialize)한다?

변수의 3단계 생성과정  
변수는 아래와 같이 3단계의 과정을 통해 생성된다.  
선언단계 : 변수를 실행컨텍스트의 변수객체에 등록한다.  
초기화 단계 : 실행 컨텍스트에 등록 된 변수객체에 대한 메모리를 할당한다. 이 단계에서 변수는 undefined로 초기화 된다.  
할당단계 : undefined로 초기화 된 변수에 값을 할당한다.  

var 키워드로 변수를 만들 경우, 선언단계와 초기화 단계가 동시에 이뤄진다.   
let 키워드는 선언단계와 초기화 단계가 분리되어 진행된다.  

let 키워드로 선언된 변수는 hoisting 되어 선언단계가 이뤄지지만 초기화 단계는 실제 let이 사용된 코드에 도착했을 때 이뤄진다.   
초기화 단계 이전에 변수에 접근하려하면 reference 에러가 발생한다.  

출처: https://medium.com/sjk5766/var-let-const-%ED%8A%B9%EC%A7%95-%EB%B0%8F-scope-335a078cec04



* 칼빈 293도일 때 섭씨와 화씨를 구해보자

```javascript
const kelvin = 293; //변하지 않는 상수
let celsius = kelvin - 273;
let fahrenheit = celsius * (9/5) + 32;
t = Math.floor(fahrenheit);
console.log('The temperature is '+t+' degrees fahrenheit.');
```


