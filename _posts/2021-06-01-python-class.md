---
layout: post
title: 코데카데미 파이썬 기초과정 요약 - 클래스 06.01 TIL
---

클래스를 살펴보기에 앞서 클래스 안의 함수를 지칭하는 매쏘드를 살펴보자.

## Method

<div class="message">
클래스 안에 들어있는 함수를 매쏘드라고 부른다. 
그래서 클래스로 만든 객체에서만 호출할 수 있다. 
첫번째 파라미터로서 self를 가지고 항상 한 개 이상의 파라미터를 가진다.
</div>

```python
class Orange:
    def __init__(self):
        #init 은 initiate(시작하다)를 뜻한다
        print("Orange Created!")
```
이렇게 두 개의 __ 언더스코어로 둘러쌓인 매쏘드는 매직매쏘드라고 불리고 객체를 생성하는 것같은 특별한 목적을 위해서 파이썬에서 사용된다.

## Class

> The object-oriented programming paradigm also addresses the problems that arise in procedural programming by eliminating global state, but instead of storing state in functions, it is stored in objects. In object-oriented programming, classes define a set of objects that can interact with each other. - 'the self-taught programmer' by cory althoff

<div class="message">
쉽게 말하면, 클래스는 다른 것들과 상호작용할 수 있는 객체들의 모음이다. 클래스는 데이터타입의 템플릿이다. 클래스라는 것을 나타내기 위해서 첫 글자는 대문자를 사용하는 것이 관례이고 instantiated(클래스를 객체로 만드는 과정) 되어야한다. 
</div>

예를 들어서 오렌지가 객채라면 오렌지 한 묶음은 클래스이다. 
오렌지를 만드는 클래스가 있다면 작고 밝은 오렌지 객체, 크고 어두운 오렌지 객체 등을 만들 수 있다.

```python
class Orange:
    def __init__(self, w, c):
        #init이라는 특별 매쏘드는 두 개의 인스탄스변수 weight와 color를 만든다.
        self.weight = w
        self.color = c
        print("Created!")
```

이렇게 새 객체를 만드는 것을 클래스를 instantiate 한다고 한다.

**궁금한 부분**

initialize(초기화)와 instantiate(인스턴스화)의 정확한 뜻이 뭘까? 코데카데미에서 아래 설명을 읽고 있었는데 맨 마지막 줄이 이해가 잘 가지 않았다.

The first dunder method we’re going to use is the __init__() method (note the two underscores before and after the word “init”). This method is used to initialize a newly created object. <u>It is called every time the class is instantiated.</u> 

* initialize(초기화) : 확보된 메모리 영역을 어떤 값으로 채우거나 쓰레기 값을 일정한 값으로 바꾸는 것

파이썬에서 init매소드는 생성자와 같은 역할을 하는데 “생성”이란 __new__ 메소드로 만든(Instantiate) 인스턴스를 사용자가 원하는 대로 사용하도록 커스토마이징(Customizing/Initiating)함을 말합니다. 예를 들어 self.x=x, self.y=y 와 같이 클래스 인스턴스에 프로퍼티(Property)를 부여하는 등 인스턴스 사용을 위한 초기 세팅을 주는 것이 바로 생성(Construct 또는 Initiate)인 것입니다.

* instantiate(인스턴스화) : 인스턴스화는 클래스 내의 객체에 대해 특정한 변형을 정의하고, 이름을 붙인 다음, 그것을 물리적인 어떤 장소에 위치시키는 등의 작업을 통해, 인스턴스를 만드는 것을 의미한다. - http://www.terms.co.kr/instance.htm
