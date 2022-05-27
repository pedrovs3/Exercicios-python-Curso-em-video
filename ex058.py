from random import randint
count = 0
pc = randint(0, 10)
print('-=' * 20)
print('Diga um numero de 0 a 10 e tentarei adivinhar')
print('-=' * 20)
print('Vou pensar em um numero de 10 a 0, você consegue adivinhar?')
acerto = False
while not acerto:
    j1=int(input('digite um palpite:\n'))
    count += 1
    if j1 == pc:
        acerto = True
    else:
        if j1 < pc:
            print('Mais... tente mais uma vez.')
        elif j1 > pc:
            print('Menos... tente mais uma vez.')
print(f'Parabens! Você ACERTOU usando {count+1} tentativas!')
'''if j1 == pc:
    print('PARABENS, você ganhou de primeira!')
else:
    while j1 >= pc:
        j1 = int(input('Menos...Tente mais uma vez:\n'))
        count += 1
    if j1<=pc:
        j1 = int(input('Mais... Tente mais uma vez:\n'))
        count += 1'''