largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = (largura * altura)

tinta = (area / 2)

print(f"Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m^2.")
print(f"Para pintar essa parede, você precisará de {tinta}l de tinta.")