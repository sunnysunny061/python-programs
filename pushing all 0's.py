def fun(s):
    l=len(s)
    m=[]
    n=[]
    for i in range(0,l):
        if s[i]==0:
            m.append(0)
        else:
            n.append(s[i])
    n=n+m
    print(n)


s=list(map(int,input().split()))
fun(s)