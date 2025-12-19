'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrado uma mensagem no final, de acordo com a nota atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('REPROVADO')
elif 5.0 < media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
print(f'Tirando {nota1} e {nota2} sua média final foi {media:.2f}')
