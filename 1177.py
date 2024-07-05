N=[]
x= int(input())
for i in range(0,1000,x):
    for j in range(x):
        N.append(j)

for i in range(0,1000):
    print(f'''N[{i}] = {N[i]}''')