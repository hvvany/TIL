import sys
input = sys.stdin.readline
dic = dict()

n = input()
num_lst = list(input().split())
v = input().strip()
for num in num_lst:
    if num == v:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
print(dic[v])