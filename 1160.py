test_case= int(input())
for i in range(test_case):
    PA, PB, GA, GB= input().split()
    PA= int(PA)
    PB= int(PB)
    GA= float(GA)
    GB= float(GB)
    count=0
    while PB>=PA:
        rpa=int(PA*(GA/100))
        rpb=int(PB*(GB/100))
        count+=1
        PA+=rpa
        PB+=rpb
        if count>100:
            break
    if count>100:
        print(f'''Mais de 1 seculo.''')
    else:
        print(f'''{count} anos.''')

