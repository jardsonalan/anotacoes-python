produto = float(input("Informe o valor do produto: R$"))

desconto = (5/100)

produto_desc = (produto - (produto * desconto))

print(f"O produto que custava R${produto}, após o desconto de 5%, passou a custar R${produto_desc:.2f}")