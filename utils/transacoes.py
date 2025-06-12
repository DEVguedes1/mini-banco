from utils.cliente import contas, buscar_saldo, atualizar_saldo

LIMITE_SAQUES = 3

def depositar():
    cpf = input("CPF: ")
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        atualizar_saldo(cpf, valor)
        contas[cpf]['extrato'].append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido!")

def sacar():
    cpf = input("CPF: ")
    valor = float(input("Valor do saque: "))
    if len([op for op in contas[cpf]['extrato'] if 'Saque' in op]) >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
        return

    saldo = buscar_saldo(cpf)
    if valor > 0 and saldo >= valor:
        atualizar_saldo(cpf, -valor)
        contas[cpf]['extrato'].append(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor inválido.")

def exibir_extrato():
    cpf = input("CPF: ")
    print("\n=== EXTRATO ===")
    for operacao in contas[cpf]['extrato']:
        print(operacao)
    print(f"Saldo atual: R$ {contas[cpf]['saldo']:.2f}")