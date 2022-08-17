# SQLite Aggregate Functions

#집계함수 #LIKE #ORDER_BY

## Aggregate function (집계 함수)

> SELECT 구문에서만 사용되는 함수
>
> 값 집합에 대한 계산을 수행하고 단일 값을 반환
>
> COUNT, AVG, MIN, MAX, SUM 등

- COUNT

  - 그룹의 항목 수를 가져옴

- AVG

  - 모든 값의 평균을 계산

- MAX

  - 그룹에 있는 모든 값의 최대값을 가져옴

- MIN

  - 그룹에 있는 모든 값의 최소값을 가져옴

- SUM

  - 모든 값의 합을 계산

  ```sql
  -- 30세 이상인 사람들의 숫자
  SELECT COUNT(*) FROM users WHERE age >= 30;
  
  -- 전체 중에 가장 작은 나이
  SELECT MIN(age) FROM users;
  
  -- 이씨 중에 가장 작은 나이
  SELECT MIN(age) FROM users WHERE last_name = '이';
  
  -- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
  SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
  
  -- 30세 이상인 사람들의 평균 나이
  SELECT AVG(age) FROM users WHERE age >= 30;
  
  -- 계좌 잔액이 가장 높은 사람
  SELECT MAX(balance), first_name FROM users;
  ```



## LIKE

> 패턴 일치를 기반으로 데이터를 조회하는 방법

- wildcards

  - % (percent sign)

    > 문자열이 존재 할수도 안할수도 있다 의미

  - _ (underscore)

    > 문자열 하나를 의미. 무조건 존재해야 한다는 의미

  - 사용 예시

    |  와일드카드패턴  |                     의미                      |
    | :--------------: | :-------------------------------------------: |
    |        2%        |                2로 시작하는 값                |
    |        %2        |                 2로 끝나는 값                 |
    |       %2%        |                2가 들어가는 값                |
    |       _2%        | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
    |       1___       |          1로 시작하고 총 4자리인 값           |
    | 2\_%\_% / 2\_\_% |        2로 시작하고 적어도 3자리인 값         |

  ```sql
  -- 지역번호가 02인 사람
  SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
  -- 준으로 끝나는 사람
  SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
  -- 중간번호가 5114
  SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';
  ```



## ORDER BY

> 조회 결과 집합을 정렬

- 특정 컬럼을 기준으로 데이터를 정렬해서 조회하기

  - ASC : 오름차순 (default)
  - DESC : 내림차순

  ```sql
  SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
  SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
  ```

  ```sql
  -- 나이 오름차순 
  SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
  
  -- 나이, 성 순으로 오름차순
  SELECT * FROM users ORDER BY age, last_name LIMIT 10;
  
  -- 계좌 잔액 순 내림차순 
  SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
  
  -- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)
  SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
  ```

  
