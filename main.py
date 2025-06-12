from utils import cliente

while True:
    print("=================MENU==================")
    
    opcao=input("""
1- CADASTRO DE USUARIO
2- BUSCAR USUARIO
3- ATUALIZAR USUARIO
4- EXCLUIR USUARIO
5- SAIR 
digite a sua opção aqui:""")
    
    if opcao == '1':
        cliente.cadastro ( )
    elif opcao == '2':
        cliente.buscar_user( )
    elif opcao == '3':
        # atualizar ( )
        cliente
    elif opcao == '4':
        # excluir ( )
        cliente
    elif opcao == '5':
        print ('Encerrando  a sessão. . .'.upper())
        break
    else:
        print ("Opção inválida, por favor tente novamente".upper())
    print ('Sessão encerrada.'.upper())
        
        # match opcao:
            
        #     case 2:
                # user_name=input("digite seu nome:")
                # user_cpf=input("digite seu cpf (ex:000.000.000-00):")
                # for cliente.usuario in cliente.usarios:
                #     if cliente.usuario["cpf"]==user_cpf:
                #         print(cliente.buscar_user(user_name,user_cpf))

        # if opcao==3:
        #     break
    