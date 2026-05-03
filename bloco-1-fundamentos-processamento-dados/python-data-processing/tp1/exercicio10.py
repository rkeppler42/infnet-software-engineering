vendas_brutas = float(input("Qual o valor das vendas brutas?\n> "))
custo_produtos_vendidos = float(input("Qual o custo total dos produtos vendidos?\n> "))
despesas_operacionais = float(input("Qual o valor das despesas operacionais diversas?\n> "))

receita_total = vendas_brutas - custo_produtos_vendidos
total_despesas = despesas_operacionais
saldo_final = receita_total - total_despesas

positivo_ou_negativo = ""

if saldo_final > 0:
    status = " Positivo"
elif saldo_final < 0:
    status = " Negativo"
else:
    status = ""

saida = f"""Demonstrativo de Fechamento de Caixa
{"Receita Total":<20}{receita_total:>15.2f}
{"Total de Despesas":<20}{total_despesas:>15.2f}
{"Saldo Final":<20}{saldo_final:>15.2f}{status}"""

print(saida)