import random

numero_sorteado = random.randint(1, 10)

numero = int(input("Digite um número de 1 a 10: "))

if numero == numero_sorteado:
    print("Você acertou!")
else:
    print("Você errou! O número sorteado foi:", numero_sorteado)