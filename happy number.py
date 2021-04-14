def happy_number(x):
    x = list(x)
    for i in range(0,10):
        arr = x
        s = 0
        for i in range(0,len(x)):
            s = s + int(x[i])**2
        x = list(str(s))
    if (s == 1):
        print('Happy Number')
    else:
        print('Not A Happy Number')



x = input()
happy_number(x)