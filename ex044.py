valor = float(input('Preço das compras: '))
pagamento = int(input('Qual a forma de pagamento? \n [1] Á vista dinheiro/cheque \n [2] Á vista Cartão \n [3] Até 2x '
                      'no Cartão \n [4] 3x ou mais no Cartão \n Qual seria a opçao?: '))
if pagamento == 1:
    total = (10 * valor) / 100
    print(f'No pagamento a vista há um desconto de 10%, portanto o total da compra é: R${valor - total:.2f}')
elif pagamento == 2:
    total = (5 * valor) / 100
    print(f'Á vista no cartão há um desconto de 5%, sendo assim o valor total fica: R${valor - total}')
elif pagamento == 3:
    parcela = valor / 2
    print(f'Para esta forma de pagamento nao há desconto, o valor total é: R${valor} e as parcelas sao de: R${parcela} ')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas?: '))
    total = (20 * valor) / 100
    print(f'Com essa forma de pagamento o valor por parcela fica de R${(valor + total) / parcelas}, sendo o valor total: R${valor + total}')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')
