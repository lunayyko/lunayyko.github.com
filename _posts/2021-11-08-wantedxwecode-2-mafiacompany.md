---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제2 Mafia company
---

# 과제 설명 요약
- 구현 기간 : 21.11.04(18시) ~ 21.11.06 (10시)
- 뮤지션 곡 앨범 3개가 있다고 가정하고 관계를 연결해서 관련된 정보를 얻는 로직을 구현 (단 앨범과 뮤지션은 연결이 안되어 있다고 가정한다)
- db는 무조건 neo4j GraphDB를 사용해야된다.
- CUD는 REST API로 구현
- Read쪽은 Graph QL로 구현하면 가산점 있음 (Strawberry 라이브러리 추천)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment2) 참조

# 과제 설명
- 마피아컴퍼니 선호 기술스택
    - Python/FastAPI
    - Javascript 사용시 선호 프레임워크 없음
- 사용 필수 데이터 베이스
    - neo4j GraphDB
    - 개발 완료 시 리뷰어가 실행해볼 수 있도록 neo4j 디비를 csv 로 export해서 프로젝트 루트 경로에 포함해주세요.
- API 구성은 Restful API 형태로 구성하시면 됩니다.
    - GraphQL로 구현하면 가산점이 있습니다.
        - Strawberry graphql 라이브러리 추천
        - CUD는 GraphQL Mutation 으로 만들지 않고, Restful로 만들어주세요.

### [필수 포함 사항]

- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### [과제 안내]
- 음악 스트리밍 서비스에는 3가지 요소 `뮤지션` `곡` `앨범` 이 존재합니다.
   
- 앨범 페이지, 뮤지션 페이지, 곡 페이지에 인접 정보들 (ex, 곡의 뮤지션, 곡의 앨범) 을 표현할 수 있도록 **CRUD** API를 구성해주세요.
   
- 이 페이지들에 대한 DB를 구성할 때 `곡` - `뮤지션` 연결과  `곡` 

- `앨범` 연결은 내부 운영팀에서 직접 연결 가능하지만, `뮤지션` - `앨범` 정보까지 태깅하기엔 내부 운영 리소스가 부족한 상황으로 가정해보겠습니다. 

- 이 때, `뮤지션` - `곡` 이 연결되어있고  `곡` - `앨범` 이 연결되어있다면  `뮤지션` - `[곡*]` - `앨범` 연결되어있다고 판단할 수 있는데요. 이 특성을 이용해서 `뮤지션` 의 `앨범` 을 보여주는 Read API, 특정 `앨범` 의 뮤지션 목록을 보여주는 Read API를 만들어주세요. 

**각 요구사항을 아래에 명시해두었습니다.**
- 화면별 Read API 요구사항
   -  `곡` 페이지 
       - 해당 `곡`이 속한 `앨범`을 가져오는 API
       - 해당 `곡`을 쓴 `뮤지션` 목록을 가져오는 API 
    - `앨범` 페이지  
      - 해당 `앨범`을 쓴 `뮤지션` 목록 가져오는 API
      - 해당 `앨범`의 `곡` 목록을 가져오는 API
    - `뮤지션` 페이지 
      - 해당 `뮤지션`의 모든 `앨범` API
      - 해당 `뮤지션`의 `곡` 목록 가져오는 API

- **Create, Update, Delete API 요구사항**
    - `곡` 생성 API
    - `앨범` 생성 API
    - `뮤지션` 생성 API
    - `뮤지션` - `곡` 연결/연결해제 API
    - `곡` - `앨범` 연결/연결해제 API
    - `뮤지션` - `앨범` 연결/연결해제 API 는 필요하지 않습니다. (구현 X)
        - `뮤지션` - `곡` 연결과 `곡` - `앨범` 연결이 되어있으면
        GraphDB (neo4j) 에서 `뮤지션` - [*] - `앨범` 연결 여부를 뽑을 수 있습니다. **이 특성을 Read API에서 활용**해주세요.

- Neo4j DB 테이블 요구사항
  - `뮤지션`, `곡`, `앨범`은 각각의 테이블 (musician, song, album)로 구성되어야합니다.
  -  `앨범` 안에는 여러 `곡`이 속해있을 수 있습니다.
  - 한 `곡`에는 여러 `뮤지션`이 참여할 수 있습니다.
  - 한 `곡`은 `앨범` 1개에만 들어가있습니다.
  - `뮤지션`은 여러 앨범을 갖고 있을 수 있습니다.
  -  `뮤지션`, `앨범`, `곡` 데이터는 위 relation을 테스트할 수 있을만큼 임의로 생성해주시면 좋습니다.

# 사용한 기술 설명

- GraphDB
기업에서 요구 조건 중에 neo4j디비는 NoSQL인 GraphDB이다. 아래 사진과 같이 각 객체와의 연결로 나타내어진다. 

![image](https://user-images.githubusercontent.com/80395324/140564638-42832fa8-4915-4f3b-b518-d54f66b5f202.png)

처음 프로젝트를 할 때는 GraphDB에 대한 이해가 없었는데 아래 영상을 보고, SQL과 NoSQL은 한국음식과 No한국음식과 같은 개념이라는 니꼬의 설명이 짧은 시간 안에 이해하는데 도움이 많이 되었다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q_9cFgzZr8Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

뮤지션과 앨범이 연결되지 않는다는 전제를 가지고 생각만으로 팀원들과 소통하고 코드를 짜기가 불편해서 아래와 같이 그림을 그려서 얘기했는데 한결 편했다.

![image](https://user-images.githubusercontent.com/80395324/140564608-72723da3-731b-45e3-9adc-0416615bd1fc.png)

- GraphQL
Restful API가 아닌 GraphQL이라는 방식으로 클라이언트와 연결을 하는 것을 처음 해봤는데 얄팍한 코딩사전의 병맛 피자가게 만화가 이해에 많은 도움이 되었다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EkWI6Ru8lFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 기억에 남는 코드

뷰셋을 처음 써봤는데 다른 팀원분이 작성해주신 동일한 구조의 코드에서 앨범만 뮤지션으로 바뀌는거라서 괜찮았지만 neo4j 디비에 연결해서 코드를 실행해보는 부분이 처음 보는 것이라서 어려웠다. 특정 뮤지션의 앨범들을 조회하는 부분은 팀장님과 다른 분 2분께서 2시간여를 씨름하다가 작성해주셨다.

```python
class MusicianViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    #뮤지션 CRUD
    def create(self, request):
        name = request.data.get('name')
        if name is None:
            return Response({'error': 'name field is required.'},status=status.HTTP_400_BAD_REQUEST)
        musician = Musician(name=name).save()
        rtn = MusicianSerializer(musician).data
        return Response(rtn, status=status.HTTP_201_CREATED)

    def list(self, request):
        musicians = Musician.nodes.all()
        rtn = MusicianSerializer(musicians, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        musician = Musician.nodes.get_or_none(uuid=pk)
        if musician is None:
            return Response({'error': 'DoesNotExist'})
        rtn = MusicianSerializer(musician).data
        return Response(rtn, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        musician = Musician.nodes.get_or_none(uuid=pk)
        musician.delete()
        return Response(status=status.HTTP_200_OK)
    
    #특정 뮤지션의 곡들을 조회 
    @action(detail=True, methods=['GET'])
    def songs(self, request, pk):
        musician = Musician.nodes.get_or_none(uuid=pk)
        if musician is None:
            return Response({'error': 'DoesNotExist'})
        songs = musician.song.all()
        rtn = SongSerializer(songs, many=True).data
        return Response(rtn, status=status.HTTP_200_OK)
```

# 프로젝트 후기

위워크 여의도점에서 18시간 정도 진행을 했는데 새로운 기술스택에 대한 이해가 낮고 새로운 디비의 세팅을 할 수가 없어서 처음에 대화에 참여하기가 어려웠다. 우리 팀은 운이 좋게도 5명 중에 세 분이 전공자인데 정말 잘 하신다. 나와 비전공자 한 분은 팀장님이 셋팅해준 구조 위에서 각각 뮤지션과 곡의 API를 작성했는데 기능 구현을 다 하고나서 11시쯤에 테스트케이스를 작성하기 시작할 때 너무 피곤해서 막차를 타러가서 남아서 첫차 탈 때까지 작업하신 두 분께 미안했다. 