def solution(citations):
  n = len(citations)
  citations.sort(reverse = True)
  print(citations)
  
  h = citations[0]
  while True:
    cnt = 0
    for num in citations:
      if num >= h:
        cnt += 1
    if cnt >= h:
      return h
    h -= 1
      

print(solution([4, 4, 4, 2, 2]))