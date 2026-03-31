preco = float(input("Qual o valor do produto?\n> "))
taxa_juros = float(input("Qual a taxa de juros (no formato x.xx)?\n> "))
meses = int(input("Qual o número de meses?\n> "))
taxa_admin = float(input("Qual a taxa administrativa (no formato x.xx)?\n> "))

valor_com_juros = preco * (1 + taxa_juros * meses) * (1 + taxa_admin)
valor_por_mes = valor_com_juros / meses

print(f"Valor total: R$ {valor_com_juros:.2f}")
print(f"Valor por mes: R$ {valor_por_mes:.2f}")