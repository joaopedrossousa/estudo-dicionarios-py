usuarios = []


def indices_menu():
    print("[1] Informar Usuario ")
    print("[2] Alterar Campos Informações")
    print("[3] Informar Profissão Usuario")
    print("[4] Exibir Usuarios Cadastrados")
    print("[5] Excluir Usuario")
    print("[6] Encerrar Sistema")


def menu_opcoes():

    indices_menu()

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


def receber_dados():

    dados = dict()
    dados["nome"] = str(input("Informe o Nome: "))
    dados["idade"] = int(input("Informe a Idade: "))
    dados["cidade"] = str(input("Informe a Cidade: "))
    print()

    return dados


def mostrar_dados():
    for i, usuario in enumerate(usuarios):
        print(f"Usuario [{i + 1}]")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Cidade: {usuario['cidade']}")
        print()


def alterar_dados():

    mostrar_dados()

    usuario_selecionado = int(
        input("Informe o Usuário que deseja alterar (número da lista): ")
    )
    idx = usuario_selecionado - 1

    if idx < 0 or idx >= len(usuarios):
        print("Usuário inválido.")
    else:
        usuario = usuarios[idx]
        print(f"\nUsuário selecionado: {usuario.get('nome', '(sem nome)')}\n")

        print("[1] Nome\n[2] Idade\n[3] Cidade\n[4] Profissão\n")
        campo_selecionado = int(input("Informe qual dado você deseja alterar: "))

        mapa = {
            1: ("nome", "Informe o novo nome: "),
            2: ("idade", "Informe a nova idade: "),
            3: ("cidade", "Informe a nova cidade: "),
            4: ("profissao", "Informe a nova profissão: "),
        }

        if campo_selecionado in mapa:
            chave, pergunta = mapa[campo_selecionado]
            novo_valor = input(pergunta)
            usuario[chave] = novo_valor
            print(f"\n{chave.capitalize()} atualizado com sucesso!\n")
        else:
            print("\nOpção inválida.\n")


def main():

    while True:

        opcao_selecionada = menu_opcoes()

        if opcao_selecionada == 1:
            usuarios.append(receber_dados())
            print("Dados Gravados...")
            print()

        if opcao_selecionada == 2:
            alterar_dados()

        if opcao_selecionada == 4:
            mostrar_dados()

        if opcao_selecionada == 6:
            print("Programa Encerrado...")
            print()
            break


if __name__ == "__main__":
    main()
