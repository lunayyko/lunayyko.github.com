---
layout: post
category: frontend
tag: [기초, TIL, react, codecademy]
title: 코데카데미 리액트 기초과정 요약 - 리액트의 기본구조
---

## 리액트 기본 앱 구조

App.js
```javascript
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

index.js
```javascript
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

index.html
```javascript
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

### 리액트 컴포넌트 

React는 컴포넌트로 이루어져있다. 컴포넌트에서 UI 조각들을 렌더한다.
렌더하기 위해서는 react와 reactDOM를 import해야한다. 
컴포넌트들은 자바스크립트 함수에 의해 정의된다. 함수 컴포넌트 이름은 대문자로 시작해야하고 파스칼케이스(CamelCase)로 쓰여져야한다. 
함수 컴포넌트는 JSX 문법에 따라 리액트 요소들을 반환해야만한다. 
리액트 컴포넌트들은 파일에서 파일로 export, import될 수 있다.
리액트 컴포넌트들은 HTML같이 생긴 '</>' 문법으로도 불러와질 수 있다.
리액트 컴포넌트를 렌더하려면 root 컨테이너를 명시하기 위해 .createRoot()가 있어야하고 .render()로 불러와야한다. 

### 리액트는 프레임워크일까 라이브러리일까?

프레임워크와 라이브러리는 둘 다 코드 작성에 도움이 되는 타인이 작성한 코드의 집합이다.

프레임워크는 사용방법이 정해져 있어서 이에 따라서 개발자가 개발해나가면 되는 것이고
라이브러리는 개발자가 필요할 때마다 가져다가 설치, 호출하여 사용할 수 있는 것이다.

제어권이 어느쪽에 있느냐에 따라 구분할 수 있고 리액트는 그리하여 라이브러리라고 볼 수 있다.


