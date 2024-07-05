
T= input()
x=[]
z=[]
count=0
for i in range(12):
    c=[]
    for j in range(12):
        p= float(input())
        c.append(p)
    x.append(c)
for row in range(0,12):
    for col in range(0,12):
        if row<col:
            z.append(x[row][col])
            count += 1
if T=='S':
    output=sum(z)
    print(f'''{output:.1f}''')
if T=='M':
    output=sum(z)/count
    print(f'''{output:.1f}''')