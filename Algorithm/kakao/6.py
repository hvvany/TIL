def solution(n, m, x, y, r, c, k):
    answer = ''

    # k가 홀수인지 짝수인지 구해서 최단거리랑 비교하여 imposibble판단
    short_cut = abs(x-r) + abs(y-c)
    if short_cut <= k:
      if short_cut % 2 == 0 and k % 2 == 0:
        
        
    return answer