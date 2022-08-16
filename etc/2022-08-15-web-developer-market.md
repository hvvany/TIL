# 웹개발자 채용 시장 분석

#개발자 #진로 #채용

### [채용 공고 Notion 정리](https://subsequent-swift-e1a.notion.site/46f9cd9e3a7a430d8d1eff7f3d01c78d?v=982e5e062b6842e585fcf8ad243c2f84)



1. ## 요구하는 기술 스택

   - ### 프론트엔드

   > **HTML / CSS / JavaScript / TypeScript / React / Next.js / Redux.js** / Node.js / Vue.js / SCSS / etc...

   - ### 백엔드

   > **Java / Spring / JavaScript / TypeScript / Node.js / NoSQL** / GraphQL / mongoDB / dynamoDB / etc...

   - ### 용어 정리

     - **라이브러리 vs 프레임워크**

       > **내가 코드를 컨트롤** 하는지 **vs** 누군가의 **규칙을 따라 코딩**하는 건지

       > 라이브러리 : 내가 필요해서 가져다가 쓰고 다른 걸로 쉽게 교체 가능
       >
       > 프레임워크 : 정해진 규칙에 따라서 파일을 작성해주어야 한다.

       > **라이브러리** 예시 : jQuery, React.js, Vue.js  => 리액트와 뷰는 컴포넌트를 넣어주기도 해야해서 논란이 많지만 라이브러리인지 프레임 워크인지에 대한 구분은 중요하지 않다. 개념만 알아두자.
       >
       > **프레임워크** 예시 : django

     - **JavaScript vs TypeScript**

       > [TypeScript 자습서](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)

       >  JavaScript는 현재 프론트엔드에서 매우 중요한 언어로 사용이 된다. 하지만 개발 당시 임시로 사용하기 위해 단 10일 만에 만들어진 언어로써 부실한 부분이 많다. 예를 들어 1 + True 는 개발자가 의도하지 않은 계산일 확률이 높은데 **<u>JavaScript는 오류를 띄우지 않고 어떻게든 2로 계산을 해버린다.</u>** 또한 문자열과 정수형의 곱은 잘못된 수식이지만 JavaScript는 어떻게든 실행을 하다가 런타임 에러가 발생한다. 

       > 이처럼 잘못된 타입은 오류 창을 띄워 개발자가 인식할 수 있도록 보완한게 TypeScript이다. **<u>타입을 명시하여 의도하지 않은 잘못된 수식을 알려준다.</u>**

     - **React / React.js / React Native 차이**

       > [React 자습서](https://ko.reactjs.org/tutorial/tutorial.html#what-is-react)

       > 우리가 보는 웹 화면 (ui) 를 만들 때 기본이 `HTML`과 `CSS`, 그리고 `JavaScript`이다.
       >
       > 딱 저 위의 세개로 화면을 구현하는 것은 생각보다 힘들다.
       >
       > React는 UI 요소 구현을 좀 더 편하게 할 수 있도록 돕기 위해 만들어진 JavaScript 라이브러리여서, 프론트엔드를 한다고 하면 보통 React를 많이 사용한다.
       >
       > 간단히 설명 하자면 **사용자 정의 태그를 통해 하위 태그를 묶어서 숨길 수 있게 된다**!!!

       > React 와 React.js 의 차이는 사실 똑같은 React인데 뒤에 그냥 자바스크립트임을 뜻하는 .js를 붙이고 떼고인것 뿐이다. React Native와 구분하기 위한 것 같다. 결국 같은 것을 의미한다.

       > 이처럼 <u>**React**</u>가 `웹` 화면 개발에 사용된다면, 
       >
       > <u>**React Native**</u>는 `휴대폰 어플리케이션` 개발에 사용된다.

       > **React Native** 이전에는 안드로이드와 아이폰 각각 다른 프로그래밍 언어를 사용해 개발을 했어야 하는데, React Native는 이 언어 하나로 **<u>아이폰과 안드로이드에서 함께 사용</u>**할 수 있는 어플을 만들 수 있게 해준다.
       >
       > **Spring boot**는 서버를 만드는 때에 많이 쓰는 프레임워크이다.
       >
       > 사용자가 사용하는 웹 화면 (프론트엔드)가 아니라, 백엔드를 만들때 사용하는 언어로 굳이 spring boot 뿐만이 아니라, kotlin, python, c, java, 심지어 javascript 로도 서버는 만들 수 있다. 

     - Next.js
     
       -  비슷한 프레임워크들
         - Gatsby : 웹 사이트를 게시하기 전에 페이지를 미리 생성
         - Remix : 사용자가 요청할 때 서버 측에서 모든 코드를 실행
       - Next.js는 위의 두 가지를 모두 할 수 있다.
       - React 기반으로 활용
       - 사용자가 로딩중을 보지 않고 기다리는 시간에 미리 웹 페이지를 볼 수 있게 하고 아니면 한 번에 로딩이 완료된 웹 사이트를 볼 수 있게 하는 기술? 이라고 정리할 수 있을 것 같다.
     
     - Redux.js
     
       - React 하면 사용하는 라이브러리
     
       - 사용하는 이유
     
         1. props 문법 귀찮을 때 쓴다
     
            > html에서 변수를 사용할 때 상위 component에 변수를 하위 component 내부에서 사용하고자 할 때 그냥 못쓰고 props 라는 것을 해주어야 한다.
     
         2. state 변경 관리할 때 쓴다
     
            > 만약 여러 component에서 사용한 변수가 특정 동작 시 값이 변하도록 구현하였는데 오류 발생시 오류를 찾기 위해 수많은 component를 찾으며 디버깅 해야한다. 이 때 Redux를 사용하면 store.js에다가 모든 동작을 if문으로 모아놓고 component들은 요청만 하게 구현한다. 이러면 버그 발생시 그 원인은 store.js 내부에 있으므로 확인해야 할 범위가 확 줄게 된다.
     
     - Node.js
     
       - 2009년에 Ryan Dahi가 기존의 프레임워크의 단점을 보완하여 만든 프레임워크.
       - 기존에는 백엔드는 Java, PHP, Python 같은 언어로만 가능했지만 JavaScript 언어로 프론트엔드, 백엔드 모두 가능하게 해준 프레임워크이다.
     
     - NoSQL
     
       >  not only SQL 의 약자로 기존의 SQL방식과는 다르게 Key Value DB, Graph DB, Document DB등 다양한 DB 구조를 말한다. 어느 하나를 말하는 것은 아니다. 그럼 SQL보다 좋은가? 꼭 그렇지는 않다.
       >
       > 보통 일반적인 프로젝트라면 SQL로 해보고 특별한 문제에 대응하거나 하기 위해 사용하는 방식이다.
     
       

2. ## 우대해주는 기술 및 경험

   > Git, AWS, Slack, SSR(서버 사이드 렌더링), Flow, 기술블로그, 몰입력, 자기주도적, 문제 해결 능력, 빠른 실행력

   

3. ## 채용 과정 및 코딩테스트 유무

   > 코테 유무는 대기업은 보통 있고 it대기업 및 스타트업 전체로 보면 반반 정도 되는 것 같다.

   > 컬쳐핏 이라고 기업 문화와 잘 맞는지 보는 면접이 많다. 단순히 코딩 실력만 좋은 것 보다 회사의 분위기와 비젼에 부합하는지가 중요한 것 같다. 그리고 보통 길면 6개월 까지 수습기간을 거치는 것을 보면 기업 문화에 잘 맞는지를 중요하게 본다는 것을 알 수 있다.
