'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores'''

from datetime import date

hoje = date.today().year
soma = 0
totmaior = 0
totmenor = 0


for c in range(1, 8):
    soma += 1
    print('Digite o ano que a {}ª pessoa nasceu: '.format(soma))
    nasc = int(input(''))
    idade = hoje - nasc
    print('Idade da {}ª pessoa é {} anos'.format(soma, idade))
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'. format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
