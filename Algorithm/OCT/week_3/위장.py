def solution(clothes):
    clothe_dic = dict()
    answer = 1
    for clothe in clothes:
        if clothe[1] in clothe_dic:
            clothe_dic[clothe[1]] += 1
        else:
            clothe_dic[clothe[1]] = 1
    for key in clothe_dic:
        answer *= clothe_dic[key] + 1
    return answer - 1