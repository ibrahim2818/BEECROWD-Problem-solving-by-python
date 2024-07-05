A, B, C, D= list(map(int,input().split()))
if A==C:
    if B==D :
        x = 24
    elif B<D:
        x=0
elif A>C:
    x = (24-A+C)
else:
    x = C-A

y=abs(B-D)
total=x*60
if B==D:
    total=total
elif B>D:
    total=total-y
else:
    total=total+y
p= total//60
q=total%60

print(f'''O JOGO DUROU {p} HORA(S) E {q} MINUTO(S)''')