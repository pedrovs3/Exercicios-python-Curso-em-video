n1 = float(input('Digite o valor da 1º Reta: '))
n2 = float(input('Digite o valor da 2º Reta: '))
n3 = float(input('Digite o valor da 3º Reta: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Essas retas PODEM formar um Triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
                print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esses segmentos NÃO podem formar um Triângulo!')
