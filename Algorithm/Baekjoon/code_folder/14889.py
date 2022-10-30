from itertools import combinations

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

teams = list(combinations(list(range(N)), N//2))
ans = 10000
for t in range(len(teams)//2) :
    start = 0
    link = 0
    for i in range(N//2) :
        for j in range(N//2) :
            start += S[teams[t][i]][teams[t][j]]
            link += S[teams[-1-t][i]][teams[-1-t][j]]
    절대값 = abs(start-link)
    if 절대값 < ans:
        ans = 절대값
print(ans)