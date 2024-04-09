a, b, c= list(map(int,input().split()))
x= ((a+b)+ abs(a-b))/2
y= ((x+c)+ abs(x-c))/2
print(f"{int(y)} eh o maior")
