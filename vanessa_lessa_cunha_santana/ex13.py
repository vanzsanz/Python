setor1 = float(input("Digite o consumo do setor 1: "))
setor2 = float(input("Digite o consumo do setor 2: "))

if setor1 > setor2:
    print("O setor 1 teve o maior consumo.")
elif setor2 > setor1:
    print("O setor 2 teve o maior consumo.")
else:
    print("Os dois setores tiveram o mesmo consumo.")