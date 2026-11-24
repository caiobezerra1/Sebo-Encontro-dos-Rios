from arquivo import carregar_livros, salvar_livros
from dados import livros

carregar_livros()
print(f"Total de livros carregados: {len(livros)}")
salvar_livros()