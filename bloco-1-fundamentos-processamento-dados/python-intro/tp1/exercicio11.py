capacidade = 550
peso_saca = 65
numero_maximo_sacas = capacidade // peso_saca
porcentagem = ((numero_maximo_sacas * peso_saca) / capacidade) * 100

print(f"O número máximo de sacas é de: {numero_maximo_sacas}.")
print(f"A porcentagem de ocupação é de {round(porcentagem, 2)}%.")