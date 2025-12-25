'''
Crie um programa que mostra na tela todos os números pares que estão no intervalo entre 01 e 50.
'''

num = int(input('Digite um número: '))
for c in range(0, num, 2):
    print(c, end=' ')
