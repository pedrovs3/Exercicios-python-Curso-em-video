from datetime import date
atual = date.today().year
data = int(input('Qual o seu ano de nascimento? R:'))
idade = atual - data
if idade == 18:
    print('Está no seu ano de alistamento!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Você ainda nao tem 18 anos e por isso ainda nao pode se alistar, Você terá que se alistar daqui a {saldo} anos \n Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Já passou do seu ano de alistamento á {saldo} anos!\n Seu ano de alistamento foi em {ano}')
