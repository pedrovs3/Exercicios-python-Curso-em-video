n = int(input('Digite um numero: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n \033[mO numero {n}, foi divisivel por {div} vezes')
if div == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NAO é primo!')