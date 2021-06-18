---
layout: post
category: python
tag: [기초, 내용 추가하기, 질문, TIL, codecademy]
title: 코데카데미 파이썬 기초과정 요약 - 상속과 다형성
---

## 상속과 다형성  

<div class="message">
클래스라는 것이 코드를 재사용할 수 있도록 디자인되었지만, 이미 있는 클래스와 비슷한 클래스를 더 만들고 싶다면 어떨까? <br>
클래스 안의 원래 있는 요소들을 사용하면서 특정 부분만 다르게 사용하고 싶다면 원래 클래스를 상속하면 된다. 리믹스같은 개념이라고 생각하면 좋다. 원래 노래하고 아주 비슷하지만 뭔가 다르다.- 코데카데미
</div>

## 상속 (Inheritance)

```python
class User:
  is_admin = False
  def __init__(self, username)
    self.username = username
 
class Admin(User): #자식(부모)
  is_admin = True
```

유저 클래스를 상속해서 하위클래스 어드민을 만들었다. 새 어드민 클래스는 유저 클래스의 모든 생성자를 가지면서 is_admin이라는 것을 새로이 가지고 있다.   
종종 상속하는 클래스를 부모라고 하고 하위 클래스를 자식이라고 한다.

## 다형성 (Polymorphism)

<div class="message">
다형성이란 같은 구문이 데이터 타입에 따라 다른 행동을 하는 것을 말한다.
</div>

우리가 흔히 더하기라고 알고있는 + 는 파이썬에서 자료형별로 다른 역할을 한다.  
예를 들어 int + int 를 하면 int가 나오고 list + list를 하면 해당 list들을 합친 리스트가 나온다.   
여기서는 +를 예로 들었지만 어떤 매쏘드도 이렇게 동작할 수 있다.

```python
# 숫자형과 숫자형을 더하면, + 더하기 부호는 숫자형을 반환한다
2 + 4 == 6
 
# float형과 float형을 더하면 +는 float형을 반환한다
3.1 + 2.1 == 5.2
 
# 문자형과 문자형을 더하면, +는 문자형을 반환한다
"Is this " + "addition?" == "Is this addition?"
 
# 리스트형과 리스트형을 더하면, +는 리스트형을 반환한다
[1, 2] + [3, 4] == [1, 2, 3, 4]
```
## 예외처리 (Exception)

재고 없음 Exception을 만들어서 적용해보자

```python
class OutOfStock(Exception): 
#Exception을 상속받아 재고없음 클래스를 만든다
  pass #그냥 들여쓰기 에러를 피하기 위해서 적어놓은 것

class CandleShop: #양초가게
  name = "Here's a Hot Tip: Buy Drip Candles" #가게이름
  def __init__(self, stock): #클래스에 재고 속성을 추가
    self.stock = stock
    
  def buy(self, color): #색깔 속성을 가진 구매 매쏘드를 만든다
    if self.stock[color] < 1: #해당 색상의 재고가 1개 미만이면
      raise OutOfStock #재고없음 클래스호출
    self.stock[color] = self.stock[color] - 1 
    #아니면 해당 색상의 재고 1개 빼기

candle_shop = CandleShop({'blue':6,'red':2,'green':0})
candle_shop.buy('blue')

#재고없음이 출력되야한다!
candle_shop.buy('green')
```

## Overriding Methods 

유저 클래스에서 쓰이는 edit_message매쏘드를 새 하위클래스 어드민에서 오버라이드해보자.

```python
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username: 
    #메세지 전송하는 사람이 해당 유저와 유저네임이 같다면
      message.text = new_text
      #메세지의 텍스트를 new_text에 넣는다
      
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text
    # 유저권한 확인 없이 메세지의 텍스트를 new_text에 넣는다
```
## Super()

오버라이딩도 좋지만 존재하는 매쏘드에 로직을 추가하고 싶을 때, <strong>부모 클래스를 통해서 매쏘드를 호출</strong> 해야하는데 그럴 때 super()가 쓰인다.

감자샐러드 클래스를 상속받아서 건포도를 추가한 스페셜감자샐러드를 만들어보자

```python
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self,potatoes, celery, onions):
    super().__init__(potatoes, celery, onions) 
    self.raisins = 40
```

## 인터페이스 (Interface)  

<div class="message">
다른 클래스에서 온 다른 객체가 같은 동작을 수행하면 같은 인터페이스를 implement했다고 본다. 
</div>

두 개의 클래스가 같은 이름의 속성들과 매쏘드들을 가지고있을 때 우리는 이 클래스들이 같은 인터페이스를 implement했다고 한다. 파이썬에서 인터페이스는 대게 클래스가 취하는 매쏘드와 인자가 무엇인지를 가리킨다.  
다른 프로그래밍언어는 인터페이스가 무엇인가에 대해서 좀 더 정해진 정의를 가지고 있다. 하지만 대게는 다른 클래스에서 온 다른 객체가 같은 동작을 수행하는걸 의미한다. (비록 각 클래스마다 다르게 implement되었어도)  

When two classes have the same method names and attributes, we say they implement the same interface. An interface in Python usually refers to the names of the methods and the arguments they take. Other programming languages have more rigid definitions of what an interface is, but it usually hinges on the fact that different objects from different classes can perform the same operation (even if it is implemented differently for each class).  

```python
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005
```

## 주요 포인트 및 생각해볼 점

super를 사용하면서 쓰임에 대해서 다시 알아봐야겠다.
## 질문

Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.?  
다형성은 많은 것을 커버하는 추상적인 개념이지만 모두 같은 인터페이스를 implement한 클래스들로써 위계구조를 정의하는 것이 다형성을 우리의 코드에 소개하는 방법일까?
이게 무슨 뜻일까?
