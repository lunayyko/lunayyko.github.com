---
layout: post
category: python
tag: [입문, 내용 추가하기]
title: 코데카데미 파이썬 기초과정 요약 - 코딩챌린지 06.04 TIL
---

- 사용된 알파벳 갯수를 출력하는 함수를 만들어보자

힌트 : 주어진 영어알파벳 리스트를 흝어서 해당 알파벳이 입력된 단어 안에 있는지 보세요

```python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count

print(unique_english_letters("mississippi"))
# 4
print(unique_english_letters("Apple"))
# 4
```

<br>
이건 답을 보고나서 좀 헷갈렸는데 알파벳 리스트를 사용한 덕분에 중복을 체크할 필요가 없다는 것을 알았다. letters리스트를 쭉 흝으면서 a 가 있나? +0 b가 있나? +0 ... s가 있나? +1 t가 있나? +0 이렇게 가기 때문에 word에 같은 알파벳이 중복되서 들어있는걸 판별하는 부분을 안 써도 된다.
<br><br>

* 주요 포인트 및 생각해볼 점 
  <del>코드블럭안의 코드를 wrap해서 넘길 수 있는 방법이 없을까?</del> -> 코드를 줄바꿈하자
  글 오른쪽 여백에 해당 글의 구성목록을 보여줄 수 없을까?
