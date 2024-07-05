A,B= list(map(int,input().split()))
if A==B:
    x=0
elif A>B: 
    x= (24-A)+B
else: 
    x=B-A
print(f'''O JOGO DUROU {x} HORA(S)''')