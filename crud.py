from dados import livros

def listar_acervo():
    if not livros:
        print("Nenhum livro encontrado")
        return
    for livro in livros:
        titulo = livro["titulo"]
        if len(titulo) > 25:
            titulo = titulo[:22]+ "..."
        print("\nTitulo", livro["titulo"])
        print("Código", livro["codigo"])
        print("Título", livro["titulo"])
        print("Autor", livro["autor"])
        print("Gênero", livro["genero"])
        print(f"Preço R${livro["preco"]:.2f}")
        print("Quantidade", livro["quantidade"])


def pesquisar_livros():
    """Tem como finalidae buscar pelos titulos de livros contidos na lista"""
    pesquisa =input("Digite o titulo do livro que busca: ").strip().lower()
    while True:
        if not pesquisa:
            print("Digite um titulo para pesquisar.")
            return
        encontrados = 0
    
        for livro in livros:
            if pesquisa in livro["titulo"].lower():
                print("Livro Encontrado" ,livro['titulo'])
                encontrados +=1

        if encontrados == 0:
            print("Nenhum livro encontrado")

        continuar = input("Deseja continuar?(S ou N): ").strip().lower()
        if continuar == "n":
            break