buffer = [ ]

posicoes = ["direita", "esquerda", "frente", "trás"]

def receberComando():

  if len(buffer) >= 5:
    print("Buffer cheio!")
    return

comando_recebido = input("Comando: ")

if comando_recebido in posicoes:
  buffer.append(comando_recebido)
  print("Comando adicionado!")
else: 
  print("Comando não aceito")

  receberComando()
  

