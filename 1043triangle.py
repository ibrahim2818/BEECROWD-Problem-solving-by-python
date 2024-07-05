
A, B, C= list(map(float,input().split()))
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c> a:
        s=(a+b+c)
        return s
    else:
        traArea= ((a+b)/2)*c
        return traArea

result = triangle(A,B,C)

if A+B>C and A+C>B and B+C>A:
    print (f'''Perimetro = {result:.1f}''')
else:
    print (f'''Area = {result:.1f}''')