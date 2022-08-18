-- 0818 실습
-- 수업 내용 정리

-- 문자열 함수
SUBSTR 문자열 자르기
TRIM, RTRIM, LTRIM  공백 제거
LENGTH  길이
REPLACE(문자열, 패턴, 변경값) 패턴에 일치하는 부분을 변경
UPPER, LOWER  대소문자
||  문자열 합치기

-- 숫자 함수
ABS 절대값
SIGN   부호
MOD(숫자1, 숫자2) 숫자 1을 숫자 2로 나눈 나머지
CEIL, FLOOR, ROUND   올림, 버림, 반올림
POWER(숫자1, 숫자2)  숫자1의 숫자2 제곱
SQRT  제곱근


-- GORUP BY
-- ALIAS
AS 또는 생략하고 공백으로 컬럼 이름 지정 가능
SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2
무조건 WHERE 절 뒤에 GROUP BY 작성








-- 1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
