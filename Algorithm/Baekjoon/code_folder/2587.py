num_lst = []
for _ in range(5):
    number = int(input())
    num_lst.append(number)
num_lst.sort()
print(int(sum(num_lst)/5))
print(num_lst[2])