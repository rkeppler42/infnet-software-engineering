minutos_totais = 1527
horas_trabalhadas = minutos_totais // 60
minutos_excedentes = minutos_totais % 60
valor_horas = horas_trabalhadas * 60
valor_minutos = minutos_excedentes * 1.2
valor_total = valor_horas + valor_minutos

print(f"Horas trabalhadas: {horas_trabalhadas}")
print(f"Minutos excedentes: {minutos_excedentes}")
print(f"Valor pago pelas horas: R$ {valor_horas:.2f}")
print(f"Valor pago pelos minutos excedentes: R$ {valor_minutos:.2f}")
print(f"Valor total pago: R$ {valor_total:.2f}")
