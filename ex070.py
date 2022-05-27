totmil = total = menor = cont = barato = 0
print('-=' * 20)
print('LOJA DO PEDROVS')
print('-=' * 20)
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < preco:
        menor = preco
        barato = nome
    conti = ' '
    if conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if conti == 'N':
            break
print(f'O total da compra foi {total}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} custando {menor:.2f}')

