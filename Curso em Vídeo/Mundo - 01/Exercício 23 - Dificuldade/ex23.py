number = int(input("Informe o número: "))

und = number // 1 % 10
dzn = number // 10 % 10
ctn = number // 100 % 10
mlh = number // 1000 % 10

print(f"\nAnalizando número: {number}")

print(f"\nUnidade: {und}")
print(f"Dezena: {dzn}")
print(f"Centena: {ctn}")
print(f"Milhar: {mlh}\n")