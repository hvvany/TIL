# Semantic tag

#html #tag

## 시맨틱 태그

> HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
>
> 단순히 div와 같은 역할이지만 의미를 지니고 있다

- **대표적인 시맨틱 태그**
  - **header** : 문서 전체나 섹션의 헤더
  - **nav** : 내비게이션
  - **aside** : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - **section** : 문서의 일반적인 구분. 컨텐츠 그룹
  - **article** : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - **footer** : 문서 마지막 부분

```html
<!-- div 사용 -->
<div>
	<div></div>
</div>
<div>
	<div></div>
<div></div>
</div>
<div></div>
```

```html
<!-- 시맨틱 태그 사용 -->
<header>
	<nav></nav>
</header>
<section>
	<article></article>
	<article></article>
</section>
<footer></footer>
```

- **시맨틱 태그를 사용해야하는 이유**
  - 검색 엔진에서 **의미 있는 정보의 그룹** 찾기 쉽다
  - 요소의 의미가 명확해져 **가독성**이 좋아진다
  - 검색 엔진 **최적화**를 위해서





## 추가 학습 내용

- 최상단 박스에서 flex의 justify로 center가 안되는 이유

  > 블럭이기 때문에 마진을 양옆에 auto로 주면 중앙에 요소들이 배치된다
  >
  > 그냥 센터를 주면 안먹힌다. direction=column 하고 align의  center를 하면 되긴 하다

- z-index

  > 사진이나 요소들의 표현되는 앞뒤 순서. 피피티에서 맨앞으로 맨뒤로 보내기 같은 역할이다.

- 반응형 이미지

  > 반응형 웹처럼 호버링시 이미지를 살짝 확대해주는 효과를 넣을 수 있다

  ```css
  .a img {
    transition: all 0.2s linear;
  }
  .a:hover img {
    transform: scale(1.4);
  }
  ```

- 이미지 자르기

  > 이미지를 자르는 방법이 여러가지가 있다 그중에서 박스를 만들어서 잘라내보자

  div로 임의의 박스를 만들고 사이즈를 정하고 css에서 overflow: hide; 를 해주면 오버되는 부분은 숨기게 된다.

  텍스트가 오버될 때 ...으로 표현할 수도 있다.

  ``` css
   .txt_post {
      overflow: hidden;
      text-overflow: ellipsis;   /* text 오버시 ... 표현--> */
    }
  ```

- top button 구현

  > 맨 위로 가는 버튼 구현

  a 태그로 이미지 같은 요소를 감싸고 a태그 안에 href="#" 을 해주면 맨 위로 간다.

- hover 할때 클자 효과

  > color 는 글자색 배경은 커서 올리면 효과 넣을 배경색이다.

  ```css
  .main-nav__link:hover {
    color: white;
    background-color: black;
  }
  ```

- 주의할점
  - ul 태그를 a로 감싸주어도 배너에서 작동이 안된다. \<li> 태그를 a로 감싸주어야 제대로 된다