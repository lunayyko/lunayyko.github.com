---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제6 디어(전동킥보드대여)
---

# 과제 설명 요약
- 구현 기간 : 21.11.18(18시) ~ 21.11.21 (22시)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment6) 참고

# 과제 설명

디어는 사용자의 요금을 계산하기 위해 다양한 상황을 고려합니다. 

- 우선 지역별로 다양한 요금제를 적용하고 있습니다. 예를 들어 건대에서 이용하는 유저는 기본요금 790원에 분당요금 150원, 여수에서 이용하는 유저는 기본요금 300원에 분당요금 70원으로 적용됩니다.
- 할인 조건도 있습니다. 사용자가 파킹존에서 반납하는 경우 요금의 30%를 할인해주며, 사용자가 마지막 이용으로부터 30분 이내에 다시 이용하면 기본요금을 면제해줍니다.
- 벌금 조건도 있습니다. 사용자가 지역 바깥에 반납한 경우 얼마나 멀리 떨어져있는지 거리에 비례하는 벌금을 부과하며, 반납 금지로 지정된 구역에 반납하면 6,000원의 벌금을 요금에 추과로 부과합니다.
- 예외도 있는데, 킥보드가 고장나서 정상적인 이용을 못하는 경우의 유저들을 배려하여 1분 이내의 이용에는 요금을 청구하지 않고 있습니다.

최근에 다양한 할인과 벌금을 사용하여 지자체와 협력하는 경우가 점점 많아지고 있어 요금제에 새로운 할인/벌금 조건을 추가하는 일을 쉽게 만드려고 합니다. 어떻게 하면 앞으로 발생할 수 있는 다양한 할인과 벌금 조건을 기존의 요금제에 쉽게 추가할 수 있는 소프트웨어를 만들 수 있을까요? 

우선은 사용자의 이용에 관한 정보를 알려주면 현재의 요금 정책에 따라 요금을 계산해주는 API를 만들어주세요. 그 다음은, 기능을 유지한 채로 새로운 할인이나 벌금 조건이 쉽게 추가될 수 있게 코드를 개선하여 최종 코드를 만들어주세요.

**다음과 같은 정보들이 도움이 될 것 같아요.**

---

- 요금제가 사용자 입장에서 합리적이고 이해가 쉬운 요금제라면 좋을 것 같아요.
- 앞으로도 할인과 벌금 조건은 새로운 조건이 굉장히 많이 추가되거나 변경될 것 같아요.
- 가장 최근의 할인/벌금 조건의 변경은 '특정 킥보드는 파킹존에 반납하면 무조건 무료' 였습니다.

**이용에는 다음과 같은 정보들이 있습니다.**

---

```
use_deer_name (사용자가 이용한 킥보드의 이름)
use_end_lat, use_end_lng (사용자가 이용을 종료할 때 위도 경도)
use_start_at, use_end_at (사용자가 이용을 시작하고 종료한 시간)
```

**데이터베이스에는 킥보드에 대해 다음과 같은 정보들이 있습니다.**

---

```
deer_name (킥보드의 이름으로 고유한 값)
deer_area_id (킥보드가 현재 위치한 지역의 아이디)
```

**데이터베이스에는 지역에 대해 다음과 같은 정보들이 있습니다.**

---

```
area_id (지역 아이디로 고유한 값)
area_bounday (지역을 표시하는 MySQL spatial data로 POLYGON)
area_center (지역의 중심점)
area_coords (지역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

**데이터베이스에는 파킹존에 대해 다음과 같은 정보들이 있습니다.**

---

```
parkingzone_id (파킹존 아이디로 고유한 값)
parkingzone_center_lat, parkingzone_center_lng (파킹존 중심 위도, 경도)
parkingzone_radius (파킹존의 반지름)
```

**데이터베이스에는 반납금지구역에 대해 다음과 같은 정보들이 있습니다.**

---

```
forbidden_area_id (반납금지구역 아이디로 고유한 값)
forbidden_area_boundary (반납금지구역을 표시하는 MySQL spatial data로 POLYGON)
forbidden_area_coords (반납금지구역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

# 디어 서비스 화면

![디어 서비스 화면](/public/img/deer_app.jpeg)

# 사용한 기술 설명

MySQL에서 point, polygon필드를 사용해서 킥보드의 경도 및 위치를 판단하여 전동킥보드의 대여, 반납 및 요금계산(할인 및 벌금 부과)을 하는 프로젝트였는데 새로운 개념이었고 여러가지 문제가 겹쳐서 추가 기능까지는 못하고 기본 기능인 대여, 반납, 기본 요금계산을 구현하게 되었다.

좌표를 이용하려면 GDAL이라는 것을 사용해야했는데 매우 새로운 개념이기도하고 gdal이 개인 개발환경에 따라 설치되지 않기도 해서 포기하는 팀들이 좀 있었다.

- [GDAL API](https://runebook.dev/ko/docs/django/ref/contrib/gis/gdal)
GDAL 은 Geospatial Data Abstraction Library의 약자 이며 GIS 데이터 기능의 "스위스 군용 칼"입니다. GDAL의 하위 집합은 다양한 표준 형식의 벡터 지리 데이터를 읽고 쓰는 것을 전문으로 하는 OGR Simple Features Library입니다.

- GeoDjango는 벡터 공간 데이터의 읽기 및 좌표 변환과 래스터 (이미지) 데이터에 대한 GDAL의 기능에 대한 최소 지원을 포함하여 OGR의 일부 기능을위한 고급 Python 인터페이스를 제공합니다.

우리 팀은 도커를 사용해서 개발환경을 설정하고 진행했다. 좌표를 다루는 기능구현에 있어서 팀장님의 블로그에 나와있어서 링크를 첨부한다. [태우님의 디어코퍼레이션 과제 블로그 글](https://velog.io/@burnkim61/%ED%94%84%EB%A6%AC%EC%98%A8%EB%B3%B4%EB%94%A9-%EA%B3%BC%EC%A0%9C-6)

# 모델링

![디어 erd1](/public/img/deer_erd.png)
처음에 나는 이렇게 erd를 작성했다. 팀에서 최종적으로 사용한 모델링은 아래와 같다.  

![디어 erd2](/public/img/deer_erd2.png)

킥보드의 사용을 시작하면 BoardingLog에 시작 시간과 함께 기록을 시작하고 in_use 필드를 True로 변경한다.  

in_use필드를 deer 테이블에 넣을 것인지 boardingLog에 넣을 것인지에 대해서 고민했는데 deer와 user테이블 양쪽에서 참조를 통해서 in_use값을 사용하는 경우가 있을 것 같아서 중간에 있는 테이블인 boardingLog에 넣기로 했다. 

# 내가 작성한 코드 / 기억에 남는 코드

```python
#vehicle > views.py
from datetime                        import datetime

from rest_framework                  import status, viewsets, response
from rest_framework.decorators       import action
from rest_framework.permissions      import IsAuthenticated, AllowAny

from vehicle.models                  import Deer, BoardingLog
from user.serializers                import UserSerializer
from vehicle.serializers             import DeerSerializer, BoardingLogSerializer

class VehicleViewSet(viewsets.GenericViewSet):
    quertset           = Deer.objects.all()
    serializer_class   = DeerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field       = 'deer_name'

    #킥보드를 대여하는 로직, 파라미터를 받는 경우에 detail=True를 적용한다. 
    @action(detail=True, methods=['POST'])
    def rent(self, request, deer_name):
        #사용자가 킥보드를 대여중인 경우
        if BoardingLog.objects.filter(user_id = request.user.id, in_use=True).exists():
            return response.Response("One Deer Allowed", status=status.HTTP_400_BAD_REQUEST)
        #킥보드가 사용중인 경우
        if BoardingLog.objects.filter(deer__name = deer_name, in_use=True).exists():
            return response.Response("Already In Use", status=status.HTTP_400_BAD_REQUEST)

        BoardingLog.objects.create(
            user_id = request.user.id,
            deer = Deer.objects.get(name = deer_name),
            in_use = True,
            use_start_at = datetime.now()
        )
        return response.Response("Start Using Deer", status=status.HTTP_200_OK)
```

