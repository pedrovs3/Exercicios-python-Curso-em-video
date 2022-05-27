n = int(input('Digite um numero para saber seu fatorial:\n'))
c = n
print(f'Calculando {n}! = ')
soma = 0
f = 1
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f' {f}')
'''for p in range(5, 0, -1):
    print(f'{p} ',end='')
    print(f' x ' if p > 1 else ' = ',end='')
    f = f * p
    soma += f
    print(soma)'''
