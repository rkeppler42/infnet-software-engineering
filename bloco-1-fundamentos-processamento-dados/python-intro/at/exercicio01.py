# Entradas
componente_a = float(input("Qual o valor unitário do componente A?\n> "))
qtd_componente_a = int(input("Quantos componente A estarão no produto final?\n> "))
componente_b = float(input("Qual o valor unitário do componente B?\n> "))
qtd_componente_b = int(input("Quantos componente B estarão no produto final?\n> "))
custo_fixo_total = float(input("Qual valor do custo fixo para a produção do lote do produto?\n> "))
qtd_produtos_lote = int(input("Quantos produtos foram produzidos neste lote?\n> "))

# Saídas
custo_total_lote = round((componente_a * qtd_componente_a + componente_b * qtd_componente_b) * qtd_produtos_lote + custo_fixo_total, 2)
custo_unitario = round(custo_total_lote / qtd_produtos_lote, 2)

print(f"{custo_total_lote:.2f}")
print(f"{custo_unitario:.2f}")