'''
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeir valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são iguais
'''
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro valor {}, é maior que o segundo valor {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor {}, é maior que o primeiro valor {}'.format(num2, num1))
else:
    print('O primeiro valor {} e o segundo valor {} são iguais'.format(num1, num2))
