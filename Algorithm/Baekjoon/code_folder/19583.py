s, e, q = input().split()
s = int(s[:2])*60 + int(s[3:])
e = int(e[:2])*60 + int(e[3:])
q = int(q[:2])*60 + int(q[3:])
entrance_set = set()
exit_set = set()

while 1:
  try:
    inform = input()
    time = int(inform[:2])*60 + int(inform[3:5])
    name = inform[6:]
    if 0 <= time <= s:
      entrance_set.add(name)
    elif e <= time <= q:
      if name in entrance_set:
        exit_set.add(name)
  except:
    break
print(len(exit_set))