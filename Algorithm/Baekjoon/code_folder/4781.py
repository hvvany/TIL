while True:
    n, m = input().split()
    if n == '0' and m =='0.00':
        break
    m = m.replace('.','')
    n, m = map(int,(n,m))
    candies = [(0,0)]
    for _ in range(n):
        cal, price = input().split()
        price = price.replace('.','')
        cal, price = map(int,(cal,price))
        candies.append((cal,price))
    knap = [[0] * (m+1) for _ in range(n + 1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if candies[i-1][1] > j:
                knap[i][j] = knap[i-1][j]
                continue
            knap[i][j] = max(knap[i][j], knap[i][j-candies[i][1]] + candies[i][0], knap[i-1][j-candies[i-1][1]] + candies[i-1][0])
    print(knap)