# Inicializa contadores para pesos pares e pesos ímpares
pesos_pares = 0
pesos_impares = 0

# Loop para usuário entrar com o peso ou entrar com 'SAIR' para interrompê-lo
while True:
  entrada = input("Digite o peso da carga (digite 'SAIR' para finalizar o programa):\n> ")
  if entrada == "SAIR":
    break
  entrada = int(entrada)
  if entrada % 2 == 0:
    pesos_pares += 1
  else:
    pesos_impares += 1
  

# Saídas
print(f"Pares: {pesos_pares}")
print(f"Ímpares: {pesos_impares}")