print('-=' *10 )
print('GERADOR DE PA')
print('-=' *10)
pt = int(input('Digite o valor do primeiro termo da PA:\n'))
r = int(input('Digite o valor da razão:\n'))
term = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <=total:
        print(f'{term} =>', end='')
        term += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você gostaria de ver? \n'))
print(f'Progressao finalizada com {total} termos!')
