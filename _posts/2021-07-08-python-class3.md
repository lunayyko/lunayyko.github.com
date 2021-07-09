---
layout: post
category: python
tag: [기초, TIL]
title: 파이썬 - 클래스 Class
---

## Database 라는 이름의 class를 구현해 주세요.

Database 클래스 내부에 다음의 속성(attribute)들을 선언해주세요.  

name : database의 이름  
size : 저장할 수 있는 데이터의 max 사이즈. Size를 넘어서는 데이터를 저장할 수 없다.  
Database 클래스 내부에 다음의 메소드들을 구현해주세요.  

insert, select, update, delete  
각 메소드들에 대한 설명은 아래와 같습니다.  

### Insert  
insert 메소드는 self 외에 2개의 parameter를 받습니다.  

field와 value 입니다.  

Field 는 저장하고자 하는 데이터의 필드명이고 value는 값입니다.  

Field 와 value는 내부적으로 dictionary에 저장되어야 합니다.  

insert 메소드는 다음 처럼 호출 할 수 있습니다.  

객체 이름이 db 라는 가정하에 db.insert("name", "정우성")  
insert 메소드는 특별한 return 값은 없습니다.  

단, 만일 내부 dictionary의 총 사이즈가 Database 클래스의 size 속성보다 크면 더이상 새로운 값들을 저장하지 말아야 합니다.  

### Select
select 메소드는 self 외에 1개의 parameter를 받습니다.  

바로 field 입니다.  

field 는 읽고자 하는 데이터의 필드명 입니다.  

내부적으로 데이터를 저장하고 있는 dictionary에서 해당 field에 해당하는 키와 연결되어 있는 값을 return 해주어야 합니다.  

예를 들어, 이미 name이라는 필드명으로 "정우성" 이라는 값을 저장했다고 한다면:  

객체 이름이 db 라는 가정하에
db.select("name")
> "정우성"
이 되어야 합니다.

만일 해당 필드값으로 저정되어 있는 값이 없다면 None 을 return 해주세요.

### Update
self 외에 2개의 parameter를 받습니다.

field와 value 입니다.

이름 그대로 이미 저장되어 있는 값을 수정하는 메소드 입니다.

객체 이름이 db 라는 가정하에
db.update("name", "아이유")

만일 field값에 해당하는 데이터가 저장되어 있지 않으면 아무것도 하지 않습니다.

그리고 특별한 return 값은 없습니다.

### Delete
delete 메소드는 self 외에 1개의 parameter를 받습니다.

field 입니다.

field 는 지우고자 하는 데이터의 필드명 입니다.

객체 이름이 db 라는 가정하에  
db.delete("name")  
만일 field값에 해당하는 데이터가 저장되어 있지 않으면 아무것도 하지 않습니다.  

그리고 특별한 return 값은 없습니다.  

```python
class Database:
  def __init__(self, name, size):
    self.name = name
    self.size = size
    self.db = {} #?
  
  def insert(self, field, value):
    if len(self.db) < self.size:
      self.db[field] = value

  def select(self, field):
    if field in self.db:
      return self.db[field]
    else:
      return None

  def update(self, field, value):
    if field in self.db:
      self.db[field] = value

  def delete(self, field):
    if field in self.db:
      del self.db[field]
```
