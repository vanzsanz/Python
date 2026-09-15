matriz = [[10, -5, 8], [-3, 7, 0], [4, -2, 6]]

positivos = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            positivos += 1

print("Quantidade de valores positivos:", positivos)