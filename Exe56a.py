'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
-> A média de idade do grupo;
-> Quao é o nome do homem mais velho;
-> Quantas mulheres tem menos de 20 anos
'''
SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
NomeVelho = 0
TotMulher20 = 0

for c in range(1, 5):
    print(' ---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    SomaIdade += idade

    if c == 1 and sexo in 'Mm':
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Mm' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        TotMulher20 += 1

MediaIdade = SomaIdade/4
print('A média de idade do grupo é de {} anos'.format(MediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(
    MaiorIdadeHomem, NomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(TotMulher20))
