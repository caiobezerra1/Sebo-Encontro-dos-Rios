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
    if not livros:
        print("Nenhum livro encontrado")
        return
    for livro in livros:
        titulo = livro["titulo"]
        if len(titulo) > 25:
            titulo = titulo[:22]+ "..."
        print("\nTitulo", titulo)
        print("Código", livro["codigo"])
        print("Autor", livro["autor"])
        print("Gênero", livro["genero"])
        print(f"Preço R${livro["preco"]:.2f}")
        print("Quantidade", livro["quantidade"])


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
                print("Livro Encontrado" ,livro['titulo'])
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
                print("Livro Encontrado: ", livro["titulo"])
                encontrado = True
                break

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

