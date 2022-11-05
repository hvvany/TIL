k, n = map(int, input().split()) 
line = [int(input()) for _ in range(k)]
start, end = 1, line[0]

while start <= end: 
    mid = (start + end) // 2
    count = 0 

    for l in line: 
        count += l // mid
    if count >= n:
        start = mid + 1
    else: 
        end = mid - 1

print(end)
