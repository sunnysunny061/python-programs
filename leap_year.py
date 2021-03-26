def leap_year(x):
    if (x%4==0):
        if(x%100==0):
            if(x%400==0):
                print('yes leap year')
            else:
                print('not a leap year')
        else:
            print('leap year')
    else:
        print('not a leap year')

x=int(input())
leap_year(x)