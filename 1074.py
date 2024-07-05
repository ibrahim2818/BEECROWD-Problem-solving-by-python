x= int(input())
p=[]
for i in range(1,x+1):
    p.append(int(input()))

for i in p:
    if i==0:
        print(f'''NULL''')
    elif i%2 == 0 and i>0:
        print(f'''EVEN POSITIVE''')
    elif i%2 == 0 and i<0 :
        print(f'''EVEN NEGATIVE''')
    elif i%2!= 0 and i>0:
        print(f'''ODD POSITIVE''')
    elif i%2!= 0 and i<0:
        print(f'''ODD NEGATIVE''')
