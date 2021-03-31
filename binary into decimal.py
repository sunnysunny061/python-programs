def fun(x):
    dec=0
    for i in range(0,len(x)):
        s=len(x)-i-1
        p=2**s
        dec=dec+int(x[i])*p

    print(dec)


x=list(input())
fun(x)