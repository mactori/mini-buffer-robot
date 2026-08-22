buffer = [ ]

posicoes = ["direita", "esquerda", "frente", "trás"]

def executarComando():
    for comando in buffer:
      print("Executando:", comando)

def receberComando():

  if len(buffer) >= 5:
    print("Buffer cheio!")
    executarComando()
    return

  comando_recebido = input("Comando: ")

  if comando_recebido in posicoes:
    buffer.append(comando_recebido)
    print("Comando adicionado!")
  else: 
    print("Comando não aceito")

  receberComando()

receberComando()
  

