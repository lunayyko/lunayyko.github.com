---
layout: post
category: python
tag: [기초, TIL]
title: 파이썬 - 진수 변환 함수
---

진수를 변환하는 함수를 만드는게 코딩테스트에서 나와서 인터넷에 나와있는 진수변환함수들을 살펴보았다.

# 1번

```python

class Transformer(object):
    decimal_digits = "0123456789"
    #10진수로 변환할 경우 숫자들의 리스트 
    def __init__(self, digits):
        self.digits = digits

    #10진수에서 i진수로 변환할 때(i값을 받고 i, 숫자리스트, 변환하려는 숫자를 반환한다.)
    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)
    
    #s진수에서 10진수로 변환할 때(s값을 받고 s, 변환하려는 숫자, 숫자리스트를 반환한다.)
    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))
```