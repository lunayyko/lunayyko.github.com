---
layout: post
category: python
tag: [입문, 나중에 살펴보기, 주석 추가하기, TIL]
title: 코데카데미 파이썬 기초과정 요약 - 클래스3 음식점메뉴 TIL
---

클래스 과정의 마지막 리뷰이다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Dk-ePlxdmBU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

영어이지만 이 비디오를 보면 문제와 코드를 쓰는 과정을 알 수 있다.

```python
class Menu: #메뉴셋트의 이름, 메뉴 아이템들, 가능시작시간, 제공종료시간
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self): #클래스의 대표가되는 스트링을 반환하는 매직 매쏘드
    return self.name + ' menu availble from ' + str(self.start_time) + '-' + str(self.end_time)
    # 예를 들어 brunch_menu 는 11시부터 16시까지 가능합니다 문자열 반환

  def calculate_bill(self, purchased_items): #음식값 계산
    bill = 0
    for purchased_item in purchased_items: #구매한 아이템들을 쭉 흝으면서
      if purchased_item in self.items: #구매한 아이템이 메뉴 아이템들 중에 있다면?
        bill += self.items[purchased_item] #구매한 아이템의 밸류(가격)를 빌에 추가한다
    return bill

# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100,1600)
#브런치_메뉴는 브런치라는 이름이고 브런치_아이템즈 리스트를 가지고 11시부터 16시까지이다.
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#13.5
#브런치_메뉴에서 calculate_bill매쏘드를 써서 (['주문한 메뉴'])의 값을 출력한다.
#왜떔시 변수 이름들을 헷갈리게 만들어놓고는 두 뎁쓰로 나눠서 표현해야했을까?

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500,1800)
print(early_bird_menu.calculate_bill(['mushroom ravioli (vegan)', 'salumeria plate']))
#21.5

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

#장사가 잘되서 프랜차이즈를 내기로 했다
#설명하는 사람의 말로는 이렇게 상위 클래스를 만들게 되는 것이 이번 연습의 중점이라고 한다

class Franchise:
  def __init__(self, address, menu):
    self.address = address
    self.menus = menus
  def __repr__(self): #프랜차이즈 클래스는 대표 문자열로 주소를 반환한다
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time #입력받은 시간이 메뉴의 시작시간의 이후이거나 종료시간 이전일 떄
        #TMI : 이 부분 오류가 났는데 선생님 코드하고 비교해보니까 똑같이 생겼다
        available_menus.append(menu) #메뉴를 가능한 메뉴들 리스트에 넣는다
    return available_menus

menus = [brunch_items, early_bird_items, dinner, kids]
#새 변수 = 클래스(변수가 가지게 할 값) 이 순서는 항상 헷갈려서 세번쯤 틀렸다
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
#1232 West End Road

flagship_store.available_menus(1200)

#프랜차이즈가 잘 되서 비즈니스로 확장하기로 했다고 한다.

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a Arepa", arepas_items, 1000, 2000)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
arepa = Business("Take a' Arepa", [arepas_place])
print(arepa.menus[0])

```
