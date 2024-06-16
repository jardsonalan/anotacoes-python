start = input("Digite algo: ")

print(f"O tipo primitivo de {start} é {type(start)}")

print(f"Só tem espaços? {start.isspace()}")

print(f"É um número? {start.isnumeric()}")

print(f"É alfabético? {start.isalpha()}")

print(f"É alfanúmerico? {start.isalnum()}")

print(f"Está em maiúsculas? {start.isupper()}")

print(f"Está em minúsculas? {start.islower()}")

print(f"Está capitalizada? {start.istitle()}")