macro = input("Entre com a macro:\n> ")
x = macro[0]
y = macro[1]
codigo_acao = macro[2:5]
tipo_de_acao = macro[5]
indicador_defesa = macro[6]
indicador_atraso = macro[7]

print(f"X={x},Y={y}")
print(codigo_acao)
if tipo_de_acao == "A":
    print("Ataque")
elif tipo_de_acao == "E":
    print("Especial")
else:
    print("Comum")
if indicador_defesa == "D":
    print("Defensivo")
elif indicador_defesa != "D" and indicador_atraso == "S":
    print("Com atraso")
else:
    print("Normal")
