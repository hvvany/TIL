# Database

#db #sql #sqlite #rdb 

1. ## Database

   - 개념

     > - 체계화된 데이터 모임
     >
     > - 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
     >
     > - 자료를 구조화하여 기억시켜 놓은 자료의 집합체

   - 장점

     > - 데이터 중복 최소화
     > - 데이터 무결성
     > - 데이터 일관성
     > - 데이터 독립성
     > - 데이터 표준화
     > - 데이터 보안 유지

     

2. ## RDB

   - 관계형 데이터베이스 (RDB, Relational Database)

     - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

     - 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스

       | 고유 번호 |  이름  | 주소 | 나이 |
       | :-------: | :----: | :--: | :--: |
       |     1     | 홍길동 | 제주 |  20  |
       |     2     | 김길동 | 서울 |  30  |
       |     3     | 박길동 | 독도 |  40  |

   - 스키마 (schema)

     - 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

       > 쉽게 말해 분류 기준과 그 데이터타입을 보여줌

       | column  | datatype |
       | :-----: | :------: |
       |   id    |   INT    |
       |  name   |   TEXT   |
       | address |   TEXT   |
       |   age   |   INT    |

   - 테이블 (table)

     - 열(column, 필드)과 행(row,record)의 모델을 사용해 조직된 데이터 요소들의 집합

       |  id  |  name  | address | age  |
       | :--: | :----: | :-----: | :--: |
       |  1   | 홍길동 |  제주   |  20  |
       |  2   | 김길동 |  서울   |  30  |
       |  3   | 박길동 |  독도   |  40  |

   - 열(column) : 각 열에 고유한 데이터 형식 지정

     - 위의 예시에서는 name이란 필드에 고객의 이름(TEXT) 정보가 저장

   - 행(row) : 실제 데이터가 저장되는 형태

     - 위의 예시에서는 총 3명의 고객정보가 저장되어 있음. 레코드가 3개

   - 기본키 (Primary Key) : 각 행의 고유값

   

3. ## RDBMS

   - 관계형 데이터베이스 관리 시스템 (RDBMS)

     > MySQL, SQLite, PostgreSQL, ORACLE, SQL Sever 등

   - SQLite

     - 서버 형태가 아닌 파일 형식으로 응용프로그램에 넣어서 사용하는 **비교적 가벼운 DB**
     - 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스
     - 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트여서 자유롭게 사용가능

   - SQLite Data Type

     1. NULL

     2. INTEGER

        > 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호가 있는 정수

     3. REAL

        > 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값

     4. TEXT

     5. BLOB

        > 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

4. ## SQL

   - SQL (Structured Query Language)

     > 관계형 데이터베이스 관리시스템의 **데이터 관리를 위해 설계된 프로그래밍 언어**

     |                           분류                           |                            개념                             |                    예시                     |
     | :------------------------------------------------------: | :---------------------------------------------------------: | :-----------------------------------------: |
     |  DDL - 데이터 정의 언어<br />(Data Definition Language)  |    관계형 데이터베이스 구조를<br />정의하기 위한 명령어     |         CREATE<br />DROP<br />ALTER         |
     | DML - 데이터 조작 언어<br />(Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을<br />하기 위한 명령어  | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
     |   DCL - 데이터 제어 언어<br />(Data Control Language)    | 데이터베이스 사용자의 권한 제어를<br />위해 사용하는 명령어 | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |

   - SQL Keywords - Data  Manipulation Language

     - INSERT : 새로운 데이터 삽입
     - SELECT : 저장되어있는 데이터 조회
     - UPDATE : 저장되어있는 데이터 갱신
     - DELETE : 저장되어있는 데이터 삭제

   

5. ## 테이블 생성 및 삭제

   ### 데이터베이스 생성하기

   ```bash
   $ sqlite3 tutorial.sqlite3
   sqlite> .datebase
   ```

   > `.`은 sqlite에서 활용되는 명령어

   
   
   ### CSV로 테이블 만들기
   
   - csv 파일을  table로 만들기
   
     ```sql
     .mode csv
     .import helodb.csv examples
     .tables
     -- examples
     ```
   
     > csv 파일이란?
     >
     > **Comma** Separated Variables 약자이다. 콤마로 구분한 텍스트 데이터 및 텍스트 파일
   
   - SELECT (만들어진 테이블 확인)
   
     ```sql
     SELECT * FROM examples;
     -- 1,"길동","홍",600,"충청도",010-0000-0000
     ```
   
   - 터미널 view 변경하기 (깔끔하게 보인다)
   
     ```sql
     .headers on
     .mode column
     
     SELECT * FROM examples;
     -- id first_name last_name age country phone
     -- -- ---------- --------- --- ------- ----------
     -- 1  길동          홍       600   충청도   010-0000-0000
     ```
   
   
   
   ### CREATE으로 테이블 만들기
   
   -  CREATE TABLE
   
     > 테이블 생성
   
     ```sql
     CREATE TABLE classmates (
     id INTEGER PRIMARY KEY,
     name TEXT
     );
     
     .tables
     -- classmates  examples
     ```
   
   - schema 조회
   
     ```sql
     .schema classmates
     -- CREATE TABLE classmates (
     -- id INTEGER PRIMARY KEY,
     -- name TEXT
     -- );
     ```
   
   - DROP TABLE
   
     > 테이블 제거
   
     ```sql
     DROP TABLE classmates;
     
     .tables
     -- examples
     ```
   
   - 필드 제약 조건
   
     - NOT NULL : null 값 입력 금지
     - UNIQUE : 중복 값 입력 금지 (null 값은 중복 입력 가능)
     - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
     - FOREIGN KEY : 외래키. 다른 테이블의 Key
     - CHECK : 조건으로 설정된 값만 입력 허용
     - DEFAULT : 기본 설정 값
   
     ```sql
     CREATE TABLE students (
     	id INTEGER PRIMARY KEY,
     	name TEXT NOT NULL,
     	age INTEGER DEFAULT 1 CHECK (0 < age)
     );
     ```
   
   
   
   
   
   6. ## CRUD
   
      ### CREATE
   
      - INSERT
   
        - 테이블에 단일 행 삽입
   
          ```sql
          INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
          ```
   
        - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
   
          ```sql
          INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
          ```
   
        > 전체 컬럼 수가 4개 인데 3개만 입력할 경우에는 단일행 삽입 방법으로 컬럼을 정해서 넣어준다.
        >
        > 값의 개수가 전체 컬럼 개수와 같다면 별도로 컬럼 지정하지 않아도 입력이 된다.
   
      - rowid
   
        > SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼
   
        ```sql
        SELECT rowid, name FROM classmates;
        rowid  name
        -----  ----
        1      홍길동
        2      김철수
        3      이호영
        4      박민희
        5      최혜영
        ```
   
      - AUTOINCREMENT
   
        > id를 처음에 테이블을 생성할 때 AUTOINCREMENT를 함께 사용하면 id가 자동으로 지정이된다.
   
         ```sql
         CREATE TABLE members(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL
         );
         ```
   
      - 다양한 데이터 한 번에 INSERT 하기
   
        ```sql
        INSERT INTO classmates VALUES
        ('홍길동', 30, '서울'),
        ('김철수', 30, '제주'),
        ('이호영', 26, '인천'),
        ('박민희', 29, '대구'),
        ('최혜영', 28, '전주');
        ```
   
      
   
      ### READ
   
      - SELECT
   
        - 테이블에서 데이터를 조회
   
        - SELECT 문은 SQLite에서  가장 기본이 되는 문법이며 다양한 절과 함께 사용
   
          > ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...
   
      - LIMIT
   
        - 쿼리에서 반환되는 행 수를 제한
        - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
   
      - WHERE
   
        - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
   
      - SELECT DISTINCT
   
        - 조회 결과에서 중복 행을 제거
        - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성
   
        ```sql
        SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
        ```
   
        ```sql
        SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
        ```
   
        > OFFSET은 건너 뛰는 개수이므로 0부터 시작
        >
        > OFFSET = 2, LIMIT = 1 이면 3번째 레코드가 지정된다
   
        ```sql
        SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
        ```
   
        ```sql
        SELECT * FROM classmates WHERE address='서울';
        ```
   
      - DISTINCT
   
        - 중복 없이 조회하는 방법
   
        ```sql
        SELECT DISTINCT 컬럼 FROM 테이블이름;
        ```
   
        ```sql
        SELECT DISTINCT age FROM classmates;
        -- age
        -- ---
        -- 30
        -- 26
        -- 29
        -- 28
        ```
   
   7. ## 기타
   
      - **데이터의 레코드 개수 보다 더 많은 수를 조회하면 에러??**
   
        > 존재하는 데이터 만큼만 보여주며 에러는 나지 않는다
   
        ```sql
        SELECT rowid, name FROM classmates LIMIT 100;
        -- 데이터는 5개만 있으면 5개만 가져온다
        -- rowid name
        -- ----- ----
        -- 1     홍길동
        -- 2     김철수
        -- 3     이호영
        -- 4     박민희
        -- 5     주세환
        ```
   
        
   
      - **데이터 제거 후 새로 만들면 id값은??**
      
        - rowid를 SELECT에서 사용할 경우에는 레코드에 고유한 id값을 임의의 순서대로 부여하는 것이므로 제거한 레코드의 rowid 값은 새로운 레코드에 부여된다.
        - 처음에 AUTOINCREMENT로 id값을 부여하였다면 레코드에 고유의 id이므로 제거하면 해당 id값도 제거가 된다.
      
        ```sql
        CREATE TABLE members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        
        INSERT INTO members VALUES 
        (1, '홍길동'), 
        (2, '김철수'),
        (3, '이호영'),
        (4, '박민희'),
        (5, '최혜영');
        
        DELETE FROM members WHERE rowid=5;
        INSERT INTO members (name) VALUES ('주세환'); 
        SELECT * FROM members;
        -- id  name
        -- --  ----
        -- 1   홍길동
        -- 2   김철수
        -- 3   이호영
        -- 4   박민희
        -- 6   주세환  
        ```
      
        
        
      - **.sql파일 / .sqlite3파일 차이점**
      
        > 사실 실습을 처음 하면서 파일 형식과 이름부터 너무 헷갈렸다
        >
        > 내가 깨달은 바를 정리하자면
        >
        > sql 파일은 그냥 sql 언어를 기록핻둔 메모장 같은 파일이다. sql문을 적으면 자동으로 코드에 색이 입혀지고 추천 명령어가 뜬다. 하지만 바로 실행하는 파일은 아니고 드래그로 선택 영역을 지정 후 해당 코드만 실행하거나 전체를 제대로 구성하여 전체 파일을 바로 실행 돌릴 수도 있다. 하지만 메모장의 느낌이 강하다
        >
        > 명령어는 사실 터미널창에서 CLI 형식으로 입력해 주면 된다.
      
        > sqlite3파일은 데이터베이스 파일이다. 바로 열리지 않는다. open DATABASE 로 접근할 수 있다. 용량이 상당한 편이다.
        >
        > csv파일을 활용할 때는 sqlite3파일에서 불러와서 테이블을 생성하여 사용한다. 그 이후에는 sqlite3 데이터베이스에서 작업을 계속 하며 그 때 활용하는 언어들을 sql 파일에 저장하는 방식이다.
