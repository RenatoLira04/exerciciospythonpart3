enuciado = str(input('Vou pensar em um número entre 0 e 5. Tente adivinhar...'))
pergunta = int(input('E que número eu pensei?'))
print('O numero que você pensou foi: {}'.format(pergunta))
if pergunta == 3:
    print('Parabéns você ganhou!')
else:
    print('O computador ganhou')