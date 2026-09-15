matriz = [[50, 30], [20, 40]]

menor = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor < menor:
            menor = valor

print("Menor valor:", menor)