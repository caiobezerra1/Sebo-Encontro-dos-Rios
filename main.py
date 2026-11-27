from arquivo import carregar_livros

#Carrega o acervo de livros ao iniciar o programa
carregar_livros()

#Função para exibir o menu principal do sistema
def menu_principal():
    print("\nSEBO")
    print("1 - Cadastrar livro")
    print("2 - Listar acervo")
    print("3 - Buscar livro")
    print("4 - Editar livro")
    print("5 - Registrar venda")
    print("6 - Excluir livro")
    print("7 - Relatórios")
    print("8 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()
    return opcao

while True:
    opcao = menu_principal()
    if opcao == "1":
        print("Cadastrar livro")
    elif opcao == "2":
        print("Livros cadastrados")
    elif opcao == "3":
        print("Buscar livros")
    elif opcao == "4":
        print("Editar livro")
    elif opcao == "5":
        print("Registrar venda")
    elif opcao == "6":
        print("Excluir livro")
    elif opcao == "7":
        print("Relatório")
    elif opcao == "8":
        print("Encerrar o sistema")
        break
    else:
        print("opção inválida...")