import string,random,re

usuario={}
usuarios=[]

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(padrao, senha):
        return True
    else:
        return False
        
def login(nome,senha):
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"]==senha:
            True
            break

    
    
    
def senha_aleatoria():
    random_senha = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=8))
    usuario["senha"]=random_senha


def cadastro(nome,senha,email,cpf):
    usuario = {
        "nome": nome,
        "senha": senha,
        "email": email,
        "cpf": cpf
    }
    usuarios.append(usuario)
        
        