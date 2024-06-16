city = str(input("Informe sua cidade: ")).strip()

cityUpper = city.upper()

key = 'SANTO'

verificador = (cityUpper[:5] in key)

print(verificador)