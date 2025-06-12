from utils import cliente

while True:
    print("=================MENU==================")
    try:
        opcao=int(input("""
1- CADASTRO
2- LOGIN
3- SAIR
digite a sua opção aqui:"""))
        
        
        match opcao:
            case 1:
                
                while True:
                    user_name=input("digite seu nome:")
                    senha_escolha=input("deseja ter uma senha aleatoria(s ou n)?").lower()
                    if senha_escolha == 's':
                        user_senha=cliente.senha_aleatoria
                        print("1- ver senha")
                        print("2- nao ver senha")
                        try:
                            senha_ver=int(input("escolha uma das opções:"))
                        except:
                            print("formato invalido")
                        if senha_ver != 1 or senha_ver != 2:
                            print("invalido")
                        else:
                            print(user_senha)
                    else:
                        while True:
                            
                            user_senha=input("digite sua senha:")
                            cliente.validar_senha(user_senha)
                            if cliente.validar_senha(user_senha)==False:
                                print("""Senha inválida. Requisitos:
- Mínimo 8 caracteres              
- Pelo menos 1 letra maiúscula              
- Pelo menos 1 letra minúscula              
- Pelo menos 1 número     
- Pelo menos 1 caractere especial (@$!%*?&)""")
                            else:
                                break
                        
                    user_email=input("digite seu email:")
                    user_cpf=input("digite seu cpf (ex:000.000.000-00):")
                    cliente.cadastro(user_name,user_senha,user_email,user_cpf)
                    continuar = input("Deseja cadastrar outro usuário? (s/n): ")
                    if continuar.lower() != 's':
                        break
            case 2:
                user_name=input("digite seu nome:")
                while True:
                        user_senha=input("digite sua senha:")
                        cliente.validar_senha(user_senha)
                        if cliente.validar_senha(user_senha)==False:
                                print("""Senha inválida. Requisitos:
- Mínimo 8 caracteres              
- Pelo menos 1 letra maiúscula              
- Pelo menos 1 letra minúscula              
- Pelo menos 1 número     
- Pelo menos 1 caractere especial (@$!%*?&)""")
                        else:
                            break
                if cliente.login(user_name,user_senha):
                    break  





        if opcao==3:
            break

    except:
        print("formato invalido")
