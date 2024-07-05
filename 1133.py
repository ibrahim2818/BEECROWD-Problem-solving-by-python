a=int(input())
b= int(input())
m= max(a,b)
n=min(a,b)
for i in range(n+1,m):
    if i%5==2 or i%5==3:
        print(i)