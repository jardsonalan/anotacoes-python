numA = int(input("Informe o primeiro número: "))
numB = int(input("Informe o segundo número: "))
numC = int(input("Informe o terceiro número: "))

if numB > numA and numB > numC:
    print(f"O maior número é {numB}")

if numC > numA and numC > numB:
    print(f"O maior número é {numC}")

if numA > numC and numA > numB:
    print(f"O maior número é {numA}")

if numB < numA and numB < numC:
    print(f"O número menor é {numB}")

if numA < numB and numA < numC:
    print(f"O número menor é {numA}")

if numC < numA and numC < numB:
    print(f"O número menor é {numC}")