n,m = list(map(int,input().split()))

수열 = []

def dfs():
    print(f'수열 : {수열}')
    if len(수열)==m:         # 길이가 m인경우 완성된 수열 프린트
        print(*수열)
        return
    
    for i in range(1,n+1):  # 길이가 m까지 처음 완성된 후 그 다음 숫자를 순서대로 넣으면서 조합 완성
        if i not in 수열:
            수열.append(i)
            dfs()           # 끝자리 부터 모든 순서 돌고 그  상위 자릿수가 다시 증가해서 반복
            수열.pop()

dfs()