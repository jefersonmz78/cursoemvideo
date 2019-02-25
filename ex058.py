from random import randint
comptador = randint(1 , 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == comptador:
        acertou = True
    else:
        if jogador < comptador:
            print('Mais...Tente uma vez.')
        elif jogador >comptador:
            print('Menos... Tente mais umz vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))