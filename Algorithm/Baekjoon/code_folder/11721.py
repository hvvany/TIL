t = input()
for i in range(len(t)//10):
    print(t[i*10:(i+1)*10])
if len(t) % 10 > 0:
    print(t[-(len(t)%10):])