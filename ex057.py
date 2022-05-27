sexo = str(input('Digite o sexo de uma pessoa [M / F]:\n')).strip().upper()[0] #pega apenas a primeira letra#
while sexo not in 'M''F':
    sexo =str(input('Dado inválido. Digite novamente! \n').strip().upper())
print(f'Sexo {sexo} registrado com sucesso!')
'''if (sexo == 'M'):
    print(f'Sexo M registrado com sucesso!')
if (sexo == 'F'):
    print('Sexo F registrado com sucesso!')'''
