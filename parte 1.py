#Adicionar livros ao acervo
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
