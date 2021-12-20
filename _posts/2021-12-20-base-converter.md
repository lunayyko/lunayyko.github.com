---
layout: post
category: python
tag: [기초, TIL]
title: 파이썬 - 진수 변환 함수
---

진수를 변환하는 함수를 만들어보자


# 1번

```python
class Transformer(object):
    decimal_digits = '0123456789'
    #10진수로 변환할 경우 숫자들의 리스트 
    def __init__(self, digits):
        self.digits = digits

    #10진수에서 i진수로 변환할 때(i값을 받고 i, 숫자리스트, 변환하려는 숫자를 반환한다.)
    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)
    
    #s진수에서 10진수로 변환할 때(s값을 받고 s, 변환하려는 숫자, 숫자리스트를 반환한다.)
    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))
    
    def _convert(self, number, fromdigits, todigits):
        # 입력받은 숫자, 바꾸기 전의 진수, 바꾼 뒤의 진수값을 받는다.
        fromdigits_len, todigits_len = len(fromdigits), len(todigits)
        # 진수의 길이를 저장한다???
        number = str(number)
        number_len = len(number)
        # 입력받은 숫자의 길이도 저장한다

        tmp_dec=0
        # 숫자의 갯수만큼 지수를 곱해서 더하여 십진수로 변환한 값을 저장한다. 
        # 예: 100(2진수)이면 (2의2승 * 1) + (2의1승 * 0) + (2의0승 * 0)
        for idx, n in enumerate(number):
            tmp = fromdigits_len ** (number_len-idx-1) * fromdigits.index(n)
            tmp_dec += tmp
        
        result=''
        while tmp_dec > 0:
            # 몫과 나머지를 구하는 파이썬의 내장함수 divmod사용
            tmp_dec, mod = divmod(tmp_dec, todigits_len)
            result += str(todigits[mod])
        return result[::-1]
```

# 2번

```python
from math import log

def convertFromBase10(num, base):
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    power = int(log(num, base))
    converted = ""
    for pow in range(power, -1, -1):
        converted += numToChar[num // (base**pow)]
        num %= base**pow
    return converted

print(convertFromBase10(429,7))
```

