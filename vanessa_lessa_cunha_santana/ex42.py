matriz = [[10, 20], [30, 40]]

soma = 0

for linha in matriz:
    for valor in linha:
        soma += valor

print("Soma dos valores:", soma)