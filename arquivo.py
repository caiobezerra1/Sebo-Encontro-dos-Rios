#Importando as bibliotecas necessárias, como json, Path e os dados do arquivo dados.py
import json 
from pathlib import Path
from dados import generos_validos, estados_validos, livros, isbns_cadastrados

#Caminho do arquivo acervo.json que contém os livros cadastrados
caminho_arquivo = Path(__file__).parent / "dados" / "acervo.json"

#Função para carregar os livros do arquivo json
def carregar_livros():
    try:
#Abrir o arquivo acervo.json e carregar os registros de livros
        with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
            registros = json.load(arquivo)

        if not isinstance(registros, list):
            print("Erro: O arquivo acervo.json não contém uma lista de livros.")
            return
#Except para tratar erros de arquivo não encontrado
    except FileNotFoundError:
        print("Erro: O arquivo acervo.json não foi encontrado.")
        return
#Except para tratar erros do JSON
    except json.JSONDecodeError:
        print("Erro: O arquivo acervo.json não contém um JSON válido.")
        return

#Atualiza a lista de livros e o conjunto de ISBNs
    livros.clear()
    livros.extend(registros)
    isbns_cadastrados.clear()

#Adicionar os ISBNs dos livros já carregados do arquivo json ao conjunto isbns_cadastrados
    for livro in livros:
        if "isbn" in livro:
            isbns_cadastrados.add(livro["isbn"])

    print(f"{len(livros)} livros carregados com sucesso!")