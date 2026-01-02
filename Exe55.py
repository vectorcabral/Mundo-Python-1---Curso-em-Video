'''
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
lista = []
for c in range(1, 6):
    print('Peso da {}ª pessoa: '.format(c))
    peso = float(input(''))
    lista.append(peso)
lista.sort()
print('O maior peso lido foi de {}'.format(lista[-1]))
print('O menor peso lido foi de {}'.format(lista[0]))
