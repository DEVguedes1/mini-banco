import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from utils.cliente import cadastrar_usuario, buscar_usuario, atualizar_usuario, excluir_usuario
from utils.transacoes import depositar, sacar, exibir_extrato



while True:
    print("\n======= MENU PRINCIPAL =======")
    print("1 - Cadastrar Usuário")
    print("2 - Buscar Usuário")
    print("3 - Atualizar Usuário")
    print("4 - Excluir Usuário")
    print("5 - Caixa Eletrônico")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        buscar_usuario()
    elif opcao == '3':
        atualizar_usuario()
    elif opcao == '4':
        excluir_usuario()
    elif opcao == '5':
        while True:
            print("\n=== CAIXA ELETRÔNICO ===")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Extrato")
            print("0 - Voltar")
            menu = input("Escolha: ")
            if menu == '1':
                depositar()
            elif menu == '2':
                sacar()
            elif menu == '3':
                exibir_extrato()
            elif menu == '0':
                break
            else:
                print("Opção inválida.")
    elif opcao == '6':
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
