x=[]
a=0
b=1
c=0
for i in range(61):
    x.append(a)
    c=a+b
    a=b
    b=c

test_case= int (input())
for i in range(test_case):
    number = int (input())
    print(f'''Fib({number}) = {x[number]}''')