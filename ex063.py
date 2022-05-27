print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)
num = int(input('Quantos termos voce quer mostrar? \n'))
t1 = 0
t2 = 1
c = 3
print(f'{t1} -> {t2}', end='')
while c <= num:
    t3 = t1  + t2
    print(f' -> {t3}', end='')
    t1 =t2
    t2 =t3
    c += 1
print(' -> FIM')
