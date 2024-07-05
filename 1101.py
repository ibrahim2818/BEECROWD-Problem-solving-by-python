def list_sum(x,y):
    q=[]
    c=[x,y]
    c.sort()
    for i in range(c[0],c[1]+1):
        q.append(i)
    return f'''{' '.join(q)} Sum={sum(q)}'''
while True:
    A, B=map(int,input().split())
    if A==0 or B==0:
        break
    else:
        result=list_sum(A,B)
        print (result)
