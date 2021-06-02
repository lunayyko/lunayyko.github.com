---
layout: post
title: 코데카데미 파이썬 기초과정 요약 - 딕셔너리 05.31 TIL
---

# Dictionaries

<div class="message">
파이썬에서 딕셔너리(dictionary)란 사전형 데이터를 의미하며, key와 value를 1대1로 대응시킨 형태이다. 이때 하나의 key에는 하나의 value만이 대응된다.
</div>

``` python
dict = {"a":1,"b":2,"c":3}
for element in dict:
    # 밸류를 프린트하려면 dict 대신 dict.value()를 사용한다
    print(element)
#결과 : 딕셔너리의 키를 프린트한다
"a"
"b"
"c"
```

* 두 리스트를 합쳐서 딕셔너리를 만들어보자 - zip의 사용

``` python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    # for 만드는 딕셔너리 이름 in zip(요소1, 요소2)
    print(pair)
#결과
(1, 'A')
(2, 'B')
(3, 'C')
```

<i class="fa fa-info-circle" aria-hidden="true"></i> 주의:* 리스트는 변형가능하기 때문에 키값이 될 수 없다. 

예를 들어서 
```python
{["apple","orange"] : "fruit"} -> X
{2: ["apple", "orange"]} -> O
```

* 응용 : old_dict의 키 a의 value를 new_dict의 키b의 value로 집어넣을 때
```python
new_dict["new key"] = old_dict.pop("old key")
```

* 직업군별 여성 비율이라는 딕셔너리의 키와 밸류를 이용해서 문장을 출력해보자

```python
pct_w_in_occupation = {"CEO":28, "Engineer":9, "Physician":40, "Lawyer":37}
for occupation.percentage in ptc_w_in_occupation.items():
    print("Women make up" + str(percentage)+"percentage of"+occupation+"s")
#결과
Women make up 28 percentage of CEOs
Women make up 9 percentage of Engineers
Women make up 40 percentage of Physicians
Women make up 37 percentage of Lawyers
```

## Scrabble 단어게임

스크래블은 영어 알파벳 블럭을 이용해서 단어를 만들어서 알파벳 블럭마다 주어진 점수를 얻는 게임이다.

<img src="scrabble.jpeg">

```python
letters=["A","B","C"..."y","Z"]
points = [1,3,6,... 5,10]
#A는1점, B는 3점...
letters_to_point = {
    key:value
    for key, value
    in zip(letters,points)
}
#두 리스트를 합쳐서 딕셔너리를 만들었다
letter_to_points[" "]=0
#알파벳 없이 비어있는 공간은 0점 처리한다. 
def score_word(word):
    #점수를 계산하는 함수
    print_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter,0)
        #키 letter의 밸류를 point_total에 더하고, 해당 키 letter 가 없으면 기본값 0을 더한다.
    return point_total
```

# 응용 : to set key:value pair in a dict

어떤 딕셔너리의 키와 새로운 리스트의 밸류를 매칭시킨다.

```python
my_dict[key_to_add] = value_to_add
#새로 만드는 딕셔너리[키] = 밸류
```
예를 들어 설명하자면, 
```python
list = {'player1':["BLUE","TENNIS"], 'player2':["WHITE","GAME"]}
point = {}

for player,words in list.item():
    player_points = 0
    for word in words:
        player_points += score_word(word)

points[player] = player_points

print(points)
#결과
{'player1':29, 'player2':32 ... }
```

* 플레이어별 새 단어 추가하기

```python
def add_word(player, word):
    list[player].append(word)

play_word('player1', "CODE")
```