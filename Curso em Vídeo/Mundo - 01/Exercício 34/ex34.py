salario = float(input("Informe o seu salário: "))

limite = 1250.00

if salario <= limite:
    aumento = (salario * 1.15)

else:
    aumento = (salario * 1.10)

print(f"Quem ganhava R${salario:.2f} passou a ganhar R${aumento:.2f} agora.")