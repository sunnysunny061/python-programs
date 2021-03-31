def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

l = list(map(int,input().split()))
x=l[0]
y=l[1]
g=gcd(x,y)
for i in range(2,len(l)):
    g=gcd(g,l[i])
print(g)
