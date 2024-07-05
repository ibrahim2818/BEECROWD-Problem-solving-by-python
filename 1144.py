x=int(input())
j=1
for k in range(x):
    print(f'''{j} {j**2} {j**3}''')
    print(f'''{j} {(j**2)+1} {(j**3)+1}''')
    j=j+1