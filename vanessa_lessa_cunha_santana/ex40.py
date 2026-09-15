import random

numero_sorteado = random.randint(1, 10)

tentativa = int(input("Digite um número de 1 a 10: "))

while tentativa != numero_sorteado:

    if numero_sorteado > tentativa:
        print("O número procurado é maior.")
    else:
        print("O número procurado é menor.")

    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")