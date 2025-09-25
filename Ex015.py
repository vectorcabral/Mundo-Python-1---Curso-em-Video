'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele 
foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
dias = int(input('Quantos dias o carro foi alugado? '))
dist = float(input('Qual a foi a quantidade de Km percorrido? '))
valor = dias * 60
km = dist * 0.15
print('O valor a ser pago pelo aluguel do carro, considerando {} dias de uso e uma distância percorrida de {} km, é de R$ {:.2f}'.format(dias,dist,(valor+km)))