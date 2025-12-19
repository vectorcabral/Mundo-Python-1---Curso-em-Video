'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, alcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-> Abaixo de 18.5: Abaixo do Peso
-> Entre 18.5 e 25: Peso ideal
-> Entre 25.0 até 30.0: Sobrepeso
-> Entre 30. até 40.0: Obesidade
-> Acima de 40.0: Obesidade mórbida
'''
peso = float(input('Qual o seu peso?: '))
altura = float(input('Digite sua altura em metros?: '))
imc = peso / (altura*altura)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} você está ABAIXO DO PESO')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f} você está com o PESO IDEAL')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2f} você está com SOBREPESO')
elif imc <= 40:
    print(f'Seu IMC é {imc:.2f} você está com OBESIDADE')
else:
    print(f'Seu IMC é {imc:.2f} você está com OBESIDADE MÓRBIDA')
