# JavaScript_Basic



## 0. 자바스크립트 

- **JavaScript는 무엇인가?**

  > 크로스-플랫폼, 객체지향 스크립트 언어. 가벼운 언어이다.

  > `Array`, `Date`, `Math`와 같은 객체에 대한 표준 라이브러리, 
  >
  > 연산자(operator), 제어 구조문과 같은 언어 요소의 코어 집합을 포함

  > Core_JavaScript는 거기에 추가 객체를 보충하여 확장

- **필요성**

  > 브라우저 화면을 동적으로 만들기 위함
  >
  > 브라우저를 조작할 수 있는 유일한 언어

- **브라우저 전쟁**

  > 1차, 2차 브라우저 전쟁으로 제작사 각자 자체 자바스크립트 언어를 사용하며 충돌 발생
  >
  > 표준화 필요성 제기되어 2015년 ES6 문법이 탄생하였다

- [**JavaScript 와 Java**](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#javascript_와_java)

  > 비슷하지만 엄연히 다르다.
  >
  > 자바 스크립트는 자바보다 타입이 단순하다. 타입 검사가 엄격하지 않다.
  >
  > 자바는 빠른 실행과 type safety를 위해 설계된 만큼 프로그래밍이 까다로운 편이다.

  |                          JavaScript                          |                             Java                             |
  | :----------------------------------------------------------: | :----------------------------------------------------------: |
  | 객체 지향.<br />객체의 형 간에 차이 없음.<br /> 프로토타입 메커니즘을 통한 상속, 그리고 속성과 메서드는 어떤 객체든 동적으로 추가될 수 있음. | 클래스 기반.<br />객체는 클래스 계층구조를 통한 모든 상속과 함께 클래스와 인스턴스로 나뉨. <br />클래스와 인스턴스는 동적으로 추가된 속성이나 메소드를 가질 수 없음. |
  | 변수 자료형이 선언되지 않음(dynamic typing, loosely typed).  | 변수 자료형은 반드시 선언되어야 함(정적 형지정, static typing). |
  |              하드 디스크에 자동으로 작성 불가.               |              하드 디스크에 자동으로 작성 가능.               |

- [**JavaScript and the ECMAScript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#javascript_and_the_ecmascript_specification)

  > ECMA는 이전에 European Computer Manufacturers Association의 약자.
  >
  > 2015년에 지정된 **표준화 버전의 JavaScript**를 ECMAScript라고 한다.

  > **세미콜론** 없어도 되는 것도 표준 지정 후 바뀜. 하지만 줄 구분이 필요하면 사용해야한다.



## 1. DOM & BOM & JS_Core

- **DOM**

  > Document Object Model
  >
  > 문서를 구조화 하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리저 트리 모델

  - 브라우저에서 할 수 있는 일 : 문서(HTML) 조작
  - **파싱 ( Parsing )**
    - 브라우저가 문자열을 해석하여 DOM 트리로 만드는 과정

- **BOM**

  > Browser Object Model
  >
  > 자바스크립트가 브라우저와 소통하기 위한 모델

  - 브라우저에서 할 수 있는 일 : navigator, screen, location, frames, history...

- **JavaScript Core** (ECMAScript)

  > 프로그래밍 언어
  >
  > 브라우저(BOM)와 그 내부의 문서(DOM)을 조작하기 위해 ECMAScrilpt를 학습

  

## 2. Dom 조작

### 1. 선택한다

> **querySelector( )**
>
> **querySelectorAll( )**
>
> getElementById(id)
>
> getElementsByTagName(name)
>
> getElementsByClassName(names)

```javascript
document.querySelector(selector)
```

- 제공한 선택자와 일치하는 element 하나 선택
- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)



```javascript
document.querySelectorAll(selector)
```

- 제공한 선택자와 일치하는 여러 element를 선택
- 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
- 지정된 셀렉터에 일치하는 NodeList를 반환



### 2. 변경(조작)한다.

> innerText 
>
> innerHTML 
>
> element.style.color 
>
> setAttribute() 
>
> getAttribute() 
>
> createElement() 
>
> appendChild() ...

### 변경

```javascript
document.createElement()
```

- 작성한 태그 명의 HTML 요소를 생성하여 반환



```javascript
Element.append()
```

- 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
- 여러 개의 Node 객체, DOMString을 추가 할 수 있음
- 반환 값이 없음



```javascript
Node.appendChild()
```

- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
- 한번에 오직 하나의 Node만 추가할 수 있음
- 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동



```javascript
Node.innerText
```

- Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text, 사람이 읽을 수 있는 요소만 남김)
- 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현



```javascript
Element.innerHTML
```

- 요소(element) 내에 포함된 HTML 마크업을 반환
- [참고] XSS 공격에 취약하므로 사용 시 주의



### 삭제

```javascript
ChildNode.remove()
```

- Node가 속한 트리에서 해당 Node를 제거



```javascript
Node.removeChild()
```

- DOM에서 자식 Node를 제거하고 제거된 Node를 반환
- Node는 인자로 들어가는 자식 Node의 부모 Node



### 속성

```javascript
Element.setAttribute(name, value)
```

- 지정된 요소의 값을 설정
- 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가



```javascript
Element.getAttribute(attributeName)
```

- 해당 요소의 지정된 값(문자열)을 반환

- 인자(attributeName)는 값을 얻고자 하는 속성의 이름



## 3. 문법과 자료형

- **기본**

  - 작성

    ```javascript
    var 갑을 = "병정"
    
    var Früh = "foobar"; var 갑을 = "병정";
    ```

    > 한 줄에 여러 명령문을 적으려면 세미콜론 필수.

  - 주석

    ```javascript
    // 한 줄 주석
    
    /* 이건 더 긴,
     * 여러 줄 주석입니다.
     */
    
    /* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
    ```

- **선언**

  - **var**

    > 

  - **let**

  - **const**