# 이차원 리스트

#리스트 #2차원 #행열

1. 이차원 리스트

   > 리스트를 원소로 가지는 리스트

   ```python
   matrix = [[1,2,3], [4, 5, 6], [7, 8, 9]]
   
   # 정렬하면 행렬의 형태가 보인다.
   matrix = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
   ]
   ```

   - 특정 값으로 초기화 된 이차원 리스트 만들기

   1. 직접 작성

      > 예시 4 x 3 행렬

      ```python
      matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
      
      matrix2 = [
      	[0, 0, 0],
      	[0, 0, 0],
      	[0, 0, 0],
      	[0, 0, 0]
      ]
      ```

   2. 반복문으로 작성

      > 예시 100 x 100 행렬

      ```python
      matrix = []
      
      for _ in range(100):
      	matrix.append([0] * 100)
      ```

   3. 리스트 컴프리헨션으로 작성

      > 예시 4 x 3 행렬

      ```python
      n = 4 # 행
      m = 3 # 열
      
      matrix = [[0] * m for _ in range(n)]
      
      print(matrix)
      >>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
      ```

   - 주의 사항 ( 리스트 컴프리 헨션 vs 리스트 곱셈 연산 )

     ```python
     n = 4 # 행
     m = 3 # 열
     
     matrix1 = [[0] * m for _ in range(n)]    # 컴프리 헨션
     matrix2 = [[0] * m] * n                  # 곱셈 연산
     
     # 같은 결과물이 나온다
     print(matrix1)
     >>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
     print(matrix2)
     >>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
     
     # 원소값 변경 해보면?
     matrix1[0][0] = 1
     matrix2[0][0] = 1
     
     print(matrix1)
     >>> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
     print(matrix2)
     >>> [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
     # 곱하기로 받으면 계속 matrix2로 접근하면 복제 모드여서 모든 값이 변한다.
     ```

     

2. 입력 받기

   1. 행렬의 크기가 미리 주어지는 경우

      ```python
      """
      3 x 3 크기의 입력을 받아보자.
      1 2 3
      4 5 6
      7 8 9
      """
      
      matrix = []
      
      for _ in range(3):
      	line = list(map(int, input().split()))
      	matrix.append(line)
      ```

      ```python
      matrix = [list(map(int, input().split())) for _ in range(3)]
      ```

   2. 행렬의 크기가 입력으로 주어지는 경우

      ```python
      """
      n x m 크기의 입력을 받아보자.
      
      3 4
      1 2 3 4
      5 6 7 8
      9 0 1 2
      """
      
      n, m = map(int, input().split()) # 3 4
      matrix = []
      
      for _ in range(n):
      	line = list(map(int, input().split()))
      	matrix.append(line)
      ```

      ```python
      n, m = map(int, input().split()) # 3 4
      
      matrix = [list(map(int, input().split())) for _ in range(n)]
      ```

      

   
