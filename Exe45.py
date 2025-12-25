import random
from time import sleep
print('Escolha uma opção para jogar "Pedra, Papel ou Tesoura"\n'
      '[1] PEDRA\n'
      '[2] PAPEL\n'
      '[3] TESOURA')

jogo = int(input('Escolha sua opção: '))
escolha = random.randint(1, 3)

conversao = {1: 'PEDRA',
             2: 'PAPEL',
             3: 'TESOURA'}

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

if jogo not in conversao:
    print('Opção inválida!')

else:
    print(f'Jogador escolheu {conversao[jogo]}')
    print(f'Computador escolheu {conversao[escolha]}')

    if jogo == escolha:
        print('EMPATE!!!')

    elif (jogo == 1 and escolha == 2) or \
         (jogo == 2 and escolha == 3) or \
         (jogo == 3 and escolha == 1):
        print('Jogador PERDEU 😢')

    else:
        print('Jogador GANHOU 🎉')
