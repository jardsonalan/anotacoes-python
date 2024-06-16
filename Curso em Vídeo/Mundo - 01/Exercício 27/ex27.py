name = str(input("Informe seu nome completo: ")).strip()

titleName = name.title()
nameDivisor = titleName.split()

lenName = len(nameDivisor)

intNumber = (int(lenName) - 1)

primeiroName = (nameDivisor[0])

ultimoName = (nameDivisor[intNumber])

print("\nPrazer em te conhecer!\n")

print(f"Seu primero nome é: {primeiroName}")
print(f"Seu último nome é: {ultimoName}\n")