import heapq
import math

def solution(jobs):
    t = 0
    k = 0
    stack = []
    processing = False
    last_process = False
    finish_time = 0
    want_start_time = 0

    for job in jobs:
      want_start_time += job[0]

    jobs = sorted(jobs,reverse=True)
    
    print(f'want_start_time : {want_start_time}')
    
    while True:     # 시간의 흐름을 생각. 한 번 반복이면 t가 1ms 경과
        print(f'\nwhile 문 진입')
        if k == 0:  # 작업중인게 있는지 확인 후 없으면 processing 초기화
            if processing == True:
                finish_time += t
                print(f'finish_time : {finish_time}')
            if last_process == True and not stack:
                print(f'want_start_time : {want_start_time}')
                return math.trunc((finish_time - want_start_time) // len(jobs))
                break
            processing = False
        else:
            print(f'else_1')
            processing = True
            
        for i in range(1,len(jobs)+1):        # 처리할 정보 가져와서
            print(f'for_1')
            if jobs[-i][0] == t:              # 시간이 해당되면
                heapq.heappush(stack,[jobs[-i][1],jobs[-i][0]])     # 스택에 추가한다
                jobs.pop()
                jobs.append(0)
                print(f'if_1')
                print(f'i : {i}')
                if i == len(jobs):        # 해당 되는 시간조건 통과한 인덱스가 마지막이면
                    last_process = True       # 마지막 작업 last_process TRUE
                    print(f'if_2')
        
        if processing == False and stack:    # 진행중인 작업이 없고 스택에 작업 있으면
            k = heapq.heappop(stack)[0]      # k 변수에 새로운 작업의 소요 시간 추가
            print(f'if_3')
        
        print(f'k : {k}')
        k -= 1
            
        print(f't : {t}')
        t += 1

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

# stack = [[0, 3], [1, 9], [2, 6]]
# stack = sorted(stack,key=lambda x : x[1], reverse=True)
# for _ in range(3):
#     print()