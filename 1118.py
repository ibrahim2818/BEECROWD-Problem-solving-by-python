
while True:
    p=[]
    while len(p)<2:
        x= float(input())
        if x>=0 and x<=10:
            p.append(x)
            
        else:
            print("nota invalida")
            
    media= (sum(p))/2
    print(f'''media = {media:.2f}''')
    
    while True: 
        print("novo calculo (1-sim 2-nao)")
        q=int(input())
        if q==2 or q==1:
            break
    if q==2:
        break
    
    
    