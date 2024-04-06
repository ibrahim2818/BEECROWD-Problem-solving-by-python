A, B, C= list(map(float,input().split()))
pi= 3.14159
triangle= 0.5*A*C
circle= pi*C*C
trapeziam= (A+B)/2*C
square= B*B
rectangle= A*B
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapeziam:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")