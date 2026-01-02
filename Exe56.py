contM = 0
contF = 0

for c in range(1, 4):
    print(f'{"-"*5} {c}ª PESSOA {"-"*5}')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    print('Seu nome: {} | Sua idade: {} | Seu gênero: {}'. format(nome, idade, sexo))
media = idade/c
print('A média de idade do grupo é de {:.1f} anos'.format(media))
if sexo == 'M':
    contM = 1
    print('Ao todo são {} homens no grupo')
if sexo == 'F':
    contF = 1
    print('Ao todo são {} mulheres no grupo')
