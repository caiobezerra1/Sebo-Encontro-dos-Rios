#Gêneros que são aceitos pelo sistema
generos_validos = (
    "Romance",
    "Ficção",
    "Cordel",
    "Poesia",
    "Didático",
    "Infantil",
    "Biografia",
    "Outros"
)

#Estados de conservação aceitos pelo sistema
estados_validos = (
    "Ótimo",
    "Bom",
    "Regular",
)

#Lista que armazena os livros carregados do arquivo acervo.json
livros = []

#Conjunto que armazena os ISBNs dos livros cadastrados
isbns_cadastrados = set()

