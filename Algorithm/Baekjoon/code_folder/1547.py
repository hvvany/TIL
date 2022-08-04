cup_lst = [1,2,3]
n = int(input())
for _ in range(n):
    cup_1, cup_2 = map(int,input().split())
    idx1 = cup_lst.index(cup_1)
    idx2 = cup_lst.index(cup_2)
    cup_lst[idx1], cup_lst[idx2] = cup_lst[idx2], cup_lst[idx1]
print(cup_lst[0])