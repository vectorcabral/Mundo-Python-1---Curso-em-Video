'''
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________

Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e 
escrevendo o nome do escolhido.
________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________
'''
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
nomes = [n1, n2, n3, n4]
nome_escolhido = random.choice(nomes)
print('O aluno escolhido foi: {}'.format(nome_escolhido))