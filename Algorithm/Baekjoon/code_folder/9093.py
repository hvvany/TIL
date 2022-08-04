t = int(input())

for _ in range(t):
    result = ''
    lst = list(input().split())
    for text in lst:
        result += text[::-1] + ' '
        print(result.rstrip())