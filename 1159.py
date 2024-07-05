while True:
    x= int(input())
    if x==0:
        break
    else:
        i=5
        total=0
        while i >0  :
            if x%2==0:
                total=total+x
                i-=1
            x+=1
        print(total)