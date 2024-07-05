#Md. Ibrahim(2101030)
while True:
    x= int(input())
    if x>0 and x<46:
        break
a=0 
b=1
p=[]
for i in range(x):
    p.append(a)
    c= a+b
    a=b
    b=c
    
print(' '.join(map(str,p)))

    