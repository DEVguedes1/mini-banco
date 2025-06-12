from utils import cliente,conta,transacoes

while True:
    print("=================MENU==================")
    
    opcao=input("""
1- CADASTRO DE USUARIO
2- BUSCAR USUARIO
3- ATUALIZAR USUARIO
4- EXCLUIR USUARIO
5- CAIXA ELETRONICO
6- SAIR 
digite a sua opção aqui:""")
    
    if opcao == '1':
        cliente.cadastro
    elif opcao == '2':
        cliente.buscar_user
    elif opcao == '3':
        cliente.atualizar
    elif opcao == '4':
        conta.excluir
    elif opcao == '5':
        while True:  
            menu = input("""\n\nCAIXA ELETRÔNICO
1- Depositar
2- Sacar
3- Extrato
0- Sair

Selecione a opção que deseja realizar: """)
            if menu == '1':
                transacoes.depositos
            elif menu == '2':
                transacoes.sacar
            elif menu == '3':
                transacoes.extratos
            elif menu == '0':
                break
            else:
                print("Número selecionado inválido. Tente novamente")   
    elif opcao == '6':
        print('Encerrando  a sessão. . .'.upper())
        break
    else:
        print("Opção inválida, por favor tente novamente".upper())
    print('Sessão encerrada.'.upper())
