# Constrói o grid original
grid = [['.' for _ in range(20)] for _ in range(20)]
grid[2][3] = 'P'   # Y=2, X=3
grid[18][15] = 'B' # Y=18, X=15
# Segue o y e x do jogador
y = 2
x = 3


# Função que faz o movimento do jogador
def movimenta_jogador(y, x, input_usuario):
  """
  Calcula nova posição de acordo com input do jogador

  :param y: int - y atual do jogador
  :param x: int - x atual do jogador
  :param input_usuario: string - input do usuário
  :return y: int - novo y do usuário de acordo com seu input
  :return x: int - novo x do usuário de acordo com seu input
  """
  if input_usuario == 'w':
    if y - 1 == -1:
      print("Colisão com a fronteira!!!")
    else:
      grid[y][x] = "."
      y -= 1
  elif input_usuario == 's':
    if y + 1 == 20:
      print("Colisão com a fronteira!!!")
    else:
      grid[y][x] = "."
      y += 1
  elif input_usuario == 'a':
    if x - 1 == -1:
      print("Colisão com a fronteira!!!")
    else:
      grid[y][x] = "."
      x -= 1
  elif input_usuario == 'd':
    if x + 1 == 20:
      print("Colisão com a fronteira!!!")
    else:
      grid[y][x] = "."
      x += 1
  else:
    print("Comando inválido!")
  return y, x


# Jogo
while grid[18][15] != "P":
  print('+' + '-' * 20 + '+')  
  for linha in grid:
    print('|' + ''.join(linha) + '|')
  print('+' + '-' * 20 + '+')
  input_usuario = input("Digite seu movimento! 'w', 'a', 's' ou 'd'").lower()
  if input_usuario.lower() == "sair":
    break
  novo_y, novo_x = movimenta_jogador(y, x, input_usuario)
  grid[y][x] = "."
  grid[novo_y][novo_x] = "P"
  y = novo_y
  x = novo_x

# Saídas
if grid[18][15] == "P":
  print('+' + '-' * 20 + '+')  
  for linha in grid:
    print('|' + ''.join(linha) + '|')
  print('+' + '-' * 20 + '+')
  print("Objetivo alcançado! Missão cumprida")
else:
  print("Que pena! Esperamos vê-lo em breve!")