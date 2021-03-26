x=list(input())
y=list(input())
x_set=set(x)
y_set=set(y)
z=list(x_set.intersection(y_set))
for i in z:
    print(i , end='')
print()
print( len(z))