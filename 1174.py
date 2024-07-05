x=[]
for i in range(100):
    number= input()
    number= float(number)
    x.append(number)
for i in range(100):
    if x[i] <=10:
        print(f'''A[{i}] = {x[i]}''')
    