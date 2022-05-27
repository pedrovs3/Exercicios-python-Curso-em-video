somaidade = 0
maioridadeM = 0
nomevelho = 0
totmulher20 = 0

for c in range(1, 5):
    print('=' * 5, f'{c}º PESSOA', '=' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadeM = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadeM:
        maioridadeM = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A media de idade do grupo é {mediaidade}')
print(F'O homem mais velho é o {nomevelho} e ele tem {maioridadeM} anos.')
print(f'Ao todo sao {totmulher20} mulheres com mais de 20 anos')
