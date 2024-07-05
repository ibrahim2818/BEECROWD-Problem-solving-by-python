while True:
    l= int(input())
    if l>=0 and l<=11:
        break
T= input()
x=[]
for i in range(12):
    c=[]
    for j in range(12):
        p= float(input())
        c.append(p)
    x.append(c)
if T=='S':
    output= sum(x[l])
    print (f'''{output:.1f}''')
if T=='M':
    output= sum(x[l])/12
    print (f'''{output:.1f}''')