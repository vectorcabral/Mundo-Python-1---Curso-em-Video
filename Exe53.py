'''
Digite uma frase:
 '''
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
palindromo = frase[::-1]
if frase == palindromo:
    print('A frase é um PALINDROMO')
else:
    print('Não é um PALINDROMO')
