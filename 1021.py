
x= round(float(input()),2)
x=x*100
a100= abs(x//(100*100))
rem= abs(x%10000)
a50= abs(rem//5000)
rem=abs(rem%5000)
a20= abs(rem//2000)
rem=abs(rem%2000)
a10= abs(rem//1000)
rem=abs(rem%1000)
a5= abs(rem//500)
rem=abs(rem%500)
a2= abs(rem//200)
rem=abs(rem%200)
a1= abs(rem//100)
rem=abs(rem%100)
a050= abs(rem//(0.50*100))
rem=abs(rem%(0.50*100))
a025= abs(rem//(0.25*100))
rem=abs(rem%(0.25*100))
a010= abs(rem//(0.10*100))
rem=abs(rem%(0.10*100))
a0050= abs(rem//(0.05*100))
rem=abs(rem%(0.05*100))
a001= abs(rem//(0.01*100))
rem=abs(rem%(0.01*100))
a100=int(a100)
a50=int(a50)
a20=int(a20)
a10=int(a10)
a5=int(a5)
a2=int(a2)
a1=int(a1)
a050=int(a050)
a025=int(a025)
a010=int(a010)
a0050=int(a0050)
a001= int(a001)
print(f'''NOTAS:
{a100} nota(s) de R$ 100.00
{a50} nota(s) de R$ 50.00
{a20} nota(s) de R$ 20.00
{a10} nota(s) de R$ 10.00
{a5} nota(s) de R$ 5.00
{a2} nota(s) de R$ 2.00
MOEDAS:
{a1} moeda(s) de R$ 1.00
{a050} moeda(s) de R$ 0.50
{a025} moeda(s) de R$ 0.25
{a010} moeda(s) de R$ 0.10
{a0050} moeda(s) de R$ 0.05
{a001} moeda(s) de R$ 0.01''')