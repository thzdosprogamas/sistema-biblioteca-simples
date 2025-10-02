#Devolver livros
while True:
 nome_devolucao = input("Digite o nome do livro que deseja devolver(ou 'sair' para encerrar): ")
 if nome_devolucao == 'sair':
     break
 if nome_devolucao in biblioteca and biblioteca[nome_devolucao]['quantidade'] < biblioteca[nome_devolucao]['estoque']:
    biblioteca[nome_devolucao]['quantidade'] += 1
    print(f"O livro '{nome_devolucao}' foi devolvido com sucesso!")
 else:
   print(f"O livro '{nome_devolucao}' não está disponível no acervo.")


