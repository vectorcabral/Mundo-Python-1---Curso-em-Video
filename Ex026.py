'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes a aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição {} da frase.'.format(frase.find('A')+1))
print('A última letra "A" aparece na posição {} da frase.'.format(frase.rfind('A')))