velocidade = float(input('Qual é a velocidade atual do carro? ' ))
if velocidade > 80:
    print('MULTADO! Você execedeu p limite pertido que é de 80Km/h')
    multa = (velocidade -80) * 7
    print(' Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenho um bom dia! Diria com segurança ')