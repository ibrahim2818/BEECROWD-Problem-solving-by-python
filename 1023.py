def removing(dictionary):
    seen={}
    for key, value in dictionary.items():
        if value in seen:
            dictionary[seen[key]] =+key
        else:
            seen[key]=value






is_on= True
consumer=[]
consume=[]
diction= {}
count=0
while is_on:
    count+=1
    n= int(input())
    if n==0:
        is_on=False
    else:
        for i in range(n):
            A, B= map(int ,input().split())
            value= B//A
            consumer.append(A)
            consume.append(B)
            if A in diction:
                diction[A].append(value)
            else:
                diction[A]= [value]
        diction= dict(sorted(diction.items(), key=lambda item: item[1]))
        avg= sum(consume)/sum(consumer)
        print(f'''Cidade# {count}:''')
        for key, values in diction.items():
            


            for value in values:
                print(f'{key}-{value}', end=" ")
        print(f"\nConsumo medio: {avg:.2f} m3.")
        

            


