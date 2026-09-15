total = 0

for i in range(7):
    venda = float(input(f"Digite o valor da venda do {i + 1}º dia: "))
    total += venda

print(f"Faturamento total da semana: R$ {total}")