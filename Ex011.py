'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
A = float(input('Digite a altura da parede: '))
L = float(input('Digite a largura da parede: '))
a = A*L
print('Para pintar uma parede com uma área de {:.2f} m² será necessário {:.1f} litros de tinta'.format(a,a/2))