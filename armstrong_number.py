#code

def fun(x):
    x=list(x)
    n=len(x)
    z=0
    for i in range(0,n):
        z=z+int(x[i])**n
    if z==y:
        print('Armstrong')
    else:
        print('Not a Armstrong')

x=input()
y=int(x)
fun(x)