A=eval(input())
B=eval(input())
C=eval(input())
D=eval(input())
E=eval(input())
F=eval(input())
pos=[A,B,C,D,E,F]
count=0
su= 0
for i in pos:
    if i>0:
        count+=1
        su= su+i

print(f'''{count} valores positivos\n{(su/count):.1f}''')