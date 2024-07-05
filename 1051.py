A=round(float(input()), 2)
if A<=2000.00:
    print("Insento")
elif A<=3000.00:
    x=(A-2000)*(8/100)
    print(f'''R$ {x:.2f}''')

elif A<=4500.00:
    x=(A-3000)*(18/100)+ 80
    print(f'''R$ {x:.2f}''')
elif A>=4500.00:
    x=(A-4500)*(28/100)+ 350
    print(f'''R$ {x:.2f}''')