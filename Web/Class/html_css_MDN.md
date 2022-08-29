# HTML & CSS 기초

#HTML #CSS #MDN



## MDN

> Mozila Developer Network 모질라 개발자 네트워크



## HTML

> Hyper Text Markup Language 는 웹을 이루는 가장 기초적인 구성 요소
>
> 웹 콘텐츠의 의미와 구조를 정의
>
> CSS, JavaScript와 함께 사용



### HTML 요소 분석

```html
<p>내 고양이는 고약해</p>
```

1. **여는 태그(opening tag)**: \<p>
2. **닫는 태그(closing tag)**: \</p>
3. **컨텐츠(content)**: 내 고양이는 고약해
4. **요소(element)**: \<p>내 고양이는 고약해\</p>



### 속성

>  실제 컨텐츠로 표시되길 원하지 않는 추가적인 정보

- **속성 작성 조건**

  1. 요소 이름 (또는 요소가 하나 이상 속성을 이미 가지고 있다면 이전 속성)과 속성 사이에 `공백`이 있어야 합니다.

  2. 속성 이름 뒤에는 `등호(=)`가 와야 합니다.

  3. 속성 값의 앞 뒤에 열고 닫는 `인용부호(" 또는 ')`가 있어야 합니다.




### 요소 중첩

> 태그 안에 또다른 태그로 감싸서 요소가 중첩이 되어 있는 것

```html
<p>내 고양이는 <strong>아주</strong> 고약해.</p>
```



### 빈 요소

> 어떤 요소들은 내용을 갖지 않는다

```html
<img src="images/firefox-icon.png" alt="My test image">
```

- img 요소는 닫는 태그가 없다



### HTML 문서 해부

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- `<!DOCTYPE html>` — **역사적 유물**. 좋은 html인지 검증 받던 시절이 있었다. 지금은 안적으면 실행이 안되므로 적어준다.
- `<html></html>` — 페이지 전체의 컨텐츠를 감싸며, **루트(root) 요소**라고도 한다.
- `<head></head>` —페이지 방문자에게는 **보여줄 필요 없지만 필요한** 데이터를 저장하는 곳. 여기에는 [keywords (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Keyword), 페이지 설명, CSS, 문자 집합 선언 등이 포함된다.
- `<body></body>` —페이지 방문자에게 **보여주길 원하는 모든 컨텐츠**를 담고 있는 곳.
- `<meta charset="utf-8">` — 이 요소는 **문서가 사용해야 할 문자** 집합 설정할 수 있다. 어떠한 유형도 가능하다. 보통 utf-8
- `<title></title>` —**페이지의 제목**. 브라우저 탭, 북마크 등에 표시되는 제목이다.



### 이미지

```html
<img src="images/firefox-icon.png" alt="My test image">
```

- `src` : source 의미로써 **이미지 파일의 경로**를 포함하는 속성
- `alt` : alternate 의미로써 **이미지를 볼 수 없는 사용자들을 위한 설명문**



### 문자 나타내기

#### 제목

> \<h1> ~ \<h6> 태그를 통해 제목의 상위, 하위 순서 지정

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

#### 문단

> \<p> 태그를 통해 문단 나눔

```html
<p>This is a single paragraph</p>
```

#### 목록

> \<ol> 순서가 있는 목록, 그리고 \<ul> 순서가 없는 목록을 표현한다
>
> 목록의 각 요소는 \<li> 태그로 감싸 준다

```html
<p>At Mozilla, we’re a global community of</p>

<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>

<p>working together ... </p>
```



### 연결

> \<a> 태그를 통해 url 주소로 연결시켜 준다
>
> anchor 닻의 약자로 항해를 하다가 닻을 내리는 비유로 이름이 붙게 되었다.
>
> 연결은 웹을 웹으로 만들어주는 아주 중요한 요소이다

```html
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```





## CSS

> CSS (Cascading Style Sheets)는 웹페이지를 **꾸미려고** 작성하는 코드
>
> CSS는 프로그래밍 언어, *마크업(markup) 언어* 도 아닙니다. ***Style sheet 언어*** 입니다.



### CSS의 rule set 해부

```css
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

> 전체 구조를 **rule set** 이라 한다

- **선택자(selector)** _ `p`

  rule set의 맨 앞에 있는 HTML 요소 이름

- **선언** _ `color : red`

  `color: red`와 같은 단일 규칙. 꾸미기 원하는 요소의 속성을 명시

- **속성(property) **_ `color`

  주어진 HTML 요소를 꾸밀 수 있는 방법

- **속성 값** _ `red`

  속성 : 뒤에 다양한 값 표현

**※ 주의할점**

- 각각의 **rule set** (**셀렉터로 구분**) 은 반드시 (`{}`) 로 감싸져야 합니다.
- 각각의 선언 안에, 각 **속성을 해당 값과 구분**하기 위해 콜론 (`:`)을 사용해야만 합니다.
- 각각의 rule set 안에, 각 선언을 그 **다음 선언으로부터 구분**하기 위해 세미콜론 (`;`)을 사용해야만 합니다.



### 여러 요소 선택하기

>  콤마로 여러 요소 지정 후 모두에게 하나의 rule set 적용 가능

```css
p,li,h1 {
  color: red;
}
```



### 선택자의 여러 종류

> 위에서는 **요소 선택자**만 봤다. 하지만 이것보다 더 구체적인 선택을 만들 수 있다.

| 선택자 이름                                       | 선택하는 것                                                  | 예시                                                         |
| :------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 요소 선택자 (때때로 태그 또는 타입 선택자라 불림) | 특정 타입의 모든 HTML 요소                                   | `p` `<p> 를 선택`                                            |
| 아이디 선택자                                     | 특정 아이디를 가진 페이지의 요소 (주어진 HTML 페이지에서, 아이디당 딱 하나의 요소만 허용) | `#my-id` `<p id="my-id">` 또는 `<a id="my-id">` 를 선택      |
| 클래스 선택자                                     | 특정 클래스를 가진 페이지의 요소 (한 페이지에 클래스가 여러번 나타날 수 있습니다) | `.my-class` `<p class="my-class">` 와 `<a class="my-class">` 를 선택 |
| 속성 선택자                                       | 특정 속성을 갖는 페이지의 요소                               | `img[src]` `<img src="myimage.png">` 를 선택하지만 `<img> `는 선택 안함 |
| 수도(Pseudo) 클래스 선택자                        | 특정 요소이지만 특정 상태에 있을 때만, 예를 들면, hover over 상태일 때 | `a:hover` `<a>` 를 선택하지만, 마우스 포인터가 링크위에 있을 때만 선택함 |



### 글꼴과 문자

```css
html {
  font-size: 10px; /* px 은 'pixels' 를 의미합니다: 기본 글자 크기는 현재 10 pixels 높이입니다. */
  font-family: placeholder: 구글 폰트로부터 여러분이 얻은 마지막 결과가 있어야합니다.
}
```



> body 콘텐츠의 제목을 가운데 정렬하고 줄의 높이(line-height) 와 자간(lettet-spacing)도 설정

```css
h1 {
  font-size: 60px;
  text-align: center;
}

p, li {
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}
```





### 박스의 모든 것

> 웹 페이지에 있는 대부분의 HTML 요소들은 서로의 위에 놓여있는 박스로 생각해볼 수 있다.



> CSS 레이아웃은 *박스모델* 을 주 기반으로 하고 있다. 페이지의 공간을 차지하고 있는 각각의 블록들은 아래와 같은 속성들을 가진다

- `padding`, 컨텐트 주위의 공간 (예, 문단 글자의 주위)
- `border`, padding 의 바깥쪽에 놓인 실선
- `margin`, 요소의 바깥쪽을 둘러싼 공간

> 여기서 이런 것도 사용한다

- `width` (한 요소의 너비)
- `background-color`, 요소의 콘텐츠와 padding 의 배경 색
- `color`, 한 요소의 콘텐츠 색 (일반적으로 글자색)
- `text-shadow`: 한 요소 안의 글자에 그림자를 적용
- `display`: 요소의 표시 형식을 설정합니다 (이것에 대해선 아직 걱정하지마세요)



### 페이지 색 바꾸기

```css
html {
  background-color: #00539F;
}
```

이 rule 은 전체 페이지를 위한 배경색을 설정한다.



### body 외부 정렬하기

```css
body {
  width: 600px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}
```

> 이제는 body 요소를 위한 것들이다.

- `width: 600px;` — 이것은 body가 항상 600 pixels 의 너비를 갖도록 강제합니다.
- `margin: 0 auto;` — 여러분이 `margin` 또는 `padding` 처럼 한 속성에 두개의 값을 설정할 때, 첫 번째 값은 요소의 상단과 하단 (이 예시에서는 0입니다) 에 영향을 주고, 두 번째 값은 좌측 **과** 우측 (여기서, `auto` 는 가능한 수평공간의 왼쪽과 오른쪽을 같게 나눠주는 특별한 값입니다) 에 영향을 줍니다. 여러분은 또한 하나, 셋, 또는 네개의 값을 사용할 수도 있습니다. [여기](https://developer.mozilla.org/ko/docs/Web/CSS/margin#values)에 문서화 되어 있습니다.
- `background-color: #FF9500;` — 전과 같이, 이것은 요소의 배경색을 설정합니다. `html` 요소를 위한 짙은 파란색에 반대되도록 body 에는 붉은 빛을 띄는 오렌지색 같은 것을 사용했었습니다. 한번 시험해보세요. 흰색이나 여러분이 원하는 어떤 색이든 편하게 사용해보세요.
- `padding: 0 20px 20px 20px;` — padding 에는 콘텐츠의 주위에 약간의 공간을 주기 위한 네 개의 값이 있습니다. 이번엔 body의 상단에 no padding, 그리고 왼쪽, 아래 그리고 오른쪽에 20 pixels 을 설정하고 있습니다. 상단, 우측, 하단, 좌측 순서로 값을 설정합니다.(12시부터 시계방향)
- `border: 5px solid black;` — 이것은 간단하게 body 모든 면의 border 를 5 pixels 두깨의 실선으로 설정합니다.



### 메인 페이지 제목 배치하고 꾸미기

```css
h1 {
  margin: 0;
  padding: 20px 0;
  color: #00539F;
  text-shadow: 3px 3px 1px black;
}
```

>  `margin: 0;`.설정에 의해 초기 스타일링을 덮어쓰는 것으로 그 틈을 제거할 수 있다.

> `text-shadow`요소의 문자 콘텐츠에 그림자를 적용해줍니다. 네 개의 값들은 다음과 같습니다:

- 첫 번째 pixel 값은 그림자의 **수평 오프셋**을 설정합니다 — 얼마나 옆으로 이동시킬 것인지.
- 두 번째 pixel 값은 그림자의 **수직 오프셋**을 설정합니다 — 얼마나 아래로 이동시킬 것인지.
- 세 번째 pixel 값은 그림자의 **흐림 반경**을 설정합니다 — 큰 값은 더 흐릿한 그림자를 의미합니다.
- 네 번째 pixel 값은 그림자의 기본 색상을 설정합니다.



### 이미지 가운데 정렬

```css
img {
  display: block;
  margin: 0 auto;
}
```

 `margin: 0 auto` 트릭을 사용해 볼 수 있지만, 무언가 더 해야할 필요가 있다. `body` 요소는 **block level** 이다. 이것은 페이지의 공간을 차지하고, margin 과 여기에 적용된 다른 여백값을 가질 수 있다는 것을 의미한다. 반면에 이미지는 **inline** 요소 이다. 이것은 그렇지 못함을 의미한다. 따라서 이미지에 margin 을 적용하기 위해서는, `display: block;` 을 사용해 이미지에 block-level 성질을 주어야 한다.





## HTML 태그 정리

- `<head></head>`

  > 메타데이터를 담음 (제목, 스크립트, 스타일 시트)

- `<title></title>`

  > 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의함
  >
  > 텍스트만 포함할 수 있음
  >
  > \<head>태그 안에서 사용해야 함

- `<body></body>`

  >  HTML 문서의 내용을 나타냄
  >
  > 한 문서에 하나만 존재할 수 있음

- `<footer></footer>`

  > 일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담는다.

- `<article></article>`

  > 문서, 페이지, 애플리케이션, 사이트 안에서 독립적으로 구분해 재사용할 수 있는 구획
  >
  > 게시판, 블로그 글, 매거진, 뉴스 기사 등

- `<section></section>`

  > HTML문서의 독립적인 구획을 나타냄
  >
  > 딱히 적합한 의미를 가진 요소가 없는데 구획을 나눌 때 사용함

- `<aside></aside>`

  > 문서의 주요 내용과 간접적으로 연관된 부분을 나타냄
  >
  > 주로 사이드바 혹은 콜아웃 박스로 표현함

- `<p></p>`

  > 문단을 나타냄

- `<div></div>`

  > 혼자는 아무것도 표현하지 않음
  >
  > class나 id 속성으로 꾸미기 쉽도록 돕거나, 문서의 특정 구역이 다른 언어임을 표시하는 등의 용도로 사용할 수 있음
  >
  > `<article>`이나 `<nav>`등의 의미를 가진 다른 요소가 적절하지 않을 때만 사용해야 함
  >
  > **블록 요소**

- `<span></span>`

  > 혼자는 아무것도 표현하지 않음
  >
  > div와 매우 유사하게 CSS로 스타일을 적용하는 등으로 사용함
  >
  > **인라인 요소**

- `<ul></ul>`

  > 순서가 없는 정렬되지 않은 리스트 표현
  >
  > `<li>`로 목록의 항목을 나타냄

  ```html
  <ul>
      <li>first item</li>
      <li>second item
      	<ul>
              <li>item1</li>
          	<li>item2</li>
      	</ul>
      </li>
      <li>third item</li>
  </ul>
  ```

- `<ol></ol>`

  > 순서가 있는 정렬된 리스트 표현

  ```html
  <ol>
      <li>first item</li>
      <li>second item
      	<ol>
              <li>item1</li>
          	<li>item2</li>
      	</ol>
      </li>
      <li>third item</li>
  </ol>
  ```

- `<img src="~.jpg" alt="">`

  >  문서에 이미지를 넣음
  >
  > `src`속성은 필수이며 이미지의 경로를 지정함
  >
  > `alt`속성은 이미지의 텍스트 설명이며 필수는 아니지만 **접근성 차원에서 매우 유용** (스크린 리더가 `alt`의 값을 읽어 사용자에게 이미지를 설명하기 때문)
  >
  > `alt`속성은 또한 이미지를 표시할 수 없는 경우에도 이 속성 값을 대신 보여줌
  >
  > 닫는 태그 X

- `<audio></audio>`

  > 문서에 소리 콘텐츠를 포함할 때 사용
  >
  > `src`속성 또는 `<source>`요소를 사용하여 한 개 이상의 오디오 소스를 지정할 수 있음
  >
  > 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고름
  >
  > 태그 안의 컨텐츠는 오디오가 지원되지 않을 때 보여짐

- `<video></video>`

  >  영상 삽입
  >
  > 태그 안의 컨텐츠는 비디오가 지원되지 않을 때 보여짐

- `<canvas> 캔버스 내용 설명하는 대체 텍스트 </canvas>`

  > `canvas api`와 함께 사용하여 그래픽과 애니메이션을 그릴 수 있음

- `<datalist></datalist>`

  >  다른 컨트롤에서 고를 수 있는 선택지를 나타내는 여러 `<option>`요소를 담음

  ```html
  <label for="myBrowser">아래 목록에서 브라우저를 선택하세요:</label>
  <input list="browsers" id="myBrowser" name="myBrowser" />
  <datalist id="browsers">
    <option value="Chrome">
    <option value="Internet Explorer">
  </datalist>
  ```

- `<details></details>`

  > "열림" 상태일 때 내부 정보를 보여주는 위젯을 생성함
  >
  > 레이블 옆의 작은 삼각형이 돌아가면서 열림/닫힘 상태를 나타냄
  >
  > 요약이나 레이블(제목)은 `<summary>`요소를 통해 제공함, `<summay>`의 콘텐츠를 위젯의 레이블로 사용함
  >
  > `<summary>`를 사용하지 않으면 레이블이 그냥 'details'로 표현됨 (브라우저 기본 설정이 표시됨)

- `<pogress></progress>`

  > 작업의 완료 정도를 나타내고 진행 표시줄 형태임

- `<embed>`

  > 외부 컨텐츠를 나타냄

- `<nav></nav>`

  > 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획
  >
  > 메뉴, 목차 색인 등에 주로 쓰임

- `<form></form>`

  > 정보를 제출하기 위한 구획, 폼

- `<input>`

  > 사용자의 데이터를 받을 수 있는 대화형 컨트롤 생성
  >
  > `type`으로 button, checkbox, date, radio 등이 가능함
  >
  > 속성이 매우 매우 많음

- `<output>`

  > `<input>`에 대한 결과값을 나타냄

