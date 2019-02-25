casa = float(input('Valor da casa: R$'))
salário = float(input('Salário da comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos *12)
mínino = salário * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos), end= ' ')
print(' a prestação será de R${:.2f}'.format(prestação))
#print(' COMPARANDO tem que pagar {} e o mínimo é de {}'.format(prestação,mínino))
if prestação <= mínino:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')