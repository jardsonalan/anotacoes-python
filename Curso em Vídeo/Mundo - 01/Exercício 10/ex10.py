user = float(input("Informe o valor que você tem: R$"))

dolar = 5.12
euro = 5.45

dolar_c = (user / dolar)
euro_c = (user / euro)

print(f"Com R${user} você pode comprar ter: \nUS${dolar_c:.2f} \nEUR${euro_c:.2f}")