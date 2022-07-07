# Markdown & Git





## Markdown

텍스트 기반 가벼운 마크업 언어

서식, 스타일링을 거의 할 수 없다. 매우 단순한 텍스트 문법으로 내용을 작성 => 다양한 환경에서 변환하여 보여줄 수  있다.



### Markdown 활용

1. #### README.md

   GitHub 등에서 파일명이 README.md 인 것을 모두 볼 수 있다.

2. #### 기술 블로그

   Jakyll, Gatsby, Hugo, Hexo  등을 통해 작성된 마크다운을 HTML, CSS, JS파일 등으로 변환하고  GitHub pages 기능으로 호스팅

3. #### 기타

   Notion 같은 필기 sw에서도 많이 사용



### Markdown 문법

1. #### Heading

   ```markdown
   # head
   ```

   #의 개수에 따라 수준이 달리진다. -> html의 <h1>,</h1> 태그와 같은 역할

   | Markdown | HTML          |
   | -------- | ------------- |
   | # 제목   | <h1>제목</h1> |
   | ## 제목  | <h2>제목</h2> |
   | ### 제목 | <h3>제목</h3> |

   ```html
   <h1>
       "대빵 큰 메인 제목은 h1"
   </h1>
   ```

   > 꿀팁
   >
   > "ctrl + 숫자" 를 통해 수준 조절 가능
   >
   > 
   >
   > 주의할점
   >
   > Heading은 제목의 역할로 개요 또는 목차에서 중요한 역할. 단순히 글자 키우기용으로 사용 금지

   

2. #### List

   - ##### ol (ordered list)
   
   ```markdown
   1. 첫번째
   2. 두번째
   ```
   
   - ##### ul (unordered list)
   
   ```markdown
   - hypen_첫번째
   - hypen_두번째
   * asterisk_첫번째
   * asterisk_두번째
   ```
   
   > 꿀팁
   >
   > "Tab"으로 하위 항목으로 이동 가능
   >
   > "Shift + Tab"으로 상위 항목으로 이동 가능
   >
   > 
   >
   > 주의할점
   >
   > 띄어 쓰기 해야한다



3. #### Fenced Code block

   ```markdown
   ```python
   ```markdown
   ```

   코드를 적어줄 때 backtic(`) 기호를 세 번 입력하고 원하는 언어를 입력한다

   박스가 생성되며 그 안에서는 특정 언어에 대한 Syntax hilighting 기능이 적용된다

   

4. #### Inline Code Block

   ```markdown
   `이건 마치 형광펜 같은 효과`
   ```

   `backtick` 으로 둘러 싸면 음영처리가 된다



5. #### Link

   ```markdown
   [링크 이름](url주소)
   ```

   대괄호 안에 글자를 적어주고 소괄호 안에 url 주소를 적어준다



6. #### Image

   ```markdown
   ![이미지 이름](이미지 url 혹은 디렉토리)
   ```

   > 꿀팁
   >
   > 보통 파일을 끌어다가 놓으면 자동으로 코드 형성
   >
   > 
   >
   > 주의할점
   >
   > C: 경로에 있으면 외부 공유시 안보일 수 있다.
   >
   > **절대경로** => 현재 md파일과 **다른** 디렉토리 (최상위 디렉토리(C:\)를 기준으로 작성된 절대적 경로)
   >
   > **상대경로** => 현재 md파일과 **같은** 디렉토리 (현재 디렉토리를 기준으로 상대적인 위치의 경로)



7. ####  Blockquotes

   ```markdown
   > 인용문
   ```

   > 앞에 바가 생기는 효과 적용된다

   

8. #### Table

   ```markdown
   ctrl + t  -> 단축키
   ```

   | 항목1 | 항목2 | 항목3 | 항목4 |
   | ----- | ----- | ----- | ----- |

   

9. #### Text

   ```markdown
   **굵게**             => ctrl + b
   *기울임*              => ctrl + i
   ~~취소선~~
   ***굵게 기울임***
   ```

   

10. #### Horizontal

    ```markdown
    **********        => 3개 이상의 *
    -----------       => 3개 이상의 -
    ____________      => 3개 이상의 _
    ```

    



### 문서작성능력 중요

자신이 경험한 사용법을 문서화해서 팀 내에 전파할 수있는 능력이 있어야 한다

> #### 참고
>
> ###### 개발자 수준 분류
>
> - 레벨0
>   - 이미 사용하고 있는 개발도구의 사용법을 알려줘도 잘 못 씀
>
> - 레벨1
>   - 알려주는 만큼만 할 수 있음
> - 레벨2
>   - 개발도구 레퍼런스를 보고 사용법 스스로 익힐 수 있음
>   - 자신이 경험한 사용법을 문서화해서 전파할 수 있음
>
> - 레벨3
>   - 여러 개발도구 비교 분석 및 선택가능
>   - 공식 레퍼런스 수정하여 기여 할 수 있음
> - 레벨4
>   - 개발도구의 문제를 소스 코드 수정하여  Fork/패치해서 사용할 수있음



구글은 글쓰기 코스도 제공

[Technical Writing Course](https://developers.google.com/tech-writing)

.

.

.

***"개발자는 글을 쓰는 사람이다"***

.

.

.



## Git



### git 정의

분산 버전 관리 시스템



### 버전관리

#### 분산버전관리시스템( DVCS)

과거에는 중앙집중식버전관리시스템 사용 => 서버에 모든 파일과 버전 관리

DVCS 장점 => 원격 저장소를 통해 협업하고, 모든 히스토리를 클라이언트들이 공유

#### 버전관리 장점

이전 버전 필요 시 정리가 잘 되어있어 찾아보기 쉽다

수정된 항목만 업데이트 되기 때문에 전체 파일의 용량을 줄일 수 있다



### GUI & CLI

#### 	GUI

​		Graphic User Interface

#### 	CLI

​		Command Line Interface



### 디렉토리 관리

 - **pwd** (print working directory)

   현재 디렉토리 출력

 - **cd** (chage directory)

   디렉토리 이동

   > cd ..   => 현재 디렉토리의 바로 위 상위 디렉토리 이동

- **ls** (list)

  목록

- **mkdir** (make directory)

  디렉토리 생성 (폴더 생성)

  > 폴더 이름이 '새 폴더' 일 때 
  >
  > cd 새\ 폴더    => 이렇게 입력해 줘야 한다. 따라서 보통 영어로 작성 및 언더바_사용하여 작성을 추천

- **touch**

  파일 생성

- **rm** (remove)

  파일 삭제

- **rm -r**

  폴더 삭제

- **clear**

  터미널 창 새로 열기

> 꿀팁
>
> 파일이나 폴더 이름(디렉토리) 입력 시 첫 몇글자 입력 후 Tab키를 눌러주면 자동으로 완성시켜준다. 비슷한 이름이 많으면 선택지를 준다.



### 기본 명령어

- #### 저장소 처음 만들때

  git init

  > 최초 실행시 id 및 이메일 주소 입력 해주기    => "마 니 눈데?!"
  >
  > git config --global user.name "hvvany"
  >
  > git config --global user.email "kjunhwan1998@gmail.com"

- #### 버전을 기록할 때

  git add 0000.txt

  git commit -m '커밋 메시지'

- #### 상태 확인할 때

  git status      => Staging Area

  git log            => Repository

  > git log -1                      => 바로 직전 버전 1개 보여줘
  >
  > git log --oneline          => 한 줄로 보여줘
  >
  > git log -2 --oneline     => 바로 직전 버전 2개 한 줄로 보여줘



> ### Working Directory
>
> git add 000.txt
>
> ### Staging Area              => git status
>
> git commit -m
>
> ### Repository                 => git log



> #### 참고
>
> Working Directory 에서 커밋 할 파일만 Staging Area에  add 한 후 commit 진행



> #### ※ 주의할 점
>
> .git 폴더가 파일 관리 하고자 하는 디렉토리의 위치가 아닌 상위 위치에 생성될 경우 상위 디렉토리의 모든 파일을 git이 관리하게 된다
>
> git의 위치를 잘 확인하자 => windows 경우 숨김 폴더 보기 하면 보인다  or cd .. 으로 상위 디렉토리로 한 단계씩 나가보며 (master) 뜨는지 확인

