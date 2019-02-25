num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECINAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(' {}converter para BINÁRIO é igaul a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{}converter para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{}converter para HEXADECINAL é igual a {}'.format(num,hex(num)[:2]))
else:
    print('opção inválida. Tente novamente. ')