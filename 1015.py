x1, y1= list(map(float,input().split()))
x2, y2= list(map(float,input().split()))
distance= (((x2-x1)**2)+ ((y2-y1)**2))**0.5
print(f"{distance:.4f}")