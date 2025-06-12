import conta

deposito = 0
extrato = []
numero_saque = 0
limite_de_saque = 3

def depositos():
    while True:  # loop infinito ate ter o break
            valor_deposito = float(input("Digite o valor do depósito: R$"))
            if valor_deposito > 0:  # numero inteiro positivo
                deposito +=valor_deposito
                conta.saldo_atualizado(valor_deposito)
                # registrando a operacao no extrato
                extrato.append(f'Depósito: R${valor_deposito}')
                print("Depósito concluído com sucesso!")
                break  # parar a execução
            else:
                # irá tentar até a condição ser atendida
                print("Valor inválido! Tente novamente.")
                
def sacar():
    if numero_saque < limite_de_saque:  # verifica se a tentativa é menor que 3 vezes
            while True:
                valor_saque = float(input("Digite o valor que deseja sacar: R$"))
                if valor_saque <= conta.saldo:  # se o valor digitado for menor que 500
                    print("Sacando...")
                    conta.saldo -= valor_saque  # o valor sacado é retirado do saldo atual
                    extrato.append(f'Saque: R${valor_saque}')
                    print("Valor sacado com sucesso")
                    numero_saque += 1  # conta as vezes que foi sacado
                    break
                else:
                    print("Você está sem saldo para realizar saque.")
                    break
    else:
        print("Você atingiu o limite máximo de saques disponíveis por dia")

def extratos():
    for operacao in extrato:
            print(operacao)
    saldo_final = conta.saldo + deposito
    print(f"\nSaldo final: R${saldo_final}")