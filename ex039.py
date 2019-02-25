from datetime import date
atual = date.today().year
nasc = int(input('Ano de narcimento:'))
#sexo = bool(input('Você é homem ou mulher:'))
idade = atual - nasc
print('Quem nasceu eu {} tem {} em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Vocâ já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))