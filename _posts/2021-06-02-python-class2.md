---
layout: post
category: python
tag: [입문, 나중에 살펴보기, TIL, codecademy]
title: 코데카데미 파이썬 기초과정 요약 - 클래스2
---

* 원의 넓이 구하는 클래스 만들기

  ```python
  class Circle:
    pi = 3.14
    def __init__(self, diameter):
      print("Creating circle with diameter {d}".format(d=diameter))
      self.radius = diameter/2
    def circumference(self):
      return 2 * self.pi * self.radius

  medium_pizza = Circle(12)
  teaching_table = Circle(36)
  round_room = Circle(11460)

  print(Circle.circumference(medium_pizza))
  print(Circle.circumference(teaching_table))
  print(Circle.circumference(round_room))
  ```

* 학생의 이름, 학년, 점수를 속성으로 가지는 클래스 만들기
  
  type()함수는 객체를 받아서 해당 객채가 속한 클래스를 반환한다.  

  ```python
  class Student:
    def __init__(self, name, year): 
    #self, name, year가 Student 클래스의 타입이 된다
      self.name = name
      self.year = year
      self.grades = []

    def add_grade(self, grade):
      if type(grade) is Grade: 
      #add_grade 매쏘드에서 입력된 grade가 Grade 클래스의 타입인지 확인한다
        self.grades.append(grade)

  class Grade:
    minimum_passing = 65
    def __init__(self,score):
      self.score = score

  roger = Student("Roger van der Weyden", 10)
  sandro = Student("Sandro Botticelli", 12)
  pieter = Student("Pieter Bruegel the Elder",8)
  pieter.add_grade(Grade(100))
  #100점의 새 Grade를 만들고 .add_grade()매쏘드를 이용해서 피터의 .grades에 추가한다.
  ```