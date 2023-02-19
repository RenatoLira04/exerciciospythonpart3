viagem = float(input('Qual a distância da viagem?'))
print('Sua distância foi?{}'.format(viagem))
if viagem <=200:
    preço = viagem * 0.50
    print('Sua viagem custou R${:.2f}'.format(preço))
else:
    viagem >200
    preço = viagem * 0.45
    print('Sua viagem custou R${:.2f}'.format(preço))
