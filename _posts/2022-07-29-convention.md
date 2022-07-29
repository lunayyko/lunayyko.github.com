---
layout: post
category: git
tag: [convention]
title: 커밋 컨벤션 예시
---

## 목적

여러명이 커밋을 남길 때, 전에 작업했던 내용을 찾아보기 쉽게, 코드에 마우스오버했을 때 어떤 작업이었는지 설명을 볼 수 있게하기 위해서 커밋을 잘 쓰도록 장려하려고한다.  


### 커밋컨벤션

```markdown

## 브랜치 이름 짓기 규칙
“브랜치이름” + “/” + “기능범위” + “-” + “설명(명사,동사 필요한대로)”     
<br>

### 브랜치 이름
feat : 기능 추가      
update : 기능 업데이트 
fix  : 버그 및 에러 수정
hotfix : 운영에서 바로 에러 수정
add : 배치파일 등 기능에 영향주지 않는 코드 추가  
refactor  : 코드 리팩토링  
<br>

### 브랜치 이름 예시
feat/referral 친구추천 추가   
feat/push_update  푸시세팅 업데이트  
fix/board_summary 게시글 서머리 에러 수정  
feat/identity_verify  신원조회 추가  
hotfix/board_related  관련 게시글 에러 수정(운영)  
add/notice_redis  공지글 redis에 추가 
refactor/board_video 영상게시글 관련코드 리팩토링 
<br>
<br>

## 커밋 컨벤션
“이슈번호” + “타입” + “(작업하는 부분)“ + ":" + “설명”  
<br>

### 타입
add: 새로운 기능 추가  
update: 기능 부분 업데이트  
fix: 버그 수정  

docs: 문서 수정  
chore: 빌드 스크립트 설정 변경, 패키지 매니저 수정  
test: 테스트 코드, 리팩토링 테스트 코드 추가  
refactor: 코드 리팩토링  
ci: ci 관련 스크립트 파일 수정  
merge: merge 시 사용  
<br>

### 예시
add(board_temp): 임시저장 추가   
update(i2e): 프리미엄스코어 로직 수정 
fix(community) : 커뮤니티 리스트 오류 수정 
docs(contributor) : 커밋 컨벤션  
```
