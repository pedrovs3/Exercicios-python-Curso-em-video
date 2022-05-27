n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
soma = (n1 + n2) / 2
if soma < 5.0:
    print(f'A media do aluno foi {soma}\n Portanto o aluno foi REPROVADO!')
elif 5.0 <= soma <= 6.9:
    print(f'A média do aluno foi {soma} \n Portanto o aluno esta de RECUPERAÇAO!')
elif soma> 7.0:
    print(f'A média do aluno foi {soma}\n Portanto o aluno foi APROVADO!')
