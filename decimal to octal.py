def fun(decimal):
    i=1
    octal=0
    while decimal>1:
        octal=octal+(decimal%8)*i
        decimal=decimal//8
        i=i*10
    print(octal)
decimal=int(input())
fun(decimal)


