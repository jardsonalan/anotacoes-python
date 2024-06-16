dias = int(input("Informe a quantidade de dias que o carro foi alugado: "))
km = float(input("Quantos km foram rodados: "))

dias_preco = 60
km_rodado = 0.15

aluguel = ((dias * dias_preco) + (km * km_rodado))

print(f"O total a pagar é R${aluguel:.2f}")