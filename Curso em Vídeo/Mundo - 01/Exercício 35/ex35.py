ladoA = float(input("Informe a primeira largura: "))
ladoB = float(input("Informe a segunda largura: "))
ladoC = float(input("Informe a terceira largura: "))

if (ladoA < (ladoB + ladoC)) and (ladoB < (ladoA + ladoC)) and (ladoC < (ladoA + ladoB)):
    print("É possível formar um TRIÂNGULO! ")

else:
    print("Não é possível formar um TRIÂNGULO! ")