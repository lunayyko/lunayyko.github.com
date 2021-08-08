---
layout: post
category: django
tag: [위코드, TIL, 프로젝트]
title: CSV 업로더
---

## CSV파일 업로더

DB를 손으로 한땀한땀 넣을 수 없어서 위코드에서 제공하는 예리님의 튜토리얼을 보고 디비업로더 파일을 만들었다. 

```python
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tangoplate.settings")
django.setup()

from restaurants.models import Restaurant, Menu
from reviews.models import Review

CSV_PATH_LOCATION = 'review_images.csv'

def insert_restaurants():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            Restaurant.objects.create(
                name = row[1], 
                address = row[2], 
                phone_number=row[3], 
                category_id = int(row[4]), 
                location_id = int(row[5]), 
                serving_price_id = int(row[6])
            )

def insert_menus():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            Menu.objects.create(
                item=row[0], 
                item_price=row[1],
                restaurant_id=row[2]
            )

def insert_review():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            Review.objects.create(
                description=row[0], 
                created_at=row[1],
                updated_at=row[2],
                restaurant_id=row[3],
                user_id=row[4],
            )

def insert_review_img():
    with open(CSV_PATH_LOCATION) as in_file:
        data_reader = csv.reader(in_file)
        for row in data_reader:
            Review.objects.create(
                image=row[0], 
                review_id=row[1],
            )

insert_review_img()

```

이렇게 하면 csv파일이 디비에 잘 올라간 것을 볼 수 있다. 
이와 함께 sql workbench를 함께 사용하면 디비를 좀 더 보기쉽게 관리할 수 있다.

![csv](/public/img/csv.png)
![db](/public/img/db.png)