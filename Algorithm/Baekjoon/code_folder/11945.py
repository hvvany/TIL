from pprint import pprint
n, m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]

for col in range(n):
    for num in matrix[col][::-1]:
        print(num,end='')
    print()