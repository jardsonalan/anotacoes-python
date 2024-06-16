import random

aluno1 = input("Informe o primeiro aluno: ")
aluno2 = input("Informe o segundo aluno: ")
aluno3 = input("Informe o terceiro aluno: ")
aluno4 = input("Informe o quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

sorteador = random.sample(lista_alunos, k=len(lista_alunos)) # Ou utiliza random.shuffle(lista_alunos)

print(f"A ordem de apresentação será: \n \n{sorteador}")