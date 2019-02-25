from random import randint
from time import sleep
comptador = randint(0,5)# Faz o computador "PENSAR"
'''print('Pensei no número {}'.format(Computador))'''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))# Jogador tenta adivinhar
print(' processando...')
sleep(2)
if jogador == comptador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! EU pensei no número {} e não no {}!'.format(comptador,jogador))