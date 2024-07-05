x= int(input())

for i in range(x):
    A, B= map(int, input().split())
    total=0
    while B>0:
        if A%2==1:
            total +=A
            B -=1
        A+=1
    print(total)


