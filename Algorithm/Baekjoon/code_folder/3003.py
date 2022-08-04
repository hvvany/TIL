chess = [1,1,2,2,2,8]
find = list(map(int,input().split()))
answer = [0]*6

for i in range(6):
    answer[i] = chess[i] - find[i]
print(*answer)