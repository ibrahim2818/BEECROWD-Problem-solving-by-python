A=eval(input())
B=eval(input())
C=eval(input())
D=eval(input())
E=eval(input())
pos=[A,B,C,D,E]
count=0
nagetive=0
odd=0
positive=0
for i in pos:
    if i%2==0:
        count+=1
    if i%2==1:
        odd+=1
    if i>0:
        positive+=1
    if i<0:
        nagetive+=1

print(f'''{count} valor(es) par(es)
{odd} valor(es) impar(es)
{positive} valor(es) positivo(s)
{nagetive} valor(es) negativo(s)''')