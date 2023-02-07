l, r = map(int,input().split())
l_lst = list(input())
r_lst = list(input())
t = int(input())
l_lst.reverse()

l_idx_lst = [*range(l)]
r_idx_lst = [*range(l,(r+1)*2,2)]
l_idx_lst += [*range(l+1,(r+2)*2,2)]
num = l_idx_lst[-1]
l_idx_lst += [*range(num+1,num+l)]
answer_lst = ['']*(2*(r+l))

print(l_idx_lst)
print(r_idx_lst)
print(answer_lst)

idx = 0
for i in r_idx_lst:
    answer_lst[i] = r_lst[idx]
    idx += 1
idx = 0
if t >= r+l:
    t = r+l-1
for j in range(t,t+l):
    answer_lst[l_idx_lst[j]] = l_lst[idx]
    idx += 1
print(answer_lst)
print("".join(answer_lst))