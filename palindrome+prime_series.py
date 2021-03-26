def fun(x):
    s=[1,1]
    t=[]
    for i in range(0,50):
        c=s[i]+s[i+1]
        s.append(c)
    for num in range(2, 50 + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                t.append(num)
    print(t)
    if x%2==0:
        m=int(x/2)
        print(t[m-1])
    else:
        m=int((x-1)/2)
        print(s[m])



x=int(input())
fun(x)