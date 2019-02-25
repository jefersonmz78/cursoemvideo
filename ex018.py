import math
ângulo = float(input(' Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem A TANGENTE de {:.2f}'.format(ângulo,tangente))