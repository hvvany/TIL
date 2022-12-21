# n = int(input())
# n_lst = list(map(int,input().split()))
# m = int(input())
# m_lst = list(map(int,input().split()))
# cnt_dic = dict()
# answer = []

# for number in n_lst:
#     if number in cnt_dic:
#         cnt_dic[number] += 1
#     else:
#         cnt_dic[number] = 1

# for num in m_lst:
#     if num in cnt_dic:
#         answer.append(cnt_dic[num])
#     else:
#         answer.append(0)

# print(*answer)

n = int(input())
n_set = set(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))
answer = []

for num in m_lst:
    if num in n_set:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)