from time import sleep
n1 = int(input('Digite um valor:\n '))
n2 = int(input('Digite outro Valor:\n '))
print('O que gostaria de fazer com os numeros? ')
c = 0
maior = 0
while c == 0:
    print('-=' * 50)
    option = int(input('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ]Sair do programa
    R:'''))
    if option == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é: {soma}')
        sleep(0.5)
    elif option == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores {n1} e {n2} é: {mult}')
        sleep(0.5)
    elif option == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'entre {n1} e {n2} o maior é {n2}')
        sleep(0.5)
    elif option == 4:
        n1 = int(input('Digite um valor:\n'))
        n2 = int(input('Digite outro valor:\n'))
        sleep(0.5)
    elif option == 5:
        print('Finalizando',end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.', end='\n')
        sleep(0.7)
        print('Fim do Programa. Volte Sempre!')
        quit()
    else:
        print('Opção inválida. Tente novamente!')
        sleep(0.5)
