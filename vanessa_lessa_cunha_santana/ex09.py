livros = []

for i in range(3):
    titulo = input(f"Informe o título do livro {i + 1}: ")
    livros.append(titulo)

print("\nLivros cadastrados:")

for titulo in livros:
    print(titulo)