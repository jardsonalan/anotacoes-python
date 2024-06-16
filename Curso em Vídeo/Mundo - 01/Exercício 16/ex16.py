# Importando o método math

import math

user = float(input("Informe um valor: "))

porcao_inteira = math.trunc(user)

print(f"O valor digitado foi {user} e sua porção inteira é {porcao_inteira}")

# Utilizando divisão inteira

valor = float(input("Informe um número: "))

pi = (valor // 1)

print(f"O valor digitado foi {valor} e sua porção inteira é {pi:.0f}")

# Utilizando int

number = float(input("Informe um número: "))

porcao_int = int(number)

print(f"O valor digitado foi {number} e sua porção inteira é {porcao_int}")