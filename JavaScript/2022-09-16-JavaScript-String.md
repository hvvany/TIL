# JavaScript_Grammar

#변수 #선언 #자료형 #문자열



## 1. 문법과 자료형

- **기본**

  - 작성

    ```javascript
    var 갑을 = "병정"
    
    var Früh = "foobar"; var 갑을 = "병정";
    ```

    한 줄에 여러 명령문을 적으려면 세미콜론 필수.

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

    변수를 `선언` 및 동시에 `초기화` 진행

  - **let**

    `블록 스코프` 지역 변수를 `선언` 및 동시에 `초기화` 진행
  
  - **const**
  
    `블록 스코프` `읽기 전용 상수`를 선언
  
- **변수**

  - 애플리케이션에서 값에 `상징적인 이름`으로 변수를 사용. 변수명은 [식별자(identifiers)](https://developer.mozilla.org/ko/docs/Glossary/Identifier)라고 불리며 특정 규칙을 따른다.

  - JavaScript 식별자는 문자, 밑줄 (`_`) 혹은 달러 기호 (`$`)로 시작해야 하는 반면 이후는 숫자 (`0`–`9`) 일 수도 있습니다.
  - JavaScript가 대소문자를 구분하기에, 문자는 "`A`"부터 "`Z`" (대문자)와 "`a`"부터 "`z`" (소문자)까지 모두 포함합니다.

- **변수 선언**

  - `var`은 ES6 이후로 이제 안쓴다. 호이스팅이 일어난다. ( 호이스팅은 휘감아 올리다 라는 의미의 단어로 선언도 안했는데 값을 주면 사용이 가능해져서 문제가 있다.)

  - `let`과 `const`로 변수를 선언한다. `let`은 계속해서 수정 가능한 변수 선언. `const`는 변경 불가능 상수 선언

  - 선언되지 않은 변수에 접근을 시도하면 `ReferenceError` 발생

    ```javascript
    var a;
    console.log('a 값은 ' + a); // a 값은 undefined
    
    console.log('b 값은 ' + b); // b 값은 undefined
    var b;
    
    let x;
    console.log('x 값은 ' + x); // x 값은 undefined
    
    console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
    let y;
    ```



## 2. 기본적인 연산 _ 숫자와 연산자

- **숫자의 종류**

  > integer
  >
  > float
  >
  > double
  >
  > 2진수
  >
  > 8진수
  >
  > 16진수

- **자바 스크립트에서 숫자를 모두 구분??**

  > Numbers 하나로 모든 숫자 데이터 타입 표현

- **산술 연산자**

  | Operator | Name           | Purpose |
  | -------- | -------------- | ------- |
  | +        | Addition       | 더하기  |
  | -        | Subtraction    | 빼기    |
  | *        | Multiplication | 곱하기  |
  | /        | Division       | 나누기  |
  | %        | Remainder      | 나머지  |

- **증감 연산자**

  | Operator | Name      | Purpose              |
  | -------- | --------- | -------------------- |
  | ++       | self += 1 | 자기 자신에 1 더하기 |
  | --       | self -= 1 | 자기 자신에 1 빼기   |

- **할당 연산자**

  | Operator | Name   | Purpose            | Example | Shortcut for |
  | -------- | ------ | ------------------ | ------- | ------------ |
  | +=       | 더하기 | 자기 자신에 더하기 | x += 4; | x = x + 4;   |
  | -=       | 빼기   | 자기 자신에 빼기   | x -= 3; | x = x - 3;   |
  | *=       | 곱하기 | 자기 자신에 곱하기 | x *= 3; | x = x * 3;   |
  | /=       | 나누기 | 자기 자신에 나누기 | x /= 5; | x = x / 5;   |

- **비교 연산자**

  | Operator | Name                     | Purpose     | Example     |
  | -------- | ------------------------ | ----------- | ----------- |
  | ===      | Strict equality          | 같은지 비교 | 5 === 2 + 4 |
  | !==      | Strict-non-equality      | 다른지 비교 | 5 !== 2 + 3 |
  | <        | Less than                | 미만        | 10 < 6      |
  | >        | Greater than             | 초과        | 10 > 20     |
  | <=       | Less than or equal to    | 이하        | 3 <= 2      |
  | >=       | Greater than or equal to | 이상        | 5 >= 4      |

  



## 3. 문자열 다루기 - 문자열

- **문자열 만들기**

  ```javascript
  var string = 'The revolution will not be televised.';
  string;
  ```

  ```javascript
  var badString = string;
  badString;
  ```
  
  문자열을 string 변수에 먼저 선언 후 다시 badString에 넣어주면 같은 값을 가지게 된다.

- **따옴표 vs 쌍따옴표**

  따옴표와 쌍따옴표 모두 허용 된다.

  ```javascript
  var sglDbl = 'Would you eat a "fish supper"?';
  var dblSgl = "I'm feeling blue.";
  ```

  내부에 따옴표를 쓸 때는 감싸는 따옴표와 다르면 상관 없다.

  ```javascript
  var bigmouth = 'I\'ve got no right to take my place...';
  ```

  같은 따옴표를 쓰게 된다면 역슬래시로 문자 구분을 해주면 된다.

- **문자열 연결하기**

  더하기로 하면 된다

  ```javascript
  var one = 'Hello, ';
  var two = 'how are you?';
  var joined = one + two;
  ```

- **숫자 vs 문자열**

  ```javascript
  'Front ' + 242;
  ```

  => Front 242 

  이 경우에는 숫자를 자동으로 문자열로 변환시켜 문자열로 연결시킨다.

  - 문자열 -> 숫자

  ```javascript
  var myString = '123';            /* STRING */
  var myNum = Number(myString);    /* NUMBER */
  typeof myNum;
  ```

  => 123 은 number 데이터타입

  - 숫자 -> 문자열

  ```javascript
  var myNum = 123;
  var myString = myNum.toString();
  typeof myString;
  ```

  => 123 은 string 데이터타입

- **문자열 길이 찾기**

  ```javascript
  var browserType = 'mozilla';
  browserType.length;
  ```

- **특정 문자열 찾기**

  ```javascript
  browserType[0];
  ```

- **마지막 문자 찾기**

  ```javascript
  browserType[browserType.length - 1];
  ```

- **특정 문자가 포함된 위치 찾기**

  ```javascript
  browserType.indexOf('zilla');
  /* mozilla =>  2  */
  browserType.indexOf('vanilla');
  /* mozilla =>  -1     해당하는 문자열이 없으면 -1 */
  ```

- **슬라이싱**

  ```javascript
  browserType.slice(0, 3);
  /* mozilla =>  moz */
  browserType.slice(2);
  /* mozilla =>  zilla */
  ```

- **대소문자 변환**

  ```javascript
  var radData = 'My NaMe Is MuD';
  radData.toLowerCase();
  radData.toUpperCase();
  ```




## 4. 배열

> 배열이란 일반적으로 "**리스트같은 객체(list-like objects)**"라고 기술됩니다.

- **배열 만들기**

  ```javascript
  var shopping = ['bread', 'milk', 'cheese', 'hummus', 'noodles'];
  var sequence = [1, 1, 2, 3, 5, 8, 13];
  var random = ['tree', 795, [0, 1, 2]];
  ```

- **인덱스 접근**

  ```javascript
  shopping[0];
  // returns "bread"
  
  shopping[0] = 'tahini';
  shopping;
  // shopping will now return [ "tahini", "milk", "cheese", "hummus", "noodles" ]
  ```

- **배열의 갯수 알아내기 (lenght)**

  ```javascript
  sequence.length;
  // should return 7
  ```

- **배열 원소 추가 제거 (push, pop)**

  ```javascript
  var myArray = ['Birmingham', 'Leeds', 'Carlisle'];
  myArray.push('Cardiff');
  myArray.push('Bradford', 'Brighton');
  /* ['Birmingham', 'Leeds', 'Carlisle','Cardiff','Bradford', 'Brighton'] */
  
  myArray.pop();
  /* ['Birmingham', 'Leeds', 'Carlisle','Cardiff','Bradford'] */
  ```

- **배열 원소 추가 제거 (unshift, shift)**

  ```javascript
  myArray.unshift('Edinburgh');
  
  var removedItem = myArray.shift();
  ```

  
