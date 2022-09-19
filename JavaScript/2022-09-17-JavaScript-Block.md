# JavaScript 구성요소

#조건문 #반복문 #함수 #이벤트



## 1. 조건문

- **if ... else 문**

  ```javascript
  /* persudo code */
  if (조건) {
    만약 조건(condition)이 참일 경우 실행할 코드
  } else {
    대신 실행할 다른 코드
  }
  ```

  ```javascript
  /* 실제 코드 */
  let shoppingDone = false;
  let childsAllowance;
  
  if (shoppingDone === true) {
    childsAllowance = 10;
  } else {
    childsAllowance = 5;
  }
  ```

- **else if 문**

  ```javascript
  const select = document.querySelector('select');
  const para = document.querySelector('p');
  
  select.addEventListener('change', setWeather);
  
  function setWeather() {
    const choice = select.value;
  
    if (choice === 'sunny') {
      para.textContent = 'a';
    } else if (choice === 'rainy') {
      para.textContent = 'b';
    } else {
      para.textContent = '';
    }
  }
  ```

  

## 2. 반복문

- **for문**

  ```javascript
  for (초기화식; 종료 조건; 증감식) {
    // 실행할 코드
  }
  ```

  ```javascript
  const cats = ['Bill', 'Jeff', 'Pete', 'Biggles', 'Jasmin'];
  let info = 'My cats are called ';
  const para = document.querySelector('p');
  
  for (let i = 0; i < cats.length; i++) {
    info += cats[i] + ', ';
  }
  
  para.textContent = info;
  ```

- **break**

  ```javascript
   for (let i = 0; i < contacts.length; i++) {
      let splitContact = contacts[i].split(':');
      if (splitContact[0] === searchName) {
        para.textContent = splitContact[0] + '\'s number is ' + splitContact[1] + '.';
        break;
      } else {
        para.textContent = 'Contact not found.';
      }
    }
  ```

- **continue**

  ```javascript
  let num = input.value;
  
  for (let i = 1; i <= num; i++) {
    let sqRoot = Math.sqrt(i);
    if (Math.floor(sqRoot) !== sqRoot) {
      continue;
    }
  
    para.textContent += i + ' ';
  }
  ```

- **while문**

  ```javascript
  초기화식
  while (종료 조건) {
    // 실행할 코드
  
    증감식
  }
  ```

  ```javascript
  let i = 0;
  
  while (i < cats.length) {
    if (i === cats.length - 1) {
      info += 'and ' + cats[i] + '.';
    } else {
      info += cats[i] + ', ';
    }
  
    i++;
  }
  ```

  

- **do ... while**

  ```javascript
  let i = 0;
  
  do {
    if (i === cats.length - 1) {
      info += 'and ' + cats[i] + '.';
    } else {
      info += cats[i] + ', ';
    }
  
    i++;
  } while (i < cats.length);
  ```

  





## 3. 함수

- **함수 호출**

  ```javascript
  function myFunction() {
    alert('hello');
  }
  
  myFunction()
  // calls the function once
  ```

- **익명 함수**

  ```javascript
  function() {
    alert('hello');
  }
  ```

- **함수 매개변수** 

  - 매개 변수 <u>필요 없는</u> 함수

    ```javascript
    var myNumber = Math.random();
    ```

  - 매개 변수 <u>필요한</u> 함수

    ```javascript
    var myText = 'I am a string';
    var newString = myText.replace('string', 'sausage');
    ```

    

- **함수 스코프**

  > 다른 함수의 내부나 외부 함수의 코드가 접근할 수 없는 그들만의 구획에 갇혀 있다

  > 함수 바깥에 선언된 가장 상위 레벨의 스코프를 '**전역 스코프**(global scope)' 라고 부릅니다.전역 스코프 내에 정의된 값들은 어느 코드든 접근이 가능합니다.

  

## 4. 이벤트

- **onclick ** 프로퍼티

  ```javascript
  const btn = document.querySelector('button');
  
  btn.onclick = function() {
    const rndCol = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
    document.body.style.backgroundColor = rndCol;
  }
  ```

  

[**다양한 이벤트 목록**](https://developer.mozilla.org/ko/docs/Web/Events)
