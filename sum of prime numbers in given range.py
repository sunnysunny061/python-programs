def fun(s):
    r1=s[0]
    r2=s[1]
    t=[]
    for num in range(r1,r2+1):
        if num>1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                t.append(num)
    print(sum(t))



s=list(map(int,input().split()))
fun(s)