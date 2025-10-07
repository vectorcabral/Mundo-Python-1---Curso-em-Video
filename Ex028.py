'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
import random
num = int(input('Digite um número: '))
numero = random.randint(1,5)
if num == numero:
    print('Parabéns! Você advinhou o número!')
    print('O número escolhido foi {} e o número que você digitou foi {}'.format(numero,num))
else:
    print('Não desista! Tente de novo')  
    print('O número escolhido foi {} e o número que você digitou foi {}'.format(numero,num))  
print('-'*12,'FIM','-'*12)