#Importando as bibliotecas necessárias, como json, Path e os dados do arquivo dados.py
import json 
from pathlib import Path
from dados import livros, isbns_cadastrados

#Caminho do arquivo acervo.json que contém os livros cadastrados
caminho_arquivo = Path(__file__).parent / "dados" / "acervo.json"

#Função para carregar os livros do arquivo json
def carregar_livros():
    """Carrega os livros do arquivo acervo.json e 
    atualiza a lista de livros e o conjunto de ISBNs cadastrados."""

#Limpa os dados anteriores para evitar as duplicações
    livros.clear()
    isbns_cadastrados.clear()

    try:
#Abrir o arquivo acervo.json e carregar os registros de livros
        with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
            registros = json.load(arquivo)

        if not isinstance(registros, list):
            print("Erro: O arquivo acervo.json não contém uma lista de livros")
            return

#Except para tratar erros de arquivo não encontrado
    except FileNotFoundError:
        print("Erro: O arquivo não encontrado, iniciando com um acervo vazio.")
        return

#Except para tratar erros do JSON
    except json.JSONDecodeError:
        print("Erro: O arquivo acervo.json não contém um JSON válido.")
        return

#Atualiza a lista principal dos livros
    livros.extend(registros)

#Atualiza o conjunto de ISBNs
    for livro in livros:
        if "isbn" in livro:
            isbns_cadastrados.add(livro["isbn"])
    print(f"{len(livros)} livros carregados com sucesso!")

#Função para salvar os livros
def salvar_livros():
    """Salva os livros no arquivo acervo.json"""
    try:
        caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(livros, arquivo, ensure_ascii=False, indent=4)
        print("Acervo salvo com sucesso!")
    except (OSError, TypeError) as e:
        print(f"Erro ao salvar o acervo: {e}")