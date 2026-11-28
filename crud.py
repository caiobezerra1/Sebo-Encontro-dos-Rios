from utils import (
    validar_isbn,
    isbn_duplicado,
    validar_texto,
    validar_genero,
    validar_conservacao,
    validar_preco,
    validar_quantidade
)
from dados import livros, isbns_cadastrados
from arquivo import salvar_livros

def listar_acervo():
    """Exibe todos os livros cadastrados em formato de tabela"""

    if not livros:
        print("Nenhum livro encontrado.")
        return

    print("\n" + "=" * 100)
    print("ACERVO DE LIVROS")
    print("=" * 100)

    print(
        f"{'Código':<8}"
        f"{'Título':<27}"
        f"{'Autor':<25}"
        f"{'Gênero':<15}"
        f"{'Preço (R$)':>12}"
        f"{'Qtd.':>8}"
    )
    print("-" * 100)

    for livro in livros:
        titulo = livro["titulo"]
        if len(titulo) > 25:
            titulo = titulo[:22] + "..."

        print(
            f"{livro['codigo']:<8}"
            f"{titulo:<27}"
            f"{livro['autor']:<25}"
            f"{livro['genero']:<15}"
            f"{livro['preco']:>12.2f}"
            f"{livro['quantidade']:>8}"
        )
    print("=" * 100)

def exibir_dados_livro(livro):
    """Mostra todos os dados de um livro qualquer"""

    print("\n------------------------------")
    print("LIVRO ENCONTRADO")
    print("------------------------------")
    print("Código:", livro["codigo"])
    print("Título:", livro["titulo"])
    print("Autor:", livro["autor"])
    print("ISBN:", livro["isbn"])
    print("Gênero:", livro["genero"])
    print("Conservação:", livro["conservacao"])
    print(f"Preço: R$ {livro['preco']:.2f}")
    print("Quantidade:", livro["quantidade"])

def pesquisar_livros():
    """Tem como finalidae buscar pelos titulos de livros contidos na lista"""
    while True:
        pesquisa =input("Digite o titulo do livro que busca: ").strip().lower()
        if not pesquisa:
            print("Digite um titulo para pesquisar.")
            continue
        encontrados = False
    
        for livro in livros:
            if pesquisa in livro["titulo"].lower():
                exibir_dados_livro(livro)
                encontrados = True

        if not encontrados:
            print("Nenhum livro encontrado")

        continuar = input("Deseja continuar?(S ou N): ").strip().lower()
        if continuar == "n":
            break

def buscar_codigo():
    """Funciona como outro método de pesquisa além da por titulo"""
    while True:
        codigo = input("Digite o código do livro: ").strip()
        
        encontrado = False

        for livro in livros:
            if str(livro["codigo"]) == codigo:
                exibir_dados_livro(livro)
                encontrado = True

        if not encontrado:
            print("Nenhum livro encontrado")
            
        continuar = input("Deseja continuar?(S ou N): ").strip().lower()
        if continuar == "n":
            break

def cadastrar_livros():
    """cadastrar novos livros no acervo"""
    titulo = input("Digite o titulo do livro: ").strip().title()
    autor = input("Digite o nome do autor: ").strip().title()
    isbn = input("Digite o ISBN: ").strip()
    genero = input("Digite o gênero: ").strip().title()
    conservacao = input("Qual o estado de conservação: ").strip().title()

    if not validar_isbn(isbn):
        print("ISBN inválido")
        return
    if isbn_duplicado(isbn, isbns_cadastrados):
        print("Este ISBN já está cadastrado.")
        return
    if not validar_texto(titulo) or not validar_texto(autor):
        print("Titulo e autor são obrigatórios.")
        return
    if not validar_genero(genero):
        print("Gênero inválido.")
        return
    if not validar_conservacao(conservacao):
        print("Inválido.")
        return
    try:
        preco = float(input("Digite o preço do livro: R$ "))
        quantidade = int(input("Digite a quantidade de livros: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if not validar_preco(preco):
        print("O preço deve ser maior que zero...")
        return
    if not validar_quantidade(quantidade):
        print("Quantidade inválida")
        return

    novo_livro = {
        "codigo": gerar_codigo(),
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero,
        "conservacao": conservacao,
        "preco": preco,
        "quantidade": quantidade
    }
    livros.append(novo_livro)
    isbns_cadastrados.add(isbn)
    salvar_livros()
    print("Livro cadastrado com sucesso!")

def gerar_codigo():
    """Gera um código único para cada livro cadastrado, para garantir que não tenha dois codigos iguais"""
    maior_codigo = max((livro["codigo"] for livro in livros), default=0)
    return maior_codigo + 1

def registrar_venda():
    """Tem como objetivo registrar a venda de livros e atualizar o estoque"""
    print("\n---VENDA DE LIVROS---")
    print("1. Buscar livro pelo título")
    print("2. Buscar livro pelo código")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        pesquisar_livros()
    
    elif opcao == "2":
        buscar_codigo()
    
    else:
        print("Opção inválida")
        return
    codigo = input("Digite o código do livro que deseja comprar: ").strip()
    livro_encontrado = None
    for livro in livros:
        if str(livro["codigo"])== codigo:
            livro_encontrado = livro 
            break
    if livro_encontrado is None:
        print("Livro não encontrado...")
        return
    try:
        quantidade_de_venda = int(input("Digite a quantidade desejada: "))
    except ValueError:
        print("Digite uma quantidade válida.")
        return
    if quantidade_de_venda <= 0:
        print("Quantidade inválida")
        return
    if quantidade_de_venda > livro_encontrado["quantidade"]:
        print("Estoque insuficiente.")
        return
    preco = livro_encontrado["preco"]

    if livro_encontrado["conservacao"] == "Regular":
        preco = preco * 0.80

    total = preco * quantidade_de_venda

    livro_encontrado["quantidade"] -= quantidade_de_venda

    salvar_livros()

    print("Venda registrada!")
    print(f"Valor total da venda: R$ {total:.2f}")
    print(f"Estoque de livros retantes: {livro_encontrado['quantidade']}")

def editar_livro():
    """Permitir editar as informações de um livro cadastrado."""
    print("\n---EDITAR LIVRO---")
    print("1. Buscar livro pelo título")
    print("2, Buscar livro pelo código")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        pesquisar_livros()

    elif opcao == "2":
        buscar_codigo()

    else:
        print("Opção inválida.")
        return
    
    codigo = input("Digite o código do livro que deseja editar: ").strip()

    livro_encontrado = None

    for livro in livros:
        if str(livro["codigo"]) == codigo:
            livro_encontrado = livro
            break
    if livro_encontrado is None:
          print("Nenhum livro")
          return

    exibir_dados_livro(livro_encontrado)
    print("\nPressione Enter para manter o valor atual.")

    titulo = input("Novo título: ").strip().title()
    autor = input("Novo autor: ").strip().title()
    isbn = input("Novo ISBN: ").strip()
    genero = input("Novo gênero: ").strip().title()
    conservacao = input("Novo estado de conservação: ").strip().title()
    preco = input("Novo preço: ").strip()
    quantidade = input("Nova quantidade livros: ").strip()

    if not titulo:
        titulo = livro_encontrado["titulo"]

    if not autor:
        autor = livro_encontrado["autor"]

    if not isbn:
        isbn = livro_encontrado["isbn"]

    if not genero:
        genero = livro_encontrado["genero"]

    if not conservacao:
        conservacao = livro_encontrado["conservacao"]

    if not preco:
        preco = livro_encontrado["preco"]

    if not quantidade:
        quantidade = livro_encontrado["quantidade"]

    if not validar_texto(titulo) or not validar_texto(autor):
        print("Titulo ou autor inválido.")
        return

    if not validar_isbn(isbn):
        print("ISBN inválido.")
        return

    if isbn != livro_encontrado["isbn"] and isbn_duplicado(isbn, isbns_cadastrados):
        print("Este ISBN já está cadastrado.")
        return

    if not validar_conservacao(conservacao):
        print("Tipo inválido.")
        return

    if not validar_genero(genero):
        print("Gênero inválido.")
        return

    if not validar_quantidade(quantidade):
        print("Quantidade inválida")
        return

    if not validar_preco(preco):
        print("Preço inválido.")
        return
    preco = float(preco)
    quantidade = int(quantidade)

    if isbn != livro_encontrado["isbn"]:
        isbns_cadastrados.discard(livro_encontrado["isbn"])
        isbns_cadastrados.add(isbn)

    livro_encontrado["titulo"] = titulo
    livro_encontrado["autor"] = autor
    livro_encontrado["isbn"] = isbn
    livro_encontrado["genero"] = genero
    livro_encontrado["conservacao"] = conservacao
    livro_encontrado["preco"] = preco
    livro_encontrado["quantidade"] = quantidade
    salvar_livros()

    print("Livro atualizado!")