x= int(input())
for i in range(x):
    number = int(input())
    count=0
    for j in range(2, number):
        if number%j == 0:
            count = 1
            break
    if count == 0:
        print(f'''{number} eh primo''')
        
    else:
        print(f'''{number} nao eh primo''')
        
