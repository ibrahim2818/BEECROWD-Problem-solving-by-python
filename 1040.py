def quardinate(a,b):
    if a>0 and b>0:
        return "Q1"
    elif a<0 and b<0:
        return "Q3"
    elif a>0 and b<0:
        return "Q4"
    elif a==0 and b==0:
        return "Origem"
    elif a<0 and b>0:
        return "Q2"
    elif b==0:
        return "Eixo X"
    elif a==0:
        return "Eixo Y"


A, B=list(map(float,input().split()))
result= quardinate(A,B)
print(result)
