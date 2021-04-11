def fun(arr):
    arr2=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] == arr[j]):
                s=j-i
                arr2.append(s)
    if (len(arr2) == 0):
        print(-1)
    else:
        print(min(arr2))


arr=list(map(int,input().split()))
fun(arr)