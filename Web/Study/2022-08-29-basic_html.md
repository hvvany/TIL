# Web

#HTML #CSS #WEB



## HTML

### Web

- **웹사이트 구성 요소**

  - HTML => 구조
  - CSS => 표현
  - JavaScript => 동작

- [**웹사이트 구성요소 테스트 사이트_html-css-js.com**](https://html-css-js.com/)

- **웹사이트와 브라우저**

  - 웹 사이트는 브라우저를 통해 동작
  - 브라우저별로 파편화가 심해서 웹 표준이 등장

- **웹 표준**

  - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)
  - [브라우저별 호환성 체크_Can I use](https://caniuse.com/)

- **개발 환경 설정**

  - **VS Code** _ Text editor

    > HTML /  CSS 추천 확장 프로그램
    >
    > - Open in browser
    > - Auto Rename Tag
    > - Auto Close Tag
    > - Intellisense for CSS class names in HTML
    > - HTML CSS Support

  - **크롬** 개발자 도구

    > 웹 브라우저 크롬에서 제공하는 다양한 개발 기능
    >
    > - **Elements** : DOM 탐색 및 CSS 확인 및 변경
    >   - Style : 요소에 적용된 CSS 확인
    >   - Computed : 스타일이 계산된 최종 결과
    >   - Event Listeners : 해당 요소에 적용된 이벤트 (JS)
    > - Sources, Network, Performance, Application, Security, Audits 등

    

### HTML 기초

- 웹 사이트에 들어가서 개발자 도구에서 CSS 및 JavaScript를 제거하면 html만 남은 모습을 볼 수 있다

  > 요즘 대부분의 웹사이트는 JavaScript 언어로 구현하기 때문에 제거하면 아무것도 안보이는 경우도 있다

- **HTML**

  > Hyper Text Markup Language

  - **Hyper Text**

    > 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

  - **Markup Language**

    > 태그 등을 이용하여 문서나 데이터의 `구조`를 명시하는 언어
    >
    > HTML, Markdown 등

- **HTML 기본 구조**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
  	<meta charset="UTF-8">
  	<title>Document</title>
  </head>
  <body>
      
  </body>
  </html>
  ```

  - **html** : 문서의 최상위 요소

  - **head** : 문서 메타데이터 요소

    > `title` : 브라우저 상단 타이틀
    >
    > `meta` : 문서 레벨 메타데이터 요소 ( 메타 데이터 : 데이터의 데이터 느낌? )
    >
    > `link` : 외부 리소스 연결 요소 ( CSS파일 )
    >
    > `script` : 스크립트 요소 ( JavaScript 파일/코드 )
    >
    > `stayle` : CSS 직접 작성

    ```html
    <head>
    	<title>HTML 수업</title>
    	<meta charset="UTF-8">
    	<link href="style.css" rel="stylesheet">
    	<script src="javascript.js"></script>
    	<style>
    		p {
    			color: black;
    		}
    	</style>
    </head>
    ```

  - **body** : 문서 본문 요소

- **Open Graph Protocol**

  - 메타 데이터를 표현하는 새로운 규약
    - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
    - 카톡에 링크 올리면 이미지가 함께 뜨는 기능



- **요소(Element)**

  - HTML 의 요소는 `Tag` 와 `Contents` 로 구성되어 있다

    > <tag> Contents </tag>

  - 태그를 통해 정보의 성격과 의미를 정의

  - 닫는 태그가 없는 태그도 존재

    > br : 줄바꿈
    >
    > hr : 수평 가로선
    >
    > img : 이미지
    >
    > input :  사용자의 입력을 받기 위한 상호작용 컨트롤을 생성
    >
    > link : 외부 링크 연결
    >
    > meta : 메타데이터

  - 요소는 중첩될 수 있다

  - 개발자 도구를 통해 해당 요소의 HTML 태그를 확인할 수 있다

- **속성(attribute)**

  - 요소는 속성을 가질 수 있으며, 추가 정보 제공 역할

  - 요소의 `사작 태그`에 작성

  - 태그와 상관없이 사용 가능한 속성도 존재(HTML Global Attribute)

  - `이름` 과 `값`이 하나의 쌍으로 존재

    > <a href="https://goggle.com"><a>
    >
    > href : 속성명
    >
    > url : 속성값

    > 속성과 값을 연결하는 등호는 공백 없이 붙여서!!!

- **HTML Global Attribute**

  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스 목록 ( CSS, JS에서 요소를 선택하거나 접근)
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서

    ```html
     <h4 id="title-yellow" class="title-brown">33</h4>
    ```

- **HTML 코드 예시**

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
  	<meta charset="UTF-8">
  	<title>Document</title>
  </head>
  <body>
  	<!-- 이것은 주석입니다. -->
  	<h1>나의 첫번째 HTML</h1>
  	<p>이것은 본문입니다.</p>
  	<span>이것은 인라인요소</span>
  	<a href="https://www.naver.com">네이버로 이동!!</a>
  </body>
  </html>
  ```

- **Rendering** (렌더링) : 코드를 웹사이트로 변환

- **DOM(Document Object Model) 트리**

  - 텍스트 파일인 HTML 문서를 브라우저에 렌더링 하기 위한 구조

    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/1024px-DOM-model.svg.png)

- **인라인/블록 요소**

  - **인라인** : 이미지 같은 요소를 글자처럼 취금
  - **블록** : 한 줄을 모두 사용

- **텍스트 요소**

  |      태그       |                           설명                           |
  | :-------------: | :------------------------------------------------------: |
  |      \<a>       | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성 |
  | \<b>, \<strong> |                      굵은 글씨 요소                      |
  |   \<i>, \<em>   |                     기울임 글씨 요소                     |
  |      \<br>      |                         줄 바꿈                          |
  |     \<img>      |         src : 이미지 표현<br />alt : 대체 텍스트         |
  |     \<span>     |                의미 없는 인라인 컨테이너                 |

  > strong과 em이 중요한 이유는 시각장애인 등을 위한 웹 접근성 확장을 위해 존재
  >
  > 이미지에 alt도 비슷하게 활용 가능

- **그룹 컨텐츠**

  |     태그      |                           설명                            |
  | :-----------: | :-------------------------------------------------------: |
  |     \<p>      |                        하나의 문단                        |
  |     \<hr>     |                          수평선                           |
  | \<ol>, \<ul>  | 순서있는 리스트, 순서 없는 리스트<br />ordered, unordered |
  |    \<pre>     |             HTML에 작성한 내용을 그대로 표현              |
  | \<blockquote> |  텍스트가 긴 인용문<br />주로 들여쓰기 한 것으로 표현됨   |
  |    \<div>     |               의미 없는 블록 레벨 컨테이너                |

  



## CSS

### CSS 기초

- **CSS**

  > Cascading Style Sheets
  >
  > 스타일을 지정하기 위한 언어

  - 선택자를 통해 스타일을 지정할 HTML 요소를 선택
  - 중괄호 안에서는 `속성`과 `값` 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - `속성` : 어떤 스타일 기능을 변경할지 결정
    - `값` : 어떻게 스타일 기능을 변경할지 결정

  ```css
  h1 {
      color: blue;
      font-size: 15px;
      속성 : 값;
  }
  ```

- **CSS 정의 방법**

  - 인라인

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>Document</title>
    </head>
    <body>
    	<h1 style="color: blue; font-size: 100px;">Hello</h1>
    </body>
    </html>
    ```

  - 내부참조

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>Document</title>
    	<style>
    		h1 {
    			color: blue;
    			font-size: 100px;
    		}
    	</style>
    </head>
    <body>
    </body>
    </html>
    ```

  - 외부 참조

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<meta charset="UTF-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    	<title>Document</title>
    	<link ref="stylesheet" href="mystyle.css"
    </head>
    <body>
    </body>
    </html>
    ```

    >  외부 CSS 파일 불러옴

- **CSS 개발자 도구**

  - `styles` : 해당 요소에 선언된 모든 CSS
  - `computed` : 해당 요소에 최종 계산된 CSS

- **CSS 기초 선택자**

  - **요소** 선택자

    - HTML 태그를 직접 선택

  - **클래스** 선택자

    - `.`문자로 시작하며, 해당 클래스가 적용된 항목을 선택

  - **아이디** 선택자

    - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 여러번 사용해도 동작은 하지만 단일 id 사용을 권장

    > 보통 CSS에서는 클래스를 통한 접근까지만 하고 ID는 JavaScript에서 활용을 한다

- **우선 순위**

  > 아이디 > 클래스 > 태그

​	