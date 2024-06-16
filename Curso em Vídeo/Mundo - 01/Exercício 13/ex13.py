salario = float(input("Informe o salário do funcionário: R$"))

valor_aumento = (15/100)

aumento = (salario + (salario * valor_aumento))

print(f"O funcionário que ganhava R${salario:.2f}, após o aumento de 15%, passou a receber R${aumento:.2f}")