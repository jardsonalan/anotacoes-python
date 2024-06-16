import random
import time

print('-='*28)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-='*28)

number = int(input("Qual número você acha que estou pensando? "))

print("\nPROCESSANDO...")
time.sleep(2)

sorteador = random.randrange(6) #Ou utiliza random.randint(0, 5)

if number == sorteador:
    print(f"\nParabéns o número {number} era o que eu estava pensando!")

else:
    print(f"\nO número que pensei foi {sorteador}")
    print("\nOps! Não foi dessa vez, tente novamente!")

print("\n ------ FIM ------")