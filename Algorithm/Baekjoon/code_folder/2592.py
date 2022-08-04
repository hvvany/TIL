dic = dict()
for _ in range(10):
    n = int(input())
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
num_sum=0
cnt = 0

for key in dic:
    num_sum += key*dic[key]
    
    if dic[key] > cnt:
        cnt = dic[key]
        freq = key

print(int(num_sum/10))
print(freq)