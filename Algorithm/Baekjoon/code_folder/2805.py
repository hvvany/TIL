n, m = map(int,input().split())
woods = list(map(int,input().split()))

start = 0
end = max(woods)

result = 0
while start <= end:
    wood_len = 0
    cut = (start + end) // 2
    for wood in woods:
        if wood > cut:
            wood_len += wood - cut
    if wood_len < m:
        end = cut - 1
    else:
        result = cut
        start = cut + 1

print(result)