x= int(input())
def total_sum(a, b):
    y=0
    m=max(a,b)
    n= min(a,b)
    for i in range(n+1, m):
        if i%2 ==1 :
            y= y+i
    return y

for i in range(x):
    A, B= map(int,input().split())
    print(total_sum(A, B))




