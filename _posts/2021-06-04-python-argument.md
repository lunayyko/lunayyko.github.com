---
layout: post
category: python
tag: [기초, 내용 추가하기, 질문]
title: 코데카데미 파이썬 기초과정 요약 - 함수와 인자 06.04 TIL
---

# 매개변수와 인수 (Parameters and Arguments)
<br>
<div class="message">
매개변수(parameter)는 함수의 정의 안에 있는 변수를 말한다</div> 

<div class="message">
인수(argument)는 함수를 호출할 때 패스되는 값이다</div>  

<img src="../public/img/param-arg.png">  

입으로 들어가는건 매개변수 나오는(?)건 인수... 인.. 인변 인수..  

함수의 인수는 파이썬에서 꼭 필요로된다. 그래서 표준 함수 정의는 두 개의 매개변수를 정의하고 함수에 두 개의 인수를 패스한다.  

## 키워드 인수 (Keyword Arguments)

파이썬에서 함수를 호출할 때, 우리는 매개변수를 함수 정의할 때 썼던 순서 그대로 나열해야되는데 키워드 인수를 사용하면 그렇지 않아도 괜찮다. 

매개변수의 이름을 사용하는 특별한 신택스가 있는 함수에서 키워드 인수를 사용한다. 함수가 선택적인(optional, 안써도 되는?) 디폴트 인수를 많이 갖고 있을 때나 매개변수의 순서를 알기 어려울 때 유용한다.
다음 함수가 선택적인 디폴트 인수를 많이 가지고 있다.  

```python
# Define a function with a bunch of default arguments
def log_message(logging_style="shout", message="", font="Times", date=None):
  if logging_style == 'shout':
    # capitalize the message
    message = message.upper()
  print(message, date)
 
# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693")
```
이 코드에서 우리는 로그_메세지() 함수를 정의했고 이는 0에서 4개까지의 인수를 가질 수 있다.
4개의 인수가 어떤 순서로 정의될 지 확실하지 않기 때문에 우리는 함수를 호출하기 위해서 매개변수 이름을 쓸 수 있다. 우리가 함수를 호출하면서 이 신택스 message="Hello from the past" 를 사용한 점에 주의하자. 여기서 이 키워드 message는 우리가 인수를 패스하고자하는 매개변수의 이름이어야한다.    

한글로 써봐도 무슨 뜻인지 잘 알 수가 없다 ㅋㅋㅋㅋ  

```python
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character='m', line_breaks=False)
```

## Don't Use Mutable Default Arguments

디폴트 인수를 갖고 함수를 만들 때, 빈 리스트를 쓰고싶겠지만 그렇게하면 안 된다.
It might be helpful to note some of the objects in Python that are not mutable (and therefore OK to use as default arguments). int, float, and other numbers can’t be mutated (arithmetic operations will return a new number). tuples are a kind of immutable list. Strings are also immutable — operations that update a string will all return a completely new string.

* 빈 리스트 대신 None 을 보초로 사용하자

```python
def update_order(new_item, current_order=None): #current_order=[]대신 =None을 넣고
  if current_order is None: #None이라면
    current_order=[] #빈 리스트를 만들어주는 방법을 사용하자
  current_order.append(new_item)
  return current_order
```

# None

None is a special value in Python. It is unique (there can’t be two different Nones) and immutable (you can’t update None or assign new attributes to it).

None is falsy, meaning that it evaluates to False in an if statement, which is why the above code prints “Goodbye”. None is also unique, which means that you can test if something is None using the 'is' keyword.

```python
# first we define session_id as None
session_id = None
 
if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"
 
# we can assign something to session_id
if active_session:
  session_id = active_session.id
 
# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)
```

What does a function return when it doesn’t return anything? This sounds like a riddle, but there is a correct answer. A Python function that does not have any explicit return statement will return None after completing. 

```python
# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return
print(prints_return)
#결과 : None

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)
#결과 : None
```
default return 값이 none이라고 하는데 나는 여기서 무엇을 배워야하는건지 잘 모르겠다. 

**보완할 점**  

- 해석할 때 용어집을 만들어야할까?
