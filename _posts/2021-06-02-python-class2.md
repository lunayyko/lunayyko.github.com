---
layout: post
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

7.
Add an .add_grade() method to Student that takes a parameter, grade.  

.add_grade() should verify that <u>grade is of type Grade</u> and if so, add it to the Student‘s .grades.  

이게 무슨 뜻일까?!

```python
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder",8)
```
