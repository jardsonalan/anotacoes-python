nome = str(input("Informe seu nome: ")).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nomeSespaco = len(''.join(nome.split()))
nomeDividido = nome.split()
leituraName = len(nomeDividido[0])

print("\nAnalisando nome...")
print(f"\nSeu nome em maiúsculas é {nome_maiusculo}")
print(f"Seu nome em minúsculas é {nome_minusculo}")
print(f"Seu nome ao todo tem {nomeSespaco}")
print(f"Seu primeiro nome é {nomeDividido[0]} e ele tem {leituraName} letras\n")