import cliente

def saldo():
    cliente.usuario["saldo"]=0.00

def saldo_atualizado(deposito):
    cliente.usuario["saldo"]=cliente.usuario["saldo"]+deposito