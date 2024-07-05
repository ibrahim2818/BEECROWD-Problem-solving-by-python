A, B, C, D = list(map(float, input().split()))
weightA = 2
weightB = 3
weightC = 4
weightD = 1

AvgWeight = ((A * weightA) + (B * weightB) + (C * weightC) + (D * weightD)) / (weightA + weightB + weightC + weightD)

print(f'Media: {AvgWeight:.1f}')

if AvgWeight >= 7:
    print('Aluno aprovado.')
elif AvgWeight < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    marks = round(float(input()), 1)
    total = (AvgWeight + marks) / 2

    print(f'Nota do exame: {marks:.1f}')
    
    if total >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {total:.1f}')
