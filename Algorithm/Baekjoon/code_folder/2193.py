n = int(input())
number = [1,0]
cnt = 0

def counter(before_num):
  memory = []
  if before_num == 0:
    counter()
