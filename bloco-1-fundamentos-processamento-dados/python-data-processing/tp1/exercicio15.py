entrada = input().strip()

pontuacoes = ".,;:!?"

entrada = entrada.strip(pontuacoes).strip()
entrada = entrada.strip("^~").strip()
if len(entrada) > 0:
    entrada = entrada.strip("[]").strip()

print(entrada)