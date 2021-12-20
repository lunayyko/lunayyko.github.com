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
        # 입력받은 숫자, 바꾸기 전의 진수, 바꾼 뒤의 진수값을 받는다. 예(555,BASE10,BASE2)
        fromdigits_len, todigits_len = len(fromdigits), len(todigits)
        # 해당 진수의 숫자리스트의 길이를 저장한다. 예(BASE10은 10진수, '0123456789' 이므로 10개)
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
            # 나온 숫자를 반대로 정렬 
        return result[::-1]
```

# 2번

```python
from math import log

    #10진수에서 원하는 진수로 바꾸기(바꿀 숫자, 바꿀 숫자의 진수)
def convertFromBase10(num, base):
    #변경할 숫자의 리스트
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    #가장 큰 지수를 power에 저장 
    power = int(log(num, base))
    converted = ""
    #power숫자부터 0까지 거꾸로 돌리기
    for pow in range(power, -1, -1):
        # 진수의 가장 큰 지수(예 7의3승)로 주어진 숫자를 나누어서 몫을 converted에 더하고  
        converted += numToChar[num // (base**pow)]
        # 나머지를 다시 숫자의 자리에 넣음
        num %= base**pow
    return converted

print(convertFromBase10(429,7))
#1152
```

# 3번

출처 : https://code.activestate.com/recipes/111286/

```python
BASE2 = "01"
BASE10 = "0123456789"
BASE16 = "0123456789ABCDEF"
BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

def baseconvert(number,fromdigits,todigits):
    """ converts a "number" between two bases of arbitrary digits

    The input number is assumed to be a string of digits from the
    fromdigits string (which is in order of smallest to largest
    digit). The return value is a string of elements from todigits
    (ordered in the same way). The input and output bases are
    determined from the lengths of the digit strings. Negative 
    signs are passed through.

    decimal to binary
    >>> baseconvert(555,BASE10,BASE2)
    '1000101011'

    binary to decimal
    >>> baseconvert('1000101011',BASE2,BASE10)
    '555'

    integer interpreted as binary and converted to decimal (!)
    >>> baseconvert(1000101011,BASE2,BASE10)
    '555'

    base10 to base4
    >>> baseconvert(99,BASE10,"0123")
    '1203'

    base4 to base5 (with alphabetic digits)
    >>> baseconvert(1203,"0123","abcde")
    'dee'

    base5, alpha digits back to base 10
    >>> baseconvert('dee',"abcde",BASE10)
    '99'

    decimal to a base that uses A-Z0-9a-z for its digits
    >>> baseconvert(257938572394L,BASE10,BASE62)
    'E78Lxik'

    ..convert back
    >>> baseconvert('E78Lxik',BASE62,BASE10)
    '257938572394'

    binary to a base with words for digits (the function cannot convert this back)
    >>> baseconvert('1101',BASE2,('Zero','One'))
    'OneOneZeroOne'

    """
    # make an integer out of the number
    x=long(0)
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)
       
    
    # create the result in base 'len(todigits)'
    res=""
    while x>0:
        digit = x % len(todigits)
        res = todigits[digit] + res
        x /= len(todigits)
    return res
```
