'''
Faça uma tabuada de um número que o usuário escolher, utilizando um laço for
'''
num = int(input('Digite um número para ve sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))
