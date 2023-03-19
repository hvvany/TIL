while True:
    inform = list(input())
    if inform[0] == '0':
        break
    answer = 'yes'
    for i in range(len(inform)):
        if inform[i] != inform[-i-1]:
            answer = 'no'
    print(answer)