'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo
com a idade:
-> Até 09 anos: MIRIM
-> Até 14 anos: INFANTIL
-> Até 19 anos: JUNIOR
-> Até 25 anos: SÊNIOR
-> Acima: MASTER
'''
from datetime import date
ano_nasc = int(input("DIgite seu ano de nascimento: "))
hoje = date.today()
idade = hoje.year - ano_nasc
print(f'Você tem {idade} anos de idade')
if idade <= 9:
    print('Sua categoria na Natação é MIRIM')
elif idade <= 14:
    print('Sua caregoria na Natação é INFANTIL')
elif idade <= 19:
    print('Sua categoria na Natação é JUNIOR')
elif idade <= 25:
    print('Sua categoria na Natação é SÊNIOR')
else:
    print('Sua categoria na Natação é MASTER')
