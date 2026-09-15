total = 0

for i in range(5):
    quantidade = int(input(f"Informe a quantidade arrecadada pelo voluntário {i + 1}: "))
    total += quantidade

print(f"Total arrecadado: {total}")