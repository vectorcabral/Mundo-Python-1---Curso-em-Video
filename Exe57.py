'''
Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente
até ter um valor correto
'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: ')).upper()
    if sexo == 'M':
        print('Masculino')
    elif sexo == 'F':
        print('Feminino')
    else:
        print('Sexo não informado. Digite M ou F')
print('Você informou sexo {}'.format(sexo))
