def answer(color_dic, num_lst):
    # 1번, 4번 조건
    for color in color_dic:
        if color_dic[color] == 5:
            # 1번 조건
            if num_lst[4] == num_lst[0] + 4:
                return num_lst[-1] + 900
            # 4번 조건
            else:
                return num_lst[-1] + 600
    # 2번 조건
    if num_lst[0] == num_lst[3] != num_lst[4]:
        return num_lst[0] + 800
    elif num_lst[1] == num_lst[4] != num_lst[0]:
        return num_lst[1] + 800
    # 3번 조건
    elif num_lst[0] == num_lst[2] and num_lst[3] == num_lst[4]:
        return num_lst[0]*10 + num_lst[3] + 700
    elif num_lst[0] == num_lst[1] and num_lst[2] == num_lst[4]:
        return num_lst[2]*10 + num_lst[0] + 700
    # 5번 조건
    elif num_lst[4] == num_lst[0] + 4:
        return num_lst[4] + 500
    # 6번 조건
    elif num_lst[0] == num_lst[2]:
        return num_lst[0] + 400
    elif num_lst[1] == num_lst[3]:
        return num_lst[1] + 400
    elif num_lst[2] == num_lst[4]:
        return num_lst[2] + 400
    # 7번 조건
    elif num_lst[0] == num_lst[1] != num_lst[2] and num_lst[2] == num_lst[3] != num_lst[4]:
        return num_lst[3]*10 + num_lst[0] + 300
    elif num_lst[0] == num_lst[1] != num_lst[2] and num_lst[3] == num_lst[4] != num_lst[2]:
        return num_lst[3]*10 + num_lst[0] + 300
    elif num_lst[1] == num_lst[2] != num_lst[0] and num_lst[3] == num_lst[4] != num_lst[2]:
        return num_lst[3]*10 + num_lst[1] + 300
    # 8번 조건
    elif num_lst[0] == num_lst[1]:
        return num_lst[0] + 200
    elif num_lst[1] == num_lst[2]:
        return num_lst[1] + 200
    elif num_lst[2] == num_lst[3]:
        return num_lst[2] + 200
    elif num_lst[3] == num_lst[4]:
        return num_lst[3] + 200
    # 9 번 조건
    return num_lst[-1] + 100

color_dic_out = {'R':0, 'G':0, 'B':0, 'Y':0}
num_lst_out = []
for _ in range(5):
    color, num = input().split()
    color_dic_out[color]+= 1
    num_lst_out.append(int(num))
    num_lst_out.sort()

print(answer(color_dic_out, num_lst_out))