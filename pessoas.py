import sys

class Pessoa:
  lista = []
  dinheiro = 5
  def __init__(self, nome, dataNascimento):
    self.nome = nome
    self.dataNascimento = dataNascimento
    Pessoa.lista.append(self)

def info():
  opcao = -1
  while opcao < 1 or opcao > 4: 
    print("Bem-vindo ao banco, escolha uma opção:")
    print("1 - Novo Cadastro")
    print("2 - Lista de Pessoas cadastradas")
    print("3 - Pagar")
    print("4 - Sair")
    opcao = input("Digite a opção: ")
    if not opcao.isnumeric():
      opcao = -1
    else:
      opcao = int(opcao)
  return opcao

def acoes():
  op = info()
  if op == 1:
    nome = input("Insira o nome da pessoa: ")
    dataNascimento = input("Insira a data de nascimento: ")
    Pessoa(nome,dataNascimento)
  elif op == 2:
    print("Pessoas cadastradas: ")
    for pessoa in Pessoa.lista:
      print(f"Nome: {pessoa.nome} / Data de Nascimento: {pessoa.dataNascimento} / Saldo: {pessoa.dinheiro}")
  elif op == 3:
    pagante = input("Insira o nome de quem paga: ")
    recebidor = input("Insira o nome de quem recebe: ")
    valor = float(input("Insira o valor: "))
    for pessoa in Pessoa.lista:
      if pessoa.nome == pagante:
        pagante = pessoa
      elif pessoa.nome == recebidor:
        recebidor = pessoa
    if type(pagante) == str or type(recebidor) == str:
      print("Erro ao achar os participantes!")
    else:
      pagante.dinheiro -= valor
      recebidor.dinheiro += valor
      print("Pagamento enviado!")
  elif op == 4:
    sys.exit()
  acoes()

acoes()