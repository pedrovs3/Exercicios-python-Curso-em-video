menos = homens = maior = 0
while True:
    print('-' * 20)
    print('Cadastre uma Pessoa')
    print('-' * 20)
    idade = int(input('Idade: \n'))
    sexo = str(input('Sexo: [M/F] \n')).strip().upper()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-=' * 20)
    contin = str(input('Quer Continuar? [S/N]:\n'))
    while contin not in 'SsNn':
        contin = str(input('Quer Continuar? [S/N]:\n'))
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade <20:
        menos += 1
    if contin in 'Nn':
        break
print(f'Total de Pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo tem {homens} homens cadastrados. ')
print(f'E temos {menos} mulheres com menos de 20 anos.')