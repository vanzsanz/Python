alunos = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

print("\nRegistros dos alunos:")

for nome, nota in alunos.items():
    print("Nome:", nome,". Nota:", nota)