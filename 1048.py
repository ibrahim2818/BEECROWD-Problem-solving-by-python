salary= round(float(input()), 2)

if salary <= 400:
    y= 15
elif salary <= 800:
    y=12
elif salary <=1200:
    y=10
elif salary <=2000:
    y=7
else:
    y=4
newSalary= salary+((y*salary)/100)

print(f'''Novo salario: {newSalary:.2f}
Reajuste ganho: {(newSalary-salary):.2f}
Em percentual: {y} %''')