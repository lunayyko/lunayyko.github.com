---
layout: post
category: javascript
tag: [기초, 나중에 살펴보기, 질문]
title: 코데카데미 자바스크립트 기초과정 요약 - 변수 06.04 TIL
---

# var, let, const

<div class="message">
var는 변수, let은 변수, const(상수)는 재선언할 수 없는 변수이다.<br> 
let과 const는 블록{} 범위이며 var는 함수 범위이다.  
</div>

어떤 상황에서 어떤 것을 사용하는게 좋을지는 아직 잘 모르겠다.   
설명을 읽던 중 호이스팅과 초기화 관련해서 궁금한 점이 생겨서 자세히 알아보았다.   

**변수의 3단계 생성과정**

변수는 아래와 같이 3단계의 과정을 통해 생성된다.  
1. 선언단계 : 변수를 실행컨텍스트의 변수객체에 등록한다.  
2. 초기화 단계 : 실행 컨텍스트에 등록 된 변수객체에 대한 메모리를 할당한다. 이 단계에서 변수는 undefined로 초기화 된다.  
3. 할당단계 : undefined로 초기화 된 변수에 값을 할당한다.  
  
var 키워드로 변수를 만들 경우, 선언단계와 초기화 단계가 동시에 이뤄진다.   
let 키워드는 선언단계와 초기화 단계가 분리되어 진행된다.  
  
let 키워드로 선언된 변수는 hoisting 되어 선언단계가 이뤄지지만  
초기화 단계는 <strong>실제 let이 사용된 코드에 도착했을 때 이뤄진다.</strong>   
초기화 단계 이전에 변수에 접근하려하면 reference 에러가 발생한다.

출처 - [var, let, const 특징 및 호이스팅](https://medium.com/sjk5766/var-let-const-%ED%8A%B9%EC%A7%95-%EB%B0%8F-scope-335a078cec04)

아직은 정확히 어떤 차이인지 잘 모르겠다. 코드를 쓰면서 알아나가지 않을까 생각한다.

참고 - [let, const와 블록 레벨 스코프](https://poiemaweb.com/es6-block-scope)


* 연습문제 : 칼빈 293도일 때 섭씨와 화씨를 구해보자

```javascript
const kelvin = 293; //변하지 않는 상수
let celsius = kelvin - 273;
let fahrenheit = celsius * (9/5) + 32;
t = Math.floor(fahrenheit);
console.log('The temperature is '+t+' degrees fahrenheit.');
```


