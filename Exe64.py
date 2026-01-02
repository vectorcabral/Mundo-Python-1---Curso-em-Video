'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
num = soma = cont = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
print('Encerra Programa')
