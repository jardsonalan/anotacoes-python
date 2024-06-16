import random

aluno1 = input("Informe o nome do primeiro aluno: ")
aluno2 = input("Informe o nome do segundo aluno: ")
aluno3 = input("Informe o nome do terceiro aluno: ")
aluno4 = input("Informe o nome do quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

sorteador = random.choice(lista_alunos)

print(f"O aluno escolhido foi: {sorteador}")