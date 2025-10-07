'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a R$1.250,00 calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
num = float(input('Digite o salário: '))
salario = 1250
if num <= salario:
    print('Seu salário atual é de R$ {:.2f} e você terá um aumento de 15%. Seu novo salário é de R$ {:.2f}'.format(num,(num*1.15)))
else:
    print('Seu salário atual é de R$ {:.2f} e você terá um aumento de 10%. Seu novo salário é de R$ {:.2f}'.format(num,(num*1.10)))
