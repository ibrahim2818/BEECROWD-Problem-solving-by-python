A,B= list(map(int,input().split()))
p = 4.00
q =4.50
r = 5.00
s= 2.00
t=1.50

if A==1:
    print(f'''Total: R$ {(p*B):.2f}''')
elif A==2:
    print(f'''Total: R$ {(q*B):.2f}''')
elif A==3:
    print(f'''Total: R$ {(r*B):.2f}''')
elif A==4:
    print(f'''Total: R$ {(s*B):.2f}''')
elif A==5:
    print(f'''Total: R$ {(t*B):.2f}''')
