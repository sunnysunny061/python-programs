def fun(x):
    arr=[]
    for i in range(0,x):
        arr.append(int(input()))
    print(arr)
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)


x=int(input())
fun(x)