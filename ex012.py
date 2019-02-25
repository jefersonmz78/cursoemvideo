preço: float = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, Na promoção com desconto de 5% vai custar R${}'.format(preço, novo))
