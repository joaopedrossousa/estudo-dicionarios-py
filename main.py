usuarios = []


def menu_opcoes():
    print("[1] Informar Usuario ")
    print("[2] Alterar Campos Informações")
    print("[3] Informar Profissão Usuario")
    print("[4] Exibir Usuarios Cadastrados")
    print("[5] Excluir Usuario")
    print("[6] Encerrar Sistema")

    while True:

        try:
            print()
            opcao_selecionada = int(input(("Selecione uma Opção: ")))
            print()

            if opcao_selecionada in [1, 2, 3, 4, 5, 6]:

                return opcao_selecionada
            else:
                print("Opção Invalida, tente novamente! ")
                print()

        except ValueError:
            print("Opcão Invalida!")
            print()


def ler_dados():

    dados = dict()
    dados["nome"] = str(input("Informe o Nome: "))
    dados["idade"] = int(input("Informe a Idade: "))
    dados["cidade"] = str(input("Informe a Cidade: "))
    print()

    return dados


def main():

    while True:

        opcao_selecionada = menu_opcoes()

        if opcao_selecionada == 1:
            usuarios.append(ler_dados())
            print("Dados Gravados...")
            print()

        if opcao_selecionada == 4:
            print(usuarios)

        if opcao_selecionada == 6:
            print("Programa Encerrado...")
            print()
            break


if __name__ == "__main__":
    main()
