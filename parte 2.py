#Emprestar livros
while True:
 nome = input("Digite o nome do livro que deseja emprestar(ou 'sair' para encerrar): ")
 if nome == 'sair':
     break
 if nome in biblioteca and biblioteca[nome]['quantidade'] > 0:
    biblioteca[nome]['quantidade'] -= 1
    print(f"O livro '{nome}' foi emprestado com sucesso!")
 else:
   print(f"O livro '{nome}' não está disponível no acervo.")

