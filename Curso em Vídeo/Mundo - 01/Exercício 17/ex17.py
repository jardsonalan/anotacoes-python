import math

oposto = float(input("Informe o comprimento do cateto oposto: "))
adjacente = float(input("Informe o comprimento do cateto adjacente: "))

hipo = (math.sqrt((math.pow(oposto, 2)) + (math.pow(adjacente, 2))))

print(f"Comprimento do cateto oposto: {oposto} \nComprimento do cateto adjacente: {adjacente} \nA hipotenusa vai medir: {hipo:.2f} \n")

# Utilizando o hypot

hi = math.hypot(oposto, adjacente)

print(f"Comprimento do cateto oposto: {oposto} \nComprimento do cateto adjacente: {adjacente} \nA hipotenusa vai medir: {hi:.2f}")