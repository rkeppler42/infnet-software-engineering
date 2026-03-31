caminho_inicial = input("Você segue pela 'Direita' ou 'Esquerda'?\n> ").lower()

if caminho_inicial == "esquerda":
  coragem = int(input("Qual seu nível de coragem? (De 0 a 100!)\n> "))
  if coragem < 80:
    vida = int(input("Quanto de vida você tem? (De 0 a 100!)\n> "))
    if vida >= 30:
      print("Fuga Bem-Sucedida")
    else:
      print("Derrota na Caverna")
  else:
    print("Tesouro Encontrado")
elif caminho_inicial == "direita":
  tocha = input("Você possui uma tocha? 'Sim' ou 'Nao'\n> ").lower()
  if tocha == "sim":
    tempo_restante = int(input("Quanto tempo restante de tocha você ainda tem? Em minutos!\n> "))
    if tempo_restante > 10:
      print("Caminho Seguro")
    else:
      print("Avanco Arriscado")
  elif tocha == "nao":
    print("Perdido na Escuridao")