a=int(input().split()[-1])
h1, m1, s1=map(int, input().split(' : '))
b=int(input().split()[-1])
hours1, minutes1, seconds1=map(int, input().split(' : '))

x= (a*24*60*60) + (h1*60*60) + (m1*60) + s1
y=(b*24*60*60) + (hours1*60*60) + (minutes1*60) + seconds1

z= y-x
newdays= z//(24*60*60)
rem= z%(24*60*60)
newhours= rem//(60*60)
rem= rem%(60*60)
newminutes= rem//60
newseconds= rem%60
print(f'''{newdays} dia(s)
{newhours} hora(s)
{newminutes} minuto(s)
{newseconds} segundo(s)''')
