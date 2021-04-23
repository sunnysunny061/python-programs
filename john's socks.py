def fun(arr):
    count=0
    arr2=list(set(arr))
    for i in range(0,len(arr2)):
        s=arr.count(arr2[i])
        s=s//2
        count = count+s
    print(count)
n=input()
arr=list(map(int,input().split()))
fun(arr)