resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero:'))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} valores e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
