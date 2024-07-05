inter=0
germio=0
empates=0
count=0
while True:
    count=count+1
    A, B= map(int,input().split())
    if A>B:
        inter=inter+1
    elif A<B:
        germio=germio+1
    elif A==B:
        empates=empates+1
    while True:
        print("Novo grenal (1-sim 2-nao)")
        p=int(input())
        if p==1 or p==2:
            break
    if p==2:
        break

print(f'''{count} grenais
Inter:{inter}
Gremio:{germio}
Empates:{empates}''')
if inter>germio:
    print("Inter venceu mais")
elif germio>inter:
    print("Gremio venceu mais")
elif germio==inter:
    print("Não houve vencedor")