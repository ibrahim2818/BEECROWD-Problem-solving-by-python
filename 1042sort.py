A, B, C= list(map(int,input().split()))
x=[A, B, C]
def sort(a,b,c):
    num = [a,b,c]
    num.sort()
    return num
result = sort(A,B,C)
print (f'''{result[0]}\n{result[1]}\n{result[2]}\n\n{x[0]}\n{x[1]}\n{x[2]}''')