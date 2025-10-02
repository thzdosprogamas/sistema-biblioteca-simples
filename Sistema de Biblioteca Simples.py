#todas as partes foram feitas por mim, separadas para eu entender melhor e com facilidade, poucas coisas foram ajustadas pelo chato(deixar mais profissional e mais bonito de certa forma), o chat é meio q o mei 'professor' nesse assunto.
#feito por: M.W

# parte 1
biblioteca = {}
while True:
    nome_livro = input("Digite o nome do livro (ou 'sair' para encerrar): ")
    if nome_livro.lower() == 'sair':
        break
    autor_livro = input("Digite o nome do autor: ")
    quantidade_livro = int(input("Digite a quantidade de exemplares: "))
    biblioteca[nome_livro] = {'autor': autor_livro, 'quantidade': quantidade_livro, 'estoque': quantidade_livro}
    if quantidade_livro == 1:
        print(f"O livro '{nome_livro}' de {autor_livro} com {quantidade_livro} exemplar foi adicionado ao acervo.")
    else:
        print(f"Os livros '{nome_livro}' de {autor_livro} com {quantidade_livro} exemplares foram adicionados ao acervo.")

print('No nosso acervo temos:')
for livro, detalhes in biblioteca.items():
    autor = detalhes['autor']
    quantidade = detalhes['quantidade']
    print(f"Os livros são: '{livro}', pelo autor: {autor}, com a quantidade: {quantidade}")


# parte 2 - empréstimo
while True:
    nome = input("Digite o nome do livro que deseja emprestar (ou 'sair' para encerrar): ")
    if nome == 'sair':
        break
    if nome in biblioteca and biblioteca[nome]['quantidade'] > 0:
        biblioteca[nome]['quantidade'] -= 1
        print(f"O livro '{nome}' foi emprestado com sucesso!")
    else:
        print(f"O livro '{nome}' não está disponível no acervo.")

print('No nosso acervo temos:')
for livro, detalhes in biblioteca.items():
    autor = detalhes['autor']
    quantidade = detalhes['quantidade']
    print(f"Os livros são: '{livro}', pelo autor: {autor}, com a quantidade: {quantidade}")


# parte 3 - devolução
while True:
    nome_devolucao = input("Digite o nome do livro que deseja devolver (ou 'sair' para encerrar): ")
    if nome_devolucao == 'sair':
        break
    if nome_devolucao in biblioteca and biblioteca[nome_devolucao]['quantidade'] < biblioteca[nome_devolucao]['estoque']:
        biblioteca[nome_devolucao]['quantidade'] += 1
        print(f"O livro '{nome_devolucao}' foi devolvido com sucesso!")
    else:
        print(f"Não é possível devolver o livro '{nome_devolucao}', pois o estoque já está completo ou o livro não existe.")
