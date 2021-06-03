---
layout: post
title: 깃헙 블로그 만들기 05.26 TIL
---

<div class="message">
  첫번째 TIL 포스트는 깃헙블로그 만들기 
</div>

깃헙에서는 계정이 있으면 지킬을 이용하여 무료로 블로그를 한 개 호스팅할 수 있다. 

 <a href="https://velog.io/@shg4821/%EA%B9%83%ED%97%88%EB%B8%8C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-1">껴르님의 포스팅과</a> <a href="https://velog.io/@shg4821/%EA%B9%83%ED%97%88%EB%B8%8C-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-1">한결님의 포스팅</a> 등을 참고해서 만들었고, 테마는 <a href="https://wayhome25.github.io/">초보몽키</a>님의 테마를 사용했다. 

> 처음에 css가 연결되지 않아서 반나절정도 검색을 하다가 무엇 때문인지 baseurl을 큰따옴표에서 작은따옴표로 바꿔야했었다는 사실을 깨달았다. 

정말 **충격과 공포** 그래서 일주일간 쳐다보지않았다.
## 1.깃헙 레포지터리 생성

새 저장소를 만들고 이름을 {username}.github.io 으로 만든다.

## 2.루비와 지킬 설치 

지킬은 깃헙의 공동창업자가 루비로 만든 간단한 정적인 사이트 생성기다. 그래서 루비를 먼저 설치해야한다. 

<div class ="message">
  Jekyll이란 HTML(.html), Markdown(.md) 등 다양한 포맷의 텍스트들을 읽고 가공하여 자신의 웹 사이트에 바로 게시할 수 있게 해주는 Rubby언어로 만들어진 하나의 텍스트 변환 엔진이라고 보면 됩니다.
</div>

```
ruby -v
//루비가 설치되어있는지 버전을 확인
\curl -sSL https://get.rvm.io | bash -s stable
rvm install ruby-2.6.6
```

```
gem install jekyll bundler
//지킬 설치
jekeyll -v
//설치가 잘 되었는지 확인
bundle exec jekyll serve
//지킬 실행
```


루비가 설치되어있는지 버전을 확인하고 없다면 루비 버전관리 매니저를 설치한 뒤 루비 2.6.6버전을 설치하고나서 지킬을 설치해준다.
## 3. 깃헙 레포지터리를 로컬 컴퓨터에 다운로드하고 변경사항을 푸시하기

<iframe width="560" height="315" src="https://www.youtube.com/embed/pYgfXPoNhUg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

예전에 찍어놓은 영상이라 퀄리티가 좋지 않지만 도움이 되기를 바란다.

### 오늘의 단축키

Command + shift + del 캐시 삭제

Command + shift + F   vs code 내의 열린 폴더 전부에서 찾기

### 더 공부할 부분

https://honbabzone.com/jekyll/start-gitHubBlog/
- Admin 페이지 세팅하기
- disqus 추가하기