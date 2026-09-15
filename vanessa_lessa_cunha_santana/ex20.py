total = 0

nota = float(input("Digite uma nota (0 para finalizar): "))

while nota != 0:
    total += nota
    nota = float(input("Digite uma nota (0 para finalizar): "))

print("A soma das notas é:", total)