# Entrada
posicoes = [0.0, 0.45, 0.89, 1.32, 1.74, 2.15, 2.55, 2.94, 3.32, 3.69]

# Inicialização da nossa lista de saída
metro_por_segundo = []

# Laço de repetição para calcular velocidade em m/s a cada 2 frames
for i in range(1, len(posicoes)):
  velocidade = (posicoes[i] - posicoes[i - 1]) / 0.01
  metro_por_segundo.append(velocidade)
  if velocidade < 40:  # Parando se velocidade for menor que 40m/s
    print("A bola está perdendo muita força!")
    break

# Saída
print(metro_por_segundo)