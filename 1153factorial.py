while True:
    x= int(input())
    if x>0 and x<13:
        break
p=1
while x>0:
    p=p*x
    x-=1
print(p)
