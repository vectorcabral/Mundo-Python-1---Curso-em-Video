'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Crie um programa que leia o nome completo de uma pessoa e mostre:
🔵 O nome completo com todas as letras maiúsculas:
🔵 O nome completo com todas as letras minúsculas:
🔵 Quantas letras ao todo (sem considerar espaços):
🔵 Quatas letras tem o primeiro nome?
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
nome = str(input('Digite seu nome: '))
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome.replace(" ",""))))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))