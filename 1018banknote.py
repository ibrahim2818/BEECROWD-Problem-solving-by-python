
x=int(input())
print(f"{x}")
a=0
b=0
c=0
d=0
e=0
f=0
g=0
while x>0:
    if x>100:
        a=x/100
        x=x%100
    elif x>50:
        b=x/50
        x=x%50
    elif x>20:
        c=x/20
        x=x%20
    elif x>10:
        d=x/10
        x=x%10
    elif x>5:
        e=x/5
        x=x%5
    elif x>2:
        f=x/2
        x=x%2
    elif x==1:
        g=1
        x=0

a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
print(f'''{a} nota(s) de R$ 100,00
{b} nota(s) de R$ 50,00
{c} nota(s) de R$ 20,00
{d} nota(s) de R$ 10,00
{e} nota(s) de R$ 5,00
{f} nota(s) de R$ 2,00
{g} nota(s) de R$ 1,00''')
    