import string,random,re,conta

contas={}
usuario={}
usuarios=[]

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(padrao, senha):
        return True
    else:
        return False
        
def buscar_user(nome,cpf):
    if len(usuarios) > 0:
        for usuario in usuarios:
            saldo = usuario [usuarios['cpf']]['saldo']
            print(f"Nome: {usuarios['nome']},\nCPF: {usuarios['cpf']},\nEmail: {usuarios['email']},\nSaldo: R$ {saldo:.2f}")
    else:
        print ("Nenhum cliente cadastrado!!!!".upper())

def validar_cpf(cpf):
    cpf_valido=False
    if len(cpf)==14:
        usuario["cpf"]= cpf.replace('.','').replace('-','')
        cpf_valido=True        
        return cpf_valido

def senha_aleatoria():
    random_senha = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=8))
    usuario["senha"]=random_senha
    return random_senha
    
def cadastro( ):
    while True:
        user_name=input("\ndigite seu nome:")
        
        while True:
            user_senha=input("digite sua senha:")
            validar_senha(user_senha)
            if validar_senha(user_senha)==False:
                print("""Senha inválida. Requisitos:
- Mínimo 8 caracteres                   
- Pelo menos 1 letra maiúscula              
- Pelo menos 1 letra minúscula              
- Pelo menos 1 número     
- Pelo menos 1 caractere especial (@$!%*?&)""")
            else:
                break
            
        user_email=input("digite seu email:")
        while True:
            user_cpf=input("digite seu cpf (ex:000.000.000-00):")
            if validar_cpf(user_cpf)==True:
                cadastro(user_name,user_senha,user_email,user_cpf)
                break
        continuar = input("Deseja cadastrar outro usuário? (s/n): ")
        if continuar.lower() != 's':
            break 
    usuario = {
        "nome": user_name,
        "senha": user_senha,
        "email": user_email
    }
    usuarios.append(usuario)
    contas[user_cpf] = {"saldo": 0}

def atualizar ( ):
  cpf = input ('Digite o CPF do cliente a ser atualizado: ')
  usuario = conta.buscar(cpf)
  if usuario is not None:
    nome = input ("Digite seu nome: ")
    email = input ("Digite seu email: ")
    while True:
            senha=input("digite sua senha:")
            validar_senha(senha)
            if validar_senha(senha)==False:
                print("""Senha inválida. Requisitos:
- Mínimo 8 caracteres                   
- Pelo menos 1 letra maiúscula              
- Pelo menos 1 letra minúscula              
- Pelo menos 1 número     
- Pelo menos 1 caractere especial (@$!%*?&)""")
            else:
                break

    usuario ['nome'] = nome
    usuario ['email'] = email
    usuario ['senha'] = senha

    print (f"Dados do cliente {cpf} atualizado com sucesso!".upper())
  else:
    print ('Cliente não encontrado!'.upper())