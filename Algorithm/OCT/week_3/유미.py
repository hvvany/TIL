import math
import sys
input = sys.stdin.readline

umi = tuple(map(int,input().split()))
per1 = tuple(map(int,input().split()))
per2 = tuple(map(int,input().split()))
per3 = tuple(map(int,input().split()))
d12 = math.sqrt((per1[0]-per2[0])**2 + (per1[1]-per2[1])**2)
d23 = math.sqrt((per2[0]-per3[0])**2 + (per2[1]-per3[1])**2)
d31 = math.sqrt((per1[0]-per3[0])**2 + (per1[1]-per3[1])**2)

# person과 유미 사이의 거리 + 그person 선택시 거리 합
answer_lst = []
# per1 선택시
umi_per = math.sqrt((umi[0]-per1[0])**2 + (umi[1]-per1[1])**2)
per_per = min(d12,d31) + d23
answer_lst.append(umi_per + per_per)
# per2 선택시
umi_per = math.sqrt((umi[0]-per2[0])**2 + (umi[1]-per2[1])**2)
per_per = min(d12,d23) + d31
answer_lst.append(umi_per + per_per)
# per3 선택시
umi_per = math.sqrt((umi[0]-per3[0])**2 + (umi[1]-per3[1])**2)
per_per = min(d23,d31) + d12
answer_lst.append(umi_per + per_per)

print(int(min(answer_lst)))