---
layout: post
category: frontend
tag: [기초, TIL, react, codecademy]
title: 코데카데미 리액트 기초과정 요약 - 리액트의 기본구조
---

## 코드

App.js
```
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

index.js
```
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

index.html
```
import React from 'react';

function MyComponent() {
  return <h1>Hello world</h1>;
}

export default MyComponent;
```

React applications are made up of components.

Components are responsible for rendering pieces of the user interface.

To create components and render them, react and reactDOM must be imported.

React components can be defined with Javascript functions to make function components.

Function component names must start with a capitalized letter, and Pascal case is the adopted naming convention.

Function components must return some React elements in JSX syntax.

React components can be exported and imported from file to file.

A React component can be used by calling the component name in an HTML-like self-closing tag syntax.

Rendering a React component requires using .createRoot() to specify a root container and calling the .render() method on it.


### 리액트는 프레임워크일까 라이브러리일까?

프레임워크와 라이브러리는 둘 다 코드 작성에 도움이 되는 타인이 작성한 코드의 집합이다.

프레임워크는 사용방법이 정해져 있어서 이에 따라서 개발자가 개발해나가면 되는 것이고
라이브러리는 개발자가 필요할 때마다 가져다가 설치, 호출하여 사용할 수 있는 것이다.

제어권이 어느쪽에 있느냐에 따라 구분할 수 있고 리액트는 그리하여 라이브러리라고 볼 수 있다.


