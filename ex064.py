num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: \n'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: \n'))
print(F'Você digitou {cont} números e a soma entre eles é: {soma}')
