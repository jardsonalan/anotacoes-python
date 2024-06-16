frase = str(input("Informe sua frase: ")).strip()

key = 'A'

fraseUpper = frase.upper()
countA = fraseUpper.count(key)
initialFind = (fraseUpper.find(key) + 1)
finalFind = (fraseUpper.rfind(key) + 1)

print(f"A letra {key} aparece {countA} nesta frase")
print(f"A primeira letra {key} aparece na posição {initialFind}")
print(f"A última letra {key} aparece na posição {finalFind}")