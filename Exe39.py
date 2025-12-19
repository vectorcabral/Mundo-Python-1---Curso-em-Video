'''
Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade, se ele vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo de alistamento. 
Seu programa também devera mostrar o tempo que falta ou o tempo que passou do prazo.
'''
from datetime import date, datetime

nasc = datetime.strptime(
    input('Digite a sua data de nascimento (dd/mm/aaaa): '), '%d/%m/%Y').date()
hoje = date.today()
idade = hoje.year - nasc.year

if (hoje.month, hoje.day) < (nasc.month, nasc.day):
    idade -= 1  # porque?
print(f'Você nascem em: {nasc.strftime('%d/%m/%Y')}')
print(f'Você tem {idade} anos de idade')

if idade < 18:
    saldo = 18 - idade
    print('Você não tem idade para se alistar nas forças armadas esse ano! Ainda falta {} anos para o alistamento'.format(saldo))
elif idade == 18:
    print('Você deve se alistar nas forças armadas esse ano!')
else:
    atraso = idade - 18
    print('Você deve se alistar nas forças armadas! Você está {} atrasado para o alistamento!'.format(atraso))
