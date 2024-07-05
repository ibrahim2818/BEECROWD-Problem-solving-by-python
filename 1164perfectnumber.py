x= int(input())
for i in range(x):
    number = int(input())
    total = 0
    for j in range(1,number):
        if number%j == 0:
            total= total+j
    if total==number:
        print(f'''{number} eh perfeito''')
    else:
        print(f'''{number} nao eh perfeito''')
