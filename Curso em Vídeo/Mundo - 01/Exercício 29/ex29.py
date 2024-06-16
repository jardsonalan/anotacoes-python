velocidade = float(input("Informe a velocidade que você estava: "))

limite = 80
precoMulta = 7
multa = ((velocidade - limite) * precoMulta)

if velocidade <= limite:
    print("\nParabéns!")

else:
    print(f"\nMULTADO! Você excedeu o limite permitido que é {limite}Km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")

print("\nTenha um bom dia! Dirija com segurança!")