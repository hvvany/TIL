# 순회, 전치, 회전

#순회 #전치 #회전 

1. ## 순회

   - 이차원 리스트를 단순히 출력하면 아래와 같이 나온다

     ```python
     matrix = [
         [1, 2, 3, 4],
     	[5, 6, 7, 8],
     	[9, 0, 1, 2]
     ]
     
     print(matrix)
     ```
     

   - 대괄호를 없애고 숫자만 나타낼 수 없을까?

     ```python
     print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
     print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
     print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
     
     >>> 1 2 3 4
     >>> 5 6 7 8
     >>> 9 0 1 2
     ```

     > 길이가 100x100면 답이 안보인다.

     1. 이중 for문을 이용한 `행` 우선 순회

        ```python
        matrix = [
        	[1, 2, 3, 4],
        	[5, 6, 7, 8],
        	[9, 0, 1, 2]
        ]
        for i in range(3):
        	for j in range(4):
        		print(matrix[i][j], end=" ")
        	print()
            
        >>> 1 2 3 4
        >>> 5 6 7 8
        >>> 9 0 1 2
        ```

     2. 이중 for문을 이용한 `열` 우선 순회

        ```python
        matrix = [
        	[1, 2, 3, 4],
        	[5, 6, 7, 8],
        	[9, 0, 1, 2]
        ]
        for i in range(4): # 열
        	for j in range(3): # 행
        		print(matrix[j][i], end=" ")
        	print()
            
        >>> 1 5 9
        >>> 2 6 0
        >>> 3 7 1
        >>> 4 8 2
        ```

     3. 행 우선 순회를 이용해 2차원 `리스트 총합` 구하기

        ```python
        matrix = [
        	[1, 1, 1, 1],
        	[1, 1, 1, 1],
        	[1, 1, 1, 1]
        ]
        
        total = 0
        for i in range(3):
        	for j in range(4):
        		total += matrix[i][j]
        print(total)
        >>> 12
        ```

     4. 행 우선 순회를 이용해 2차원 리스트의 최대값, 최솟값 구하기

        ```python
        # 최대값
        matrix = [
        	[0, 5, 3, 1],
        	[4, 6, 10, 8],
        	[9, -1, 1, 5]
        ]
        max_value = 0
        for i in range(3):
        	for j in range(4):
        		if matrix[i][j] > max_value:
        		max_value = matrix[i][j]
        print(max_value)
        >>> 10
        ```

        ```python
        # 최소값
        matrix = [
        	[0, 5, 3, 1],
        	[4, 6, 10, 8],
        	[9, -1, 1, 5]
        ]
        min_value = 99999999
        for i in range(3):
        	for j in range(4):
        		if matrix[i][j] < min_value:
        		min_value = matrix[i][j]
        print(min_value)
        >>> -1
        ```

        

   

2. ## 전치

   > 전치란 행렬의 행과 열을 서로 맞바꾸는 것을 의미

   ```python
   matrix = [
   	[1, 2, 3, 4],
   	[5, 6, 7, 8],
   	[9, 0, 1, 2]
   ]
   transposed_matrix = [[0] * 3 for _ in range(4)]
   for i in range(4):
   	for j in range(3):
   		transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
   """
   transposed_matrix = [
   	[1, 5, 9],
   	[2, 6, 0],
   	[3, 7, 1],
   	[4, 8, 2]
   ]
   """
   ```

   

3. ## 회전

   > 문제에서 2차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.

   1. 왼쪽으로 90도 회전하기

      ```python
      matrix = [
      	[1, 2, 3],
      	[4, 5, 6],
      	[7, 8, 9]
      ]
      n = 3
      rotated_matrix = [[0] * n for _ in range(n)]
      
      for i in range(n):
      	for j in range(n):
      		rotated_matrix[i][j] = matrix[j][n-i-1]
      ```

   2. 오른쪽으로 90도 회전하기

      ```python
      matrix = [
      	[1, 2, 3],
      	[4, 5, 6],
      	[7, 8, 9]
      ]
      n = 3
      rotated_matrix = [[0] * n for _ in range(n)]
      
      for i in range(n):
      	for j in range(n):
      		rotated_matrix[i][j] = matrix[n-j-1][i]
      ```

      
