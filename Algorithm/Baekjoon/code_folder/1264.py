
lst = ['a','e','i','o','u']
while True:
    cnt = 0
    text = input()
    if text == '#':
        break
    for t in text.lower():
        if t in lst:
            cnt += 1
    print(cnt)