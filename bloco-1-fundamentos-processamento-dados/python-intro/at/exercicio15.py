# Entrada
meta = int(input("Qual o valor da meta?\n> "))

# Inicialização do somatório
doacao_total = 0
while True:
  doacao_individual = float(input("Qual o valor da doação?\n> "))
  doacao_total += doacao_individual
  if doacao_total >= meta:  # Se somatório maior ou igual à entrada sair do loop
    break

# Saída
print(f"{doacao_total:.2f}", end="")  # O enunciado pediu para imprimir tudo numa única linha - por isso end=""
if doacao_total == meta:
  print(" | Meta atingida!!!")
elif doacao_total > meta:
  print(f" | Meta superada!!! Passamos o valor em {doacao_total - meta:.2f}")