'''
Melhore o jogo do DESAFIO #28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar 
até acertar, mostrando no final quantos palpites foram necessário para vencer
'''
import random
num = 0
numero = random.randint(1, 10)
while num != numero:
    num = int(input('Digite um número: '))
    if num == numero:
        print('Parabéns! Você advinhou o número! 🥳')
        print('O número escolhido foi {} e o número que você digitou foi {}'.format(
            numero, num))
    else:
        print('Você errou! Tende novamente! 🙁')
        print('O número escolhido foi {} e o número que voc~e digitou foi {}'.format(
            numero, num))
print('-'*12, 'FIM', 12*'-')
