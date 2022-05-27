from datetime import date

atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
idade = atual - ano
print(f'A Idade do atleta é: {idade}')
if idade <= 9:
    print(f'Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
