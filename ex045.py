from random import randint
from time import sleep
list = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j1 = int(input('Qual vai ser sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=-' * 20)
print(f'O computador jogou {list[comp]}')
print(f'O jogador jogou {list[j1]}')
print('-=' * 20)
if comp == 0:
    if j1 == 0:
        print('\033[1;33mEMPATE!')
    elif j1 == 1:
        print('\033[1;32mO JOGADOR GANHOU!')
    elif j1 == 2:
        print('\033[1;31mO COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1:
    if j1 == 0:
        print('\033[1;31mO COMPUTADOR GANHOU!')
    elif j1 == 1:
        print('\033[1;33mEMPATE!')
    elif j1 == 2:
        print('\033[1;32mO JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 2:
    if j1 == 0:
        print('\033[1;32mO JOGADOR GANHOU!')
    elif j1 == 1:
        print('\033[1;31mO COMPUTADOR GANHOU!')
    elif j1 == 2:
        print('\033[1;33mEMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
