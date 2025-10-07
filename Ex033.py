'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Faça m programa que leia três números e mostre qual é o maior e qual é o menor deles.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# Verificando quem é o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a < b and a < c:
    menor = a

# Verificando quem é o maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a > b and a > c:
    maior = a

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
