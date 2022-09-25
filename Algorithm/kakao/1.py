# def solution(today, terms, privacies):
#     answer = []
#     terms_dic = dict()
#     y_2_m_today = int(today[1:4])*12 + int(today[5:7])

#     for term in terms:
#       c, m = term.split()
#       terms_dic[c] = int(m)
#     print(terms_dic)

#     for idx in range(len(privacies)):
#         inf_date = privacies[idx][0:10]
#         inf_code = privacies[idx][-1]
#         y_2_m_inf = int(inf_date[1:4])*12 + int(inf_date[5:7])
#         month_dif = y_2_m_today - y_2_m_inf
#         print(f'month_dif : {month_dif}')

#         if month_dif <= terms_dic[inf_code]:
#           print('yes1')
#           if month_dif == terms_dic[inf_code]:
#             print('yes2')
#             print(f'inf_d : {inf_date[-2:]} to : {today[-2:]}')
#             if int(inf_date[-2:]) <= int(today[-2:]):
#               print('yes3')
#               answer.append(idx + 1)
#               continue
#           if month_dif == terms_dic[inf_code] - 1:
#             print('wow')
#             print(f'today_day : {today[-2::]}, inf : {inf_date[-2::]}')
#             if today[-2::] == '28' and inf_date[-2::] == '01':
#               continue
#             else:
#               answer.append(idx + 1)
#               continue
#         else:
#           answer.append(idx + 1)

#     return answer


def solution(today, terms, privacies):
    answer = []
    terms_dic = dict()
    y_2_d_today = int(today[1:4])*12*28 + int(today[5:7])*28 + int(today[8:])

    for term in terms:
      c, m = term.split()
      terms_dic[c] = int(m)
    print(terms_dic)

    for idx in range(len(privacies)):
        inf_date = privacies[idx][0:10]
        inf_code = privacies[idx][-1]
        y_2_d_inf = int(inf_date[1:4])*12*28 + int(inf_date[5:7])*28 + int(inf_date[8:])
        
        expire_date = y_2_d_inf + terms_dic[inf_code]*28

        if expire_date <= y_2_d_today:
          answer.append(idx + 1)

    return answer
















today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms, privacies))