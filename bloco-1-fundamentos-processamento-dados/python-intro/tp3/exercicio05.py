descricao_despesa = input("Qual a descricao da despesa?\n> ").lower()
valor_despesa = float(input("Qual o valor da despesa?\n> "))

if ("aluguel" in descricao_despesa
    or "moradia" in descricao_despesa
    or "supermercado" in descricao_despesa
    or "alimentacao" in descricao_despesa
    or "agua" in descricao_despesa
    or "luz" in descricao_despesa
    or "internet" in descricao_despesa):
  print(f"Essencial - R$ {valor_despesa:.2f}")
elif ("acoes" in descricao_despesa
      or "fundos" in descricao_despesa
      or "previdencia" in descricao_despesa
      or "bolsa" in descricao_despesa):
  print(f"Investimento - R$ {valor_despesa:.2f}")
else:
  print(f"Lazer e Outros - R$ {valor_despesa:.2f}")