A, B, C= list(map(float, input().split()))
side=[A, B, C]
side.sort(reverse=True)
A=side[0]
B=side[1]
C=side[2]
if A>=B+C:
    print('NAO FORMA TRIANGULO')
if (A**2)==(B**2)+(C**2):
    print('TRIANGULO RETANGULO')
if (A**2)>(B**2)+(C**2):
    print('TRIANGULO OBTUSANGULO')

if (A**2)<(B**2)+(C**2):
    print('TRIANGULO ACUTANGULO')
if A==B==C:
    print('TRIANGULO EQUILATERO')
if (A==B!=C) or (A==C!=B) or (B==C!=A):
    print('TRIANGULO ISOSCELES')