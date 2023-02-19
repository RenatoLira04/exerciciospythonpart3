velocidade = float(input('A velocidade do carro é:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado, sua multa é R${:.2f}'.format(multa))
else:
    print('Boa viagem!')