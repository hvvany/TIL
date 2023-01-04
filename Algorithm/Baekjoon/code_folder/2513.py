n, m, k = map(int,input().split())
answer_left = []
answer_right = []
result_left = 0
result_right = 0

for _ in range(n):
    position, cnt = map(int,input().split())
    distance = abs(k - position)
    if k - position >= 0: # left
        for _ in range(cnt):
            answer_left.append(distance)
    else:
        for _ in range(cnt):
            answer_right.append(distance)
answer_left.sort(reverse=True)
answer_right.sort(reverse=True)
# print(answer_left)
# print(answer_right)

if len(answer_left) > 0:
    for i in range(len(answer_left)//m + 1):
        result_left += answer_left[m * i]*2
if len(answer_right) > 0:
    for i in range(len(answer_right)//m + 1):
        result_right += answer_right[m * i]*2
# print(result_left)
# print(result_right)
print(result_right + result_left)