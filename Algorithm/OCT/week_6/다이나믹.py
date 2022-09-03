n = int(input())
numbers = list(map(int,input().split()))
count_lst = [1]*n

# 수열 돌면서 작은 값의 누적 값 가장 큰거에 +1 해서 현재 누적값 저장
for i in range(n):
  for j in range(i):
    if numbers[j] < numbers[i]:
      count_lst[i] = max(count_lst[j]+1,count_lst[i])
print(max(count_lst))
