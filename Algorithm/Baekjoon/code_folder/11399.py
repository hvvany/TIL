n = int(input())
lst = list(map(int,input().split()))
answer = 0
for num in sorted(lst):
    answer += n*num
    n -= 1
print(answer)