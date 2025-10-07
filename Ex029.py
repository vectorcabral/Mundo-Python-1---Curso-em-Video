'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai
custar R$7,00 por cada km acima do limite.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
veloc = float(input('Digite a velocidade do carro: '))
multa = 7
if veloc > 80.0:
    print('Você ultrapassou o limite de velocidade. Sua velocidade foi de {} Km/h e a multa é R${:.2f}'.format(veloc,((veloc-80)*multa)))
else:
    print('Tenha um bom dia! Diriga com segurança!')