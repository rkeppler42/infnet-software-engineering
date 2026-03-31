inimigos_derrotados = int(input("Quantos inimigos foram derrotados?\n> "))
objetivos_conquistados = int(input("Quantos objetivos foram conquistados?\n> "))
mortes_sofridas = int(input("Quantas mortes foram sofridas?\n> "))
tempo_de_partida = int(input("Quanto tempo em minutos foram jogados?\n> "))

pontuacao_final = 0

if inimigos_derrotados < 10:
  pontuacao_final += 10
elif 10 <= inimigos_derrotados <= 29:
  pontuacao_final += 30
elif inimigos_derrotados >= 30:
  pontuacao_final += 50

if objetivos_conquistados >= 3:
  pontuacao_final += 60
elif objetivos_conquistados >= 1:
  pontuacao_final += 25

if mortes_sofridas > 10:
  pontuacao_final -= 30
elif mortes_sofridas >= 5:
  pontuacao_final -= 10

if tempo_de_partida >= 15:
  pontuacao_final += 5
elif tempo_de_partida >= 5:
  pontuacao_final += 15
elif tempo_de_partida >= 0:
  pontuacao_final += 25

print(f"Sua pontuação final foi de {pontuacao_final}")

if pontuacao_final > 100:
  print("Você é um Jogador Elite!")