medicamentos = {}

for i in range(5):
    nome = input("Digite o nome do medicamento: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    medicamentos[nome] = quantidade

nome_consulta = input("Digite o nome do medicamento para consultar: ")

if nome_consulta in medicamentos:
    print("Quantidade em estoque:", medicamentos[nome_consulta])
else:
    print("Medicamento não encontrado.")