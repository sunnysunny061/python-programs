def fun(x):
    for i in range(1,x):
        for j in range(i,x):
            for k in range(j,x+1):
                if (i*i+j*j==k*k):
                    print(i,j,k)




x=int(input())
fun(x)