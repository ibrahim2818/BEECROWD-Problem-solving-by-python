import math
A, B, C= list(map(float,input().split()))

#x=-b+-rootb2-2ac/2a 
if A==0 and (B**2<(4*A*C)):
    print("Impossivel calcular")
else:
    x1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
    x2=(-B-math.sqrt(B**2-4*A*C))/(2*A)
    print(f'''R1 = {x1:.5f}
R2 = {x2:.5f}''')
