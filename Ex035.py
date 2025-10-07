'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
print('Analisador de Triângulo\n')
a = int(input('Digite um lado do triângulo: '))
b = int(input('Digite outro lado do triângulo: '))
c = int(input('Digite mais um lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Essas medidas formam um triângulo')
else:
    print('Essas medidas NÃO formam um triângulo')