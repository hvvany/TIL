# 딕셔너리 나이 : [(순서, 이름)]
n = int(input())
inform_dic = dict()
for _ in range(n):
  k, v = input().split()
  k = int(k)
  if k in inform_dic:
    inform_dic[k] += [(len(inform_dic[k]),v)]
  else:
    inform_dic[k] = [(0,v)]
# print(f'inform_dic : {inform_dic}')
for k in sorted(inform_dic):
  for i, v in sorted(inform_dic[k],key=lambda x:x[0]):
    print(f'{k} {v}')



# 딕셔너리 나이 : [이름, 이름...]
# n = int(input())
# inform_dic = dict()
# for _ in range(n):
#   k, v = input().split()
#   k = int(k)
#   if k in inform_dic:
#     inform_dic[k] += [v]
#   else:
#     inform_dic[k] = [v]
# print(inform_dic)
# for k in sorted(inform_dic):
#   for v in inform_dic[k]:
#     print(f'{k} {v}')



# import sys

# n = int(sys.stdin.readline())
# lst = []
# for i in range(n):
#   age, name = sys.stdin.readline().strip('\n').split()
#   lst.append((int(age), name))
# lst = sorted(lst,key = lambda x: x[0])

# for person in lst:
#   print(person[0],person[1])