soma = cont = 0
while True:
    num = int(input('Digite um valor ( 999 para Parar ) : \n'))
    if num == 999:
        break
    cont += 1
    soma+= num
print(f'Você digitou {cont} valores e a soma entre eles é: {soma}')
