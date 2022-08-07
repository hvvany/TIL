def solution(clothes):
    clothe_dic = dict()
    count_lst = []
    for clothe in clothes:
        if clothe[1] in clothe_dic:
            clothe_dic[clothe[1]] += 1
        else:
            clothe_dic[clothe[1]] = 1   # headgear : 4 
    # 카운트를 리스트에 저장하여 인덱스로 접근        
    for count in clothe_dic.values():
        count_lst.append(count)
    idx_start = 0
    idx_end = 0
    count_sum = 0
    while idx_end == len(count_lst)-1:
        count_lst[idx_start]*count_lst[idx_end]
        
    answer = 0
    return answer