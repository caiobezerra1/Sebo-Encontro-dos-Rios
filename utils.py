from dados import generos_validos, estados_validos

#Função para validar o ISBN
def validar_isbn(isbn):
    """Verifica se o ISBN fornecido é válido e possui 13 dígitos"""
    if len(isbn) != 13 or not isbn.isdigit():
        return False
    return True

#Função para verificar se o ISBN já está cadastrado
def isbn_duplicado(isbn, isbns_cadastrados):
    """Verifica se o ISBN fornecido já está cadastrado para evitar duplicidades"""
    return isbn in isbns_cadastrados

#Função para validar texto
def validar_texto(texto):
    """Verifica se o texto fornecido não esta vazio"""
    return bool(texto.strip())

#Função para validar gênero
def validar_genero(genero):
    """Verifica se o gênero fornecido é valido e não está vazio tambem"""
    return bool(genero.strip()) and genero in generos_validos

#Função para validar o estado de conservação 
def validar_conservacao(estado):
    """Verifica se o estado de conservação fornecido é valido e não esta vazio"""
    return bool(estado.strip()) and estado in estados_validos 

#Função para validar preço
def validar_preco(preco):
    """Verifica se o preço que foi fornecido é um número positivo"""
    try:
        preco_float = float(preco)
        return preco_float > 0
    except ValueError:
        return False 

#Função para validar quantidade
def validar_quantidade(quantidade):
    """Verifica se a quantidade informada é tambem um número positivo"""
    try:
        quantidade_int = int(quantidade)
        return quantidade_int >= 0
    except ValueError:
        return False