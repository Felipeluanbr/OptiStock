def mostrar_menu():

    print("----MENU PRINCIPAL----")
    print("1. Adicionar Produtos")
    print("3. Listar Produtos")
    print("4. Sair")
    print("----------------------")


def iniciar_sistema():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção:")

        if opcao == '1':
            print("Opção escolhida: Adicionar Produto")

        elif opcao == '2':
            print("Opção escolhida: Listar Produtos")

        elif opcao == '3':
            print("Opção escolhida: Sair")


iniciar_sistema()
