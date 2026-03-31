total_bruto_compra = float(input("Qual o valor da compra?\n> "))
input_usuario = input("Cliente tem Cartão TecnoMais? 'S' ou 'N'\n> ").lower()
cartao_technomais = True if input_usuario == "s" else False
desconto = 1

if total_bruto_compra > 1000:
  desconto -= 0.15
elif total_bruto_compra > 500:
  desconto -= 0.1
elif total_bruto_compra > 100:
  desconto -= 0.05

if cartao_technomais and total_bruto_compra > 100:
  desconto -= 0.02

print(f"Preço final: R$ {total_bruto_compra * desconto:.2f}")