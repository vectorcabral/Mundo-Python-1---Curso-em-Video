'''
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
    e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
    '''

valor_casa = float(input('Qual o valor da casa desejada?: R$ '))
valor_salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Quantos anos de fincanciamento?: '))
prestacao = valor_casa/(anos*12)
print('Para pagar uma casa de R$ {:.2f} em {} anos'. format(
    valor_casa, anos), end='')
print(' a prestação será de {:.2f}'.format(prestacao))

if prestacao <= (valor_salario*0.3):
    print('Emprétimo APROVADO')
else:
    print('Emprestimo NEGADO')
