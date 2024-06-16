user = int(input("Informe um número: "))

dobro = (user * 2)
triplo = (user * 3)
rq = (user ** (1/2)) # Ou utiliza pow(user, (1/2))

print(f"O dobro de {user} vale {dobro} \nO triplo de {user} vale {triplo} \nA raiz quadrada de {user} é igual a {rq:.2f}")