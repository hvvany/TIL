t = int(input())
for _ in range(t):
  k = int(input())
  n = int(input())
  graph = [[1] for _ in range(15)]
  graph[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
  for j in range(1,15):
    for i in range(1,14):
      graph[j].append(graph[j][i-1] + graph[j-1][i])
  print(graph[k][n-1])