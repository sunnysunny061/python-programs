#new code

def hcf(a,b,c):
    if (a>b) and (c>b):
        smaller=b
    elif (b>a) and (c>a):
        smaller = a
    else:
        smaller= c
    hcf=1
    for i in range(2,smaller+1):
        if ((a%i==0) and (b%i==0) and (c%i==0)):
            hcf=i

    print(hcf)

a=int(input())
b=int(input())
c=int(input())
hcf(a,b,c)
