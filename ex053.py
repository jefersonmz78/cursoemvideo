frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso = junto[::-1]
print('O inverso {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Termos um pslíndromo! ')
else:
    print('A frase digitada não é um palíndromo! ')
