from itertools import combinations

n = int(input())
podo_lst = []
ex_lst = []
for i in range(n):
    podo_lst.append(int(input()))
podo_comb = list(map(sum,combinations(podo_lst,3)))
podo_comb.sort(reverse=True)
for idx in range(n-2):
    ex_lst.append(sum([podo_lst[idx],podo_lst[idx+1],podo_lst[idx+2]]))
ex_lst.sort(reverse=True)

우코테 = True
j = 0
for podo in podo_comb:
    print(f'포도 : {podo}')
    if podo == ex_lst[j] and 우코테 and ex_lst:
        j += 1
        if j != len(ex_lst):
            continue
        else:
            우코테 = False
    else:
        print(podo)
        break