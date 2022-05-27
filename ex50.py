soma = 0
count = 0
for c in range(1, 7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        soma += valor
        count += 1
if count > 1:
    print(f'Você informou {count} valores PARES e a soma dos mesmos é: {soma}')
else:
    print(f'Você informou {count} valor PAR e a soma do mesmo é: {soma}')
