import numpy as np

def matrix_mul(r,c):
    matrix1=[]
    matrix2=[]
    for i in range(0,r):
        m1=list(map(int,input().split()))
        matrix1.append(list(m1))
    print(matrix1)
    for i in range(0,r):
        m2=list(map(int,input().split()))
        matrix2.append(list(m2))

    result=np.dot(matrix1,matrix2)
    for r in result:
        print(r)



r=int(input('enter the no rows: '))
c=int(input('enter the no columns: '))
matrix_mul(r,c)