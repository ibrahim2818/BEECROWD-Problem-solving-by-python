a=[]
for i in range(1,101):
    x= int(input())
    a.append(x)
q=max(a)
p=a.index(q)
print(q)
print(p-1)