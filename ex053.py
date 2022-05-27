frase = str(input('Digite uma frase: ')).strip().upper()
separaçao = frase.split()
junçao = ''.join(separaçao)
print(f'Voce digitou a frase: \n{junçao}')
inverso = ''
for letra in range(len(junçao) - 1, -1, -1):
    inverso += junçao[letra]
print(inverso)
if inverso == junçao:
    print('Essa palavra É um palindromo')
else:
    print('Essa palavra NAO é um palindromo')