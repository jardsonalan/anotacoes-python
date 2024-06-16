import math

angulo = float(input("Informe o ângulo que você deseja: "))

angulo_radiano = math.radians(angulo)

seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f"O ângulo de {angulo}° tem o SENO de: {seno:.2f} \nO ângulo de {angulo}° tem o COSSENO de: {cosseno:.2f} \nO ângulo de {angulo}° tem a TANGENTE de: {tangente:.2f}")