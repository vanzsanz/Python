total = 0

for i in range(10):
    quantidade = int(input(f"Digite a {i + 1}ª quantidade de cestas arrecadadas: "))
    total += quantidade

print("Total de cestas arrecadadas:", total)