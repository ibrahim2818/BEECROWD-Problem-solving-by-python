name= input()
fixedSalary= round(float(input()),2)
totalSales= round(float(input()),2)
bonus= (totalSales*15)/100
totalsalary= fixedSalary+bonus
print(f"TOTAL = R$ {totalsalary:.2f}")