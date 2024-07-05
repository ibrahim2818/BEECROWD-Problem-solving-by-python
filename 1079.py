N= int(input())
def avg ( A, B, C):
    return round(((A*2+B*3+C*5)/10),1)
x=[]
for i in range(1, N+1):
    a, b, c = map(float, input().split())
    result= avg(a, b, c)
    x.append(result)
for i in x:
    print(f'{i:.1f}')