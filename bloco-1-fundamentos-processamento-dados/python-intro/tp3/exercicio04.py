peso = float(input("Qual o peso do pacote?\n> "))
if peso > 10:
  print("Excesso de peso.")
elif peso >= 9.5:
  print("Peso próximo ao limite. Verificar embalagem.")
else:
  print("Permitido.")