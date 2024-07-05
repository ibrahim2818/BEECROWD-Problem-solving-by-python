x= int(input())
y= int(input())
A= [x,y]
A.sort()
p= A[0]
q= A[1]
p= int(p)
q= int(q)
count=0
for i in range(p+1, q):
    if i%2 ==1:
        count= count + i

print(count)