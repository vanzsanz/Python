tupla = ("Matematica", "Portugues")

dicionario = {}

for i in range (5):
    nome = input("Digite o nome do estudante: ")
    matematica = float(input("Digite a nota de Matemática: "))
    portugues = float(input("Digite a nota de Português: "))
    dicionario[nome] = (matematica, portugues)
    
print("\nDisciplinas cadastradas:")
for disciplinas in tupla:
    print(disciplinas)
    
print("\nDesempenho dos alunos:")

for nome, notas in dicionario.items():
    media = (notas[0] + notas[1]) / 2

    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    print("\nNome:", nome)
    print("Média:", media)
    print("Resultado:", resultado)
