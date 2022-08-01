# Stack & Queue

#stack #queue

0. ## 데이터 구조 & 알고리즘

   - **파이썬 기본 데이터 구조**

     > - 컨테이너
     >   - 시퀀스형
     >     - 리스트
     >     - 튜플
     >     - 레인지
     >   - 비시퀀스형
     >     - 세트
     >     - 딕셔너리

   - **코딩 테스트 정복 위한 데이터구조**

     - Array(배열)
     - Linked List(연결리스트)
     - Hash(해시)
     - Stack(스택)
     - Queue(큐)
     - Priority Queue(우션선위 큐)
     - Heap(힙)
     - Tree(트리)
     - Graph(그래프)

   - **코딩 테스트 정복 위한 알고리즘**

     - 기본

       > 완전탐색, 재귀, 시뮬레이션, 그리디

     - 심화

       > DFS, BFS, 백트래킹, 이진탐색, DP, 다익스트라, 크루스칼, 프림

   - 왜 알아야 하는가? 

     > 적절한 상황에서 알맞게 응용하기 위해서!!!

   

1. ## 스택

   > Stack은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조
   >
   > LIFO (Last in First out)

   - 왜 스택을 써야하는가?

     1. 뒤집기, 되돌리기, 되돌아가기

        > 브라우저 히스토리(뒤로가기), ctrl z, 단어 뒤집기

     2. 마무리 되지 않은 일을 임시 저장

        > 괄호 매칭, 함수 호출, 백트래킹, DFS(깊이 우선 탐색)

   - 파이썬에서의 사용

     > 리스트로 스택을 간편하게 사용한다!

     - push : append()
     - pop : pop()

     ```python
     list = [1,2,3,4,5]
     list.append(6)
     # [1,2,3,4,5,6]
     list.pop()
     # [1,2,3,4,5]
     ```

     > BOJ 10773 제로 풀이

     ```python
     stack = []
     for _ in range(int(input())):
     	number = int(input())
     	if number == 0:
     		stack.pop()
     	else:
     		stack.append(number)
     
     print(sum(stack))
     ```

     

     

     

2. ## 큐

   > Queue는 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조
   >
   > FIFO(First in First out)

   > 큐 자료구조도 파이썬에서는 리스트로 간편하게 사용할 수 있다!!!

   - enqueue : append()

   - dequeue : pop(0)

     > BOJ 2161 카드1 풀이

     ```python
     n = int(input())
     queue = list(range(1, n + 1))
     
     while len(queue) > 1:
     	print(queue.pop(0), end=" ")
     	queue.append(queue.pop(0))
         
     print(queue[0])
     ```

   

   

3. ## 덱

   > 양 방향으로 삽입과 삭제가 자유로운 큐

   - => ㅁㅁㅁ

     > appendleft()

   - <= ㅁㅁㅁ

     > popleft()

   - ㅁㅁㅁ <=

     > append()

   - ㅁㅁㅁ =>

     > pop()

     

   - 큐를 이용한 풀이

   ```python
   n = int(input())
   queue = list(range(1, n + 1))
   
   while len(queue) > 1:
   	print(queue.pop(0), end=" ")
   	queue.append(queue.pop(0))
       
   print(queue[0])
   ```

   - 덱을 이용한 풀이

   ```python
   from collections import deque
   
   n = int(input())
   queue = deque(range(1, n + 1))
   
   while len(queue) > 1:
   	print(queue.popleft(), end=" ")
   	queue.append(queue.popleft())
       
   print(queue[0])
   ```

   
