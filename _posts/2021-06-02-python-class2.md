---
layout: post
category: python
tag: [입문, 나중에 살펴보기, 질문]
title: 코데카데미 파이썬 기초과정 요약 - 클래스2 06.02 TIL
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

  7.add_grade method should verify that <u>grade is of type Grade</u> and if so, add it to the Student‘s .grades.      
  이게 무슨 뜻일까? 시간이 지나고 다시 살펴봐야할 것 같다.  
  type()함수는 객체를 받아서 해당 객채가 속한 클래스를 반환한다.  

  ```python
  class Student:
    def __init__(self, name, year): # 셀프, 네임, 이어가 학생 클래스의 타입인가?
      self.name = name
      self.year = year
      self.grades = []

    def add_grade(self, grade):
      if type(grade) is Grade: #입력된 점수가 그레이드 클래스?의 타입인가? 확인한다는 뜻인가? 
        self.grades.append(grade)

  class Grade:
    minimum_passing = 65
    def __init__(self,score):
      self.score = score

  roger = Student("Roger van der Weyden", 10)
  sandro = Student("Sandro Botticelli", 12)
  pieter = Student("Pieter Bruegel the Elder",8)
  pieter.add_grade(Grade(100))
  #8.Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade()
  ```

뒤로 갈수록 점점 미궁으로 빠져들어간다