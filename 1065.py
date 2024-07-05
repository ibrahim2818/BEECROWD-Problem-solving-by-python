A=eval(input())
B=eval(input())
C=eval(input())
D=eval(input())
E=eval(input())
pos=[A,B,C,D,E]
count=0
for i in pos:
    if i%2==0:
        count+=1

print(f'''{count} valores pares''')