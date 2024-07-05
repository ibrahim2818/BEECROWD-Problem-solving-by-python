n= int(input())
q=[]
in_range = 0
ou_range = 0
for i in range(1,n+1):
    q.append(int(input()))
for j in q:
    if j >=10 and j <=20:
        in_range+=1
    else:
        ou_range+=1
print(f'''{in_range} in
{ou_range} out''')