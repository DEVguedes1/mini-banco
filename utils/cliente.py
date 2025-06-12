import string,random,re

usuario={}
usuarios=[]

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(padrao, senha):
        return True
    else:
        return False
        
def buscar_user(nome,cpf):
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["cpf"]==cpf:
            for i, u in enumerate(usuarios, start=1):
                return print(f"{i}. Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")
            

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
        senha_escolha=input("deseja ter uma senha aleatoria(s ou n)?").lower()
        if senha_escolha == 's':
            user_senha=senha_aleatoria
            print("1- ver senha")
            print("2- nao ver senha")
            try:
                senha_ver=int(input("escolha uma das opções:"))
            except:
                print("formato invalido")
            if senha_ver == 1:
                print(senha_aleatoria)
        else:
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
        
        