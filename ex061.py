p1 = int(input('Digite o Primeiro Termo:\n'))
r = int(input('Digite a razão:\n'))
termo = p1
c = 1
while c <= 10:
    print(f'{termo} =>', end='')
    termo += r
    c += 1
print('FIM!')

'''while c < ultimo + r:
    print(f'{c} -> ', end='')
    c += r
print('Acabou!')'''