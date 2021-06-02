---
layout: post
title: 코데카데미 파이썬 기초과정 요약 - 딕셔너리 05.31 TIL
---

# Dictionaries

* zip

``` python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)
#결과
(1, 'A')
(2, 'B')
(3, 'C')
```

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

<i class="fa fa-info-circle" aria-hidden="true"></i> 주의:* 리스트는 변형가능하기 때문에 키값이 될 수 없다. 
예를 들어서 
```python
{["apple","orange"] : "fruit"} -> X
{2: ["apple", "orange"]} -> O
```

* 딕셔너리 1에서 키 a의 value를 딕셔너리2의 키b의 value로 집어넣을 때
```python
new_dict["new key"] = old_dict.pop("old key")
```

* Get all items
```python
pct_w_in_occupation = {"CEO":28, "Engineer":9, "Physician":40, "Lawyer":37}
for occupation.percentage in ptc_w_in_occupation.items():
    print("Women make up" + str(percentage)+"percentage of"+occupation+"s")
```

## Scrabble(Dictionary 복습)
```python
letters=["A","B","C"..."y","Z"]
points = [1,3,6,... 5,10]

letters_to_point = {
    key:value
    for key, value
    in zip(letters,points)
}
letter_to_points[" "]=0

def score_word(word):
    print_total=0
    for letter in word:
        point_total += letters_to_points.get(letter,0)
    return point_total
```

## to set key:value pair in a dict
```python
my_dict[key_to_add] = value_to_add
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