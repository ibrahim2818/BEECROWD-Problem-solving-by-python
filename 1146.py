while True:
    x= int(input())
    if x==0:
        break
    else:
        p= range(1,x+1)
        line= " ".join(map(str,p))
        print(line)