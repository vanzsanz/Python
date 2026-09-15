matriz = [[10, 25], [30, 15]]

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print("Maior valor:", maior)