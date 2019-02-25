real= float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
euro = real  / 4.18
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EURO${:.2f}'.format(real, euro))