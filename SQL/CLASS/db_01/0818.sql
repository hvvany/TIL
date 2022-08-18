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
SELECT * , COUNT(*) AS '사람수' FROM healthcare GROUP BY smoking;

-- 2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
SELECT * , COUNT(*) AS '사람수' FROM healthcare GROUP BY is_drinking;

-- 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.
SELECT * , COUNT(*) AS '사람수' FROM healthcare WHERE blood_pressure >= 200 AND blood_pressure != '' GROUP BY is_drinking;

-- 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.
SELECT sido, COUNT(sido) AS '사람수' FROM healthcare GROUP BY sido HAVING COUNT(sido) >= 50000;

-- 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.
--> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.
SELECT  height, COUNT(*) AS 사람수
FROM healthcare 
GROUP BY height 
ORDER BY 사람수 DESC LIMIT 5;

-- 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 
--> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.
SELECT weight 몸무게, height 키, COUNT(*) 사람수
FROM healthcare
GROUP BY height, weight
ORDER BY 사람수 DESC LIMIT 5;

-- 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.
SELECT is_drinking 음주여부, AVG(waist) 평균허리둘레, COUNT(*) 사람수
FROM healthcare
GROUP BY is_drinking;


-- 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.
--> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.
SELECT gender 성별, ROUND(AVG(va_left),2) '평균 왼쪽 시력', ROUND(AVG(va_right),2) '평균 오른쪽 시력'
FROM healthcare
GROUP BY gender;

-- 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.
--> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 
-- 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.
SELECT age 나이대, ROUND(AVG(height),2) '평균 키', ROUND(AVG(weight),2) '평균 몸무게'
FROM healthcare
GROUP BY 나이대
HAVING '평균 키' >= 160 AND '평균 몸무게' >= 60;

-- 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.
--> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.
SELECT is_drinking '음주 여부', smoking '흡연 여부', ROUND(AVG(weight*10000/POWER(height,2)),2) '평균 BMI'
FROM healthcare
GROUP BY is_drinking, smoking
HAVING is_drinking != '' AND smoking != '';





