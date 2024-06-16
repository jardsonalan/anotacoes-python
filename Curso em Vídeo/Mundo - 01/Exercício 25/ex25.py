name = str(input("Informe seu nome: ")).strip()

nameUpper = name.upper()

key = "SILVA"

verificador = (key in nameUpper)

print(f"O seu nome tem Silva? {verificador}")