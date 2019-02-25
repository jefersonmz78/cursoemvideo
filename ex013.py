salário= float(input("Qual éo salário de funcionário? R$"))
novo = salário + (salário *5 / 100)
print('Um funcionário qua ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
