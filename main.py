from utils import cliente,conta

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
        cliente.cadastro( )
    elif opcao == '2':
        cliente.buscar_user( )
    elif opcao == '3':
        cliente.atualizar( )
    elif opcao == '4':
        conta.excluir( )
    elif opcao == '6':
        print ('Encerrando  a sessão. . .'.upper())
        break
    else:
        print ("Opção inválida, por favor tente novamente".upper())
    print ('Sessão encerrada.'.upper())
