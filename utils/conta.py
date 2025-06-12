import cliente

def buscar(cpf): 
  for usario in cliente.usuarios:
    if cliente ['cpf'] == cpf:
      return cliente
  return None

def saldo():
    cliente.usuario["saldo"]=0.00

def saldo_atualizado(deposito):
    cliente.usuario["saldo"]=cliente.usuario["saldo"]+deposito

def excluir():
    cpf = input("Cliente digite o seu CPF para prosseguir com a exclusão: ")
    user=buscar(cpf)
    if user is not None:
        cliente.usuarios.remove(cliente.usuario)
        cliente.contas.pop(cpf)
        print ("Cliente excluído com sucesso!.".upper())
    else:
        print ("Cliente não encontrado no banco de Dados!".upper())