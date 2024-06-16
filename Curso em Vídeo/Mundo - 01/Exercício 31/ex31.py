distancia = float(input("Informe a distância da sua viagem: "))

print(f"Você está prestes a fazer uma viagem de {distancia}Km.")

distanciaCobranca = 200

viagemCurta = 0.50
viagemLonga = 0.45

cobrancaCurta = (distancia * viagemCurta)
cobrancaLonga = (distancia * viagemLonga)

if distancia <= distanciaCobranca:
    print(f"E o preço da sua viagem será de R${cobrancaCurta:.2f}")

else:
    print(f"E o preço da sua viagem será de R${cobrancaLonga:.2f}")