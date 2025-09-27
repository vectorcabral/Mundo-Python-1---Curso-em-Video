'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Faça um programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um triângulo e mostre o comprimento
da hipotenusa.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
from math import hypot
co = float(input('Digite um comprimento: '))
ca = float(input('Digite outro comprimento: '))
hip = hypot(co, ca)
print('O Triângulo cujo o Cateto Oposto é {:.2f} e o Cateto Adjacente é {:.2f}, tem sua hipotenusa no valor de {:.1f}'.format(co,ca,hip))
