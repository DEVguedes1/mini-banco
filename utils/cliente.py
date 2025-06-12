import re

usuarios = []
contas = {}

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(padrao, senha))

def validar_cpf(cpf):
    return len(cpf) == 14

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF (000.000.000-00): ")

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    senha = input("Senha: ")
    if not validar_senha(senha):
        print("Senha inválida!")
        return

    usuario = {"nome": nome, "email": email, "cpf": cpf, "senha": senha}
    usuarios.append(usuario)
    contas[cpf] = {"saldo": 0.0, "extrato": []}
    print("Usuário cadastrado com sucesso!")

def buscar_usuario():
    cpf = input("Digite o CPF para buscar: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            saldo = contas[cpf]['saldo']
            print(f"Nome: {usuario['nome']}\nEmail: {usuario['email']}\nCPF: {cpf}\nSaldo: R$ {saldo:.2f}")
            return
    print("Usuário não encontrado.")

def atualizar_usuario():
    cpf = input("CPF do cliente: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['nome'] = input("Novo nome: ")
            usuario['email'] = input("Novo email: ")
            senha = input("Nova senha: ")
            if validar_senha(senha):
                usuario['senha'] = senha
                print("Usuário atualizado com sucesso!")
            else:
                print("Senha inválida.")
            return
    print("Usuário não encontrado.")

def excluir_usuario():
    cpf = input("Digite o CPF: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            contas.pop(cpf, None)
            print("Usuário excluído com sucesso.")
            return
    print("Usuário não encontrado.")

def buscar_saldo(cpf):
    return contas.get(cpf, {}).get('saldo', 0.0)

def atualizar_saldo(cpf, valor):
    if cpf in contas:
        contas[cpf]['saldo'] += valor