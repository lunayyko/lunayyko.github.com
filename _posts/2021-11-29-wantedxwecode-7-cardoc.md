---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제4 카닥()
---

# 과제 설명 요약
- 구현 기간 : 21.11.22(18시) ~ 21.11.28 (22시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-YY) 참고

# 과제 설명

### 1. 배경 및 공통 요구사항

<aside>
😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

[Copy of Code](https://www.notion.so/08e67c3cdc8e471fb1aab50e5963fb05)

---

### 2. 사용자 생성 API

🎁 **요구사항**

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

```jsx
/* Request Body 예제 */

 { "id": "candycandy", "password": "ASdfdsf3232@" }
```

---

### 3. 사용자가 소유한 타이어 정보를 저장하는 API

🎁 **요구사항**

- 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.

```jsx
/* Request Body 예제 */
[
  {
    "id": "candycandy",
    "trimId": 5000
  },
  {
    "id": "mylovewolkswagen",
    "trimId": 9000
  },
  {
    "id": "bmwwow",
    "trimId": 11000
  },
  {
    "id": "dreamcar",
    "trimId": 15000
  }
]
```

🔍 **상세구현 가이드**

- 자동차 정보 조회 API의 사용은 아래와 같이 5000, 9000부분에 trimId를 넘겨서 조회할 수 있다.
 **자동차 정보 조회 API 사용 예제 → 
📄** [https://dev.mycar.cardoc.co.kr/v1/trim/5000](https://dev.mycar.cardoc.co.kr/v1/trim/5000)
**📄** [https://dev.mycar.cardoc.co.kr/v1/trim/9000
📄](https://dev.mycar.cardoc.co.kr/v1/trim/9000) [https://dev.mycar.cardoc.co.kr/v1/trim/11000
📄](https://dev.mycar.cardoc.co.kr/v1/trim/11000) [https://dev.mycar.cardoc.co.kr/v1/trim/15000](https://dev.mycar.cardoc.co.kr/v1/trim/15000)
- 조회된 정보에서 타이어 정보는 spec → driving → frontTire/rearTire 에서 찾을 수 있다.
- 타이어 정보는 205/75R18의 포맷이 정상이다. 205는 타이어 폭을 의미하고 75R은 편평비, 그리고 마지막 18은 휠사이즈로써 {폭}/{편평비}R{18}과 같은 구조이다.
 위와 같은 형식의 데이터일 경우만 DB에 항목별로 나누어 서로다른 Column에 저장하도록 한다.

---

### 4. 사용자가 소유한 타이어 정보 조회 API

🎁 **요구사항**

- 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.

# 모델링

![모델링](/public/img/cardoc_erd.png)


# 사용한 기술 설명

이번 과제는 팀이 아닌 개인과제였어서 초기세팅부터 배포까지 혼자 진행하게되었다.  
저번 과제때 했던 drf를 이용한 회원가입/로그인에 태우님이 작성하셨던 simpleJWT를 사용해서 refresh token/ access token을 발급하도록 했다.

실력이 부쳐서 4개 중 2번과제까지만 진행할 수 있었다.  
함께 위워크에서 작업했던 현묵님의 도움을 받아서 해당 JSON을 디비에 업로드하였다.

위코드에서 제공하는 비디오 튜토리얼을 따라서 AWS EC2로 배포를 했는데 생각보다 어렵지 않았다.

# EC2 배포 명령어

```shell
cd coding/aws-pem
ssh -i wantedxcardoc.pem ubuntu@3.38.150.162  
#public ip주소

wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh

chmod +x Miniconda3-py37_4.10.3-Linux-x86_64.sh

./Miniconda3-py37_4.10.3-Linux-x86_64.sh

source .bashrc

#껏다 켜고, 가상환경 생성
conda create -n cardoc python=3.8
conda activate cardoc

sudo apt-get update
sudo apt-get upgrade

#gcc 설치, mysql 설치
sudo apt-get install gcc
sudo apt-get install libmysqlclient-dev

git clone 레포 주소
pip install -r requirements.txt
```

# API

![모델링](/public/img/cardoc_api.png)

# 데이터셋

카닥에서 제공한 데이터는 이런 식으로 생겼었다. 
![DB](/public/img/cardoc_db.png)

# 내가 작성한 코드 / 기억에 남는 코드

```python
#현묵님이 작성하신 디비 업로더 파일
import urllib.request
import json
import django
import os

from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardoc.settings')
django.setup()

from tires.models import Tire

def DataUploader():
    
    trimid = ["5000", "9000", "11000", "15000"]
    
    for i in trimid:
        url = "https://dev.mycar.cardoc.co.kr/v1/trim/" + i

        response    = urllib.request.urlopen(url)
        json_str    = response.read().decode("utf-8")
        json_object = json.loads(json_str)
        data        = json_object
        frontTire   = data['spec']['driving']['frontTire']['value']
        rearTire    = data['spec']['driving']['rearTire']['value']

        Tire.objects.create(
            trimid          = int(i),
            f_section_width = int(frontTire.split('/')[0]),
            f_aspect_ratio  = int(frontTire.split('/')[1].split('R')[0]),
            f_rim_diameter  = int(frontTire.split('/')[1].split('R')[1]),
            r_section_width = int(rearTire.split('/')[0]),
            r_aspect_ratio  = int(rearTire.split('/')[1].split('R')[0]),
            r_rim_diameter  = int(rearTire.split('/')[1].split('R')[1]),
        )

DataUploader()
```


# 프로젝트 후기

혼자 진행하면서 모르겠는 부분이 너무 많아서 팀원분들의 소중함을 느꼈고, 팀장님의 코드를 보고 작성해보려다가 내 실력보다 너무 어려운 코드를 소화하려고 하는 것은 사상누각을 짓는 일이구나 단계별로 차근차근 소화해서 코드가 한 줄 한 줄 어떤 역할을 하는지 정확히 알고 사용해야겠다고 생각했다. 과제 4개 중 2개밖에 하지 못해서 아쉬움이 남는다. 

온보딩 과정이 너무 어려워서 중간에 포기하고 싶은 마음도 있었고 한 달동안 많이 배우거나 팀에 기여하지 못한 것 같아서 안타까웠지만 이렇게 한 달이 흐른 뒤에 회고를 해보니 생각보다 많은 코드를 쳐봤고 배웠다는 생각이 든다. 회사에 한 달 일찍 입사하는 것보다 이 과정에 참여한 것이 좋은 결정이었다는 생각이 들고 한 달간 7개의 프로젝트를 진행하면서 힘들었던 만큼 많이 성장했다고 느낀다.


