'''
Crie um programa que faça o computador jogar JOKENPÔ com você
'''
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?\n'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('-'*25)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-'*25)

if computador == 0:  # PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU 😆 🎉')
    elif jogador == 2:
        print('COMPUTADOR VENCEU 🤖 🎉')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:  # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU 🤖 🎉')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU 😆 🎉')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:  # TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU 😆 🎉')
    elif jogador == 1:
        print('COMPUTADOR VENCEU 🤖 🎉')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')
