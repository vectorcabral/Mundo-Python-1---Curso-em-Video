'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
digito = input('Digite algo: ')
print('É um número?', digito.isalnum())
print('É um alfabético?', digito.isalpha())
print('É alfanumérico?', digito.isalnum())
print('É um número decimal? ', digito.isdecimal())
print('Está em minúsculo?', digito.islower())
print('Está em maiusculo?', digito.isupper())
print('É somente espaços?', digito.isspace())
print('Está capitalizada?', digito.istitle())
