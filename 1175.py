x=[]
for i in range(20):
    p= int(input())
    x.append(p)
x.reverse()

for i in range(20):
    print(f'''N[{i}] = {x[i]}''')
