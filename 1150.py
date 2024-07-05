x= int(input())
while True:
    z= int(input())
    if z>x:
        break
p= x
total=0
count=0
while True:
    total=total+p
    count=count+1
    if total >=z:
        break
    
    p+=1
print(count)