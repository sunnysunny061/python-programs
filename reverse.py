def rev(x):
    rev=0
    while x!=0:
        rev = rev * 10
        rev=rev+x%10
        x=x//10
    print(rev)

x=int(input())
rev(x)