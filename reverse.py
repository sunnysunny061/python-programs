def reverse(x):
    reverse=0
    while x!=0:
        reverse = reverse * 10
        reverse=reverse+x%10
        x=x//10
    print(reverse)

x=int(input())
reverse(x)