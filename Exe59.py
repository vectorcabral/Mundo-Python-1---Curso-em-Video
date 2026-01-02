'''
Crie um programa que leia dois valores de um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''
opcao = 0
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
while opcao != 5:
    print("=-="*10)
    print('''Escolha uma opção: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print('O resultado de {} + {} é {}'.format(valor1, valor2, valor1+valor2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(
            valor1, valor2, valor1*valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print('O número {} é maior que o número {}'.format(valor1, valor2))
        else:
            print('O número {} é maior que o número {}'.format(valor2, valor1))
    elif opcao == 4:
        valor1 = int(input('Digite o 1º valor: '))
        valor2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Sair do Programa')
