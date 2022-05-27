from random import randint
v =0
print('-=' * 20)
print('JOGO DO PAR OU ÍMPAR')
print('-=' * 20)
while True:
    j1 = int(input('Digite um numero: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? ')).strip().upper()[0]
    comp = randint(0, 11)
    soma = j1 + comp
    if pi =='P':
        if soma % 2 == 0:
            print('Você Ganhou!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif pi =='I':
        if soma % 2 == 1:
            print('Você Ganhou')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print(f'Você jogou {j1} e o computador {comp}. Total = {soma}', end='')
    print('Deu Par' if soma % 2 ==0 else 'Deu Ímpar')
print(f'FIM DE JOGO. Você ganhou {v} vezes consecutivas.')
