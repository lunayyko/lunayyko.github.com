---
layout: post
category: HTML/CSS
tag: [기초, 위코드, TIL]
title: HTML/CSS - Semantic Web 과 Semantic Tag
---

## 시맨틱 요소란 무엇인가

시맨틱 요소는 브라우저와 개발자에게 둘 다 에게 분명한 의미를 전달하는 요소이다.  
시맨틱이 아닌 요소에는 예를 들어 <div> 와 <span> 이 있다. 이 요소들은 안에 어떤 내용이 들어있는지에 대한 정보를 전혀 전달하지 않는다.  

시맨틱 요소의 예로는 <form>, <table>, <article> 등이 있는데 이름을 보면 안에 내용이 어떤 것일지 분명하게 알 수 있다.  

## HTML에서의 시맨틱 태그들

부분 별로 어떤 내용인지 설명하기위한 시맨틱 요소들은 아래와 같은 것들이 있다.

![기본 시맨틱 태그](/public/img/img_sem_elements.gif)

이외에도 이런 것들이 있다.  

article : 독립적이고 안에 개별적인 내용을 포함한 부분  
aside : 페이지 컨텐츠 옆에 들어가는 부분  
details: 사용자가 보거나 숨길 수 있는 부가적인 세세한 내용  	
figcaption : figure 요소의 캡션
figure : 일러스트, 도표, 사진, 코드 등의 개별적인 컨텐츠  
footer: 글이나 섹션의 미주 부분	
header : 글이나 섹션의 맨 위의 제목 부분  
main :	메인 컨텐츠  
nav: 네비게이션 링크   
section: 컨텐츠를 포함한 웹사이트의 한 부분  
summary: details 요소에서 보여지는 헤딩  
time: 날짜 혹은 시간  
[출처: w3school](https://www.w3schools.com/html/html5_semantic_elements.asp)
## 시맨틱 웹

시맨틱 웹이란 이런 식으로 컨텐츠에 무슨 내용이 포함되어있는지 자동으로 컴퓨터가 알게함으로서 정보를 더 잘 분류하고 보여질 수 있도록 하자는 아이디어이다.  

> 시맨틱 웹은 컴퓨터가 정보 자원의 뜻을 이해하고 논리적 추론까지 하는 차세대 지능형 웹이다. 지금의 웹은 특정 검색어를 치면 불필요한 문서가 모두 나와 일일이 찾아 보아야 하는데 지능형 웹은 다르다. 단어의 유사성과 상관관계 등을 파악해서 원하는 결과물만 찾아 보여준다.
[출처: 차세대 지능형 시맨틱 웹 & 온톨로지](https://www.itfind.or.kr/WZIN/jugidong/1265/126503.htm#:~:text=%EC%8B%9C%EB%A7%A8%ED%8B%B1%20%EC%9B%B9%EC%9D%80%20%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B0%80,%EC%9B%90%ED%95%98%EB%8A%94%20%EA%B2%B0%EA%B3%BC%EB%AC%BC%EB%A7%8C%20%EC%B0%BE%EC%95%84%20%EB%B3%B4%EC%97%AC%EC%A4%80%EB%8B%A4.)

## 시맨틱 태그의 예시

예를 들어서 \<img> 태그를 사용하면 이 컨텐츠가 이미지라는 것을 컴퓨터가 알 수 있지만 css를 통해서 background-img: url로 이미지를 보여주게 되면 컴퓨터는 해당 요소에 이미지가 들어있는지 알 수 없다.