kg = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = kg / (alt ** 2)
print(f'O IMC dessa pessoa é: {imc:.1f}')
if imc < 18.5:
    print('Você esta abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('PARABENS!, Seu IMC esta na faixa de peso ideal!')
elif 25 <= imc < 30:
    print('Cuidado, você está com sobrepeso!')
elif 30 <= imc < 40:
    print('CUIDADO, você esta com obesidade!')
else:
    print('CUIDADO, Você está com obesidade mórbida')
