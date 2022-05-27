from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? \n'))
    idade = atual - ano
    if idade > 21:
        maior += 1
    else:
        menor += 1
print(f'No total de pessoas temos {maior} maiores de idade \n E {menor} menores de idade. ')
