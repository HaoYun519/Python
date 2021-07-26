sc = input('Enter your score: ')
sc = float(sc)
if sc > 1.0: 
    print('error score')
elif sc < 0.0:
    print('error score')
elif sc >= 0.9 :
    print(sc,'A')
elif sc >= 0.8 :
    print(sc,'B')
elif sc >= 0.7 :
    print(sc,'C')
elif sc >= 0.6 :
    print(sc,'D')
elif sc < 0.6 :
    print(sc,'F')