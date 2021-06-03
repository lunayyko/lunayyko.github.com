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