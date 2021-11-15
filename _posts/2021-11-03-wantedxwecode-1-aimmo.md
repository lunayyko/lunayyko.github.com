---
layout: post
category: wecode
tag: [wantedxwecode]
title: 원티드 x 위코드 프리온보딩 과제1 Aimmo 
---

# 과제 설명 요약

- 구현 기간 : 21.11.01(17시) ~ 21.11.03 (10시)
- 기본적인 게시판 CRUD 구현
- 댓글과 대댓글 기능 필요하며, pagination 구현 해야된다.
- db는 무조건 mongodb를 사용해야된다.
- 성능 테스트 필요(1000만건의 data가 db에 있는 상태에서)
- 자세한 내용은 [Github](https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment1-TW-JW-YY) 참조

# 과제 설명

- [에이모 사이트](https://aimmo.co.kr/)
- [wanted 채용공고 링크](https://www.wanted.co.kr/wd/16937)

<aside>
📝 아래 요구사항에 맞춰 게시판 Restful API를 개발합니다.
</aside>

- 에이모 선호 기술스택: python flask, mashmallow, mongoengine
- 필수 사용 데이터베이스: mongodb

### **[필수 포함 사항]**

- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

### [개발 요구사항]

- 원티드 지원 과제 내용 포함
- 게시글 카테고리
- 게시글 검색
- 대댓글(1 depth)
    - 대댓글 pagination
- 게시글 읽힘 수
    - 같은 User가 게시글을 읽는 경우 count 수 증가하면 안 됨
- Rest API 설계
- Unit Test
- 1000만건 이상의 데이터를 넣고 성능테스트 진행 결과 필요

# 사용한 기술 설명

**Djongo 사용**

Django에서 기본적으로 제공하는 Database는 Mongodb가 포함되어 있지 않아서 Mongodb기반의 ORM을 작성할 수 있도록 해주는 Djongo를 사용하여 Mongodb와 연결했다.

**Docker 사용**

팀원들의 빠른 개발환경 셋팅을 위해서 로컬 개발용과 배포용 docker-compose 파일을 만들어서 적용했다.

<details markdown="1">
<summary>docker-compose-deploy.yml 파일 펼쳐서 보기</summary>

```
version: "3"
services:
  aimmo_deploy_db:
    image: mongo
    container_name: aimmo_deploy_db
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - ./mongodb/database:/data/db
    ports:
      - 27017:27017
    restart: unless-stopped
  aimmo_deploy_backend:
    build:
      context: .
      dockerfile: ./Dockerfile-deploy
    container_name: aimmo_deploy_backend
    ports:
      - 8000:8000
    depends_on:
      - aimmo_deploy_db
    restart: always
    environment:
      DB_HOST: aimmo_deploy_db
      DJANGO_SETTINGS_MODULE: aimmo.settings.deploy
    env_file:
      - .dockerenv.deploy
    command:
      - bash
      - -c
      - |
        python manage.py migrate
        gunicorn --bind 0.0.0.0:8000 aimmo.wsgi:application
    volumes:
      - .:/usr/src/app/
```

</details>

# 기억에 남는 코드

### 대댓글을 보여주는 api

```python
class CommentView(View):
    @login_decorator
    def get(self, request, post_id):
        parent_id = int(request.GET.get("parent_id","0"))
        #parent_id를 받아와서 저장한다. 없는 경우에는 0.

        if parent_id == 0:
            all_comments = Comment.objects.filter(post_id=post_id, parent_comment__isnull=True).select_related('user')
        #parent_id가 0인 경우(대댓글이 아닌 댓글)에는 parent_comment_id 컬럼이 null인 코멘트들(댓글)을 불러온다. 'parent_id' 라는 변수에 0이 입력되면 댓글을 조회
        
        else:
            all_comments = Comment.objects.filter(post_id=post_id, parent_comment_id=parent_id).select_related('user')
        #대댓글일 경우에는 parent_comment_id가 해당 id인 코멘트들(대댓글)을 불러온다. 'parent_id' 라는 변수에 *이 입력되면 *번 댓글의 대댓글을 조회

        limit = int(request.GET.get("limit","10"))
        offset = int(request.GET.get("offset","0"))
        offset=offset*limit
        
        comments  = all_comments[offset:offset+limit]
        #대댓글의 페이지네이션을 짤 때 어떤 순서로 댓글을 보여주어야할 지 고민했었는데 

        comment_list = [{   
                'comment_id' : comment.id,
                'user_id'    : comment.user_id,
                'email'      : comment.user.email,
                'content'    : comment.content,
                'created_at' : comment.created_at,
                'updated_at' : comment.updated_at,
                'parent_id'  : comment.parent_comment_id,
                } for comment in comments
            ]
        return JsonResponse({'comments':comment_list}, status=200)
```

### 댓글과 대댓글을 보여주는 url

{server_url}/posts/1/comments?parent_id=1&offset=0&limit=5
-> 1번 게시물 / 1번 댓글의 대댓글을 조회 / 5개의 대댓글을 조회

### 데이터 천만건 넣기?

우리 팀은 시간이 없어서 성능테스트를 하지 못했는데 온보딩 참여하신 분 중에 성능테스트를 하고 블로그를 아주 잘 작성하신 분이 계셔서 링크를 첨부한다.
[김태희 - [WEEK1] Aimmo 기술과제를 마치고..](https://medium.com/@godtaehee/week1-aimmo-%EA%B8%B0%EC%88%A0%EA%B3%BC%EC%A0%9C%EB%A5%BC-%EB%A7%88%EC%B9%98%EA%B3%A0-67fffb08b47b)

# 프로젝트 후기

처음 만나는 사람 세명이서 거의 하루만에 하는 프로젝트였음에도 불구하고 능력이 엄청 좋으면서 사려깊은 팀장님과 정말 열심히 공부하시고 밝고 친절한 분을 팀원으로 만나서 잘 끝낼 수 있었다.
나는 밤 12시쯤에 전사했지만 나머지 두 분께서 새벽 4시반까지 마무리작업을 해주셨는데 리드미와 커밋메세지가 좋은 사례로 뽑혀서 온보딩을 진행하는 위코드 대표 은우님께서 세션을 하면서 다른 분들께 보여드렸다.  

처음 써보는 몽고디비와 도커 개발환경으로 초기 세팅을 하다보니 태우님이 해주셨는데 좀 시간이 걸려서 그 동안 모델링을 하고 오후 5시정도부터 뷰를 쓰기 시작했다. 댓글 CRUD는 원래 하던 것에서 가져와서 금방했는데 대댓글을 구현하는 부분이 어려웠어서 태우님께서 저 기억에 남는 코드를 작성해주셨다. 

처음하는 프로젝트라서 시간이 더 걸렸던 것 같고 후기를 쓰는 지금은 세번째 프로젝트가 진행중인데 서로 기술 수준도 잘 알고 패턴도 잘 알고, 미리 시작하고 위워크에서 오프라인으로 만나고해서 훨씬 수월해진 것 같다.