from time import sleep
print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
sleep(0.5)
p1 = int(input('Primeiro termo da Progressão Aritmética: '))
r = int(input('Razão da Progressão: '))
n = 10
ultimo = p1 + (n - 1) * r
ultimo += 1

for c in range(p1, ultimo, r):
    print(F'{c} ->', end=' ')
print('FIM')
