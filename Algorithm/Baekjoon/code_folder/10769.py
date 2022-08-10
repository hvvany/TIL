
text = input()
sad = text.count(':-(')
happy = text.count(':-)')
if happy > sad :
    print('happy')
elif happy < sad :
    print('sad')
elif happy == sad :
    if happy == 0:
        print('none')
    else:
        print('unsure')