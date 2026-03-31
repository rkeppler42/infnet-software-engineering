minutos_iniciais = 345
horas = minutos_iniciais // 60
minutos = minutos_iniciais % 60

print(f"A máquina funcionou por {horas} horas e {minutos} minutos")

hora_decimal = horas + minutos / 60

print(f"O formato decimal é de {hora_decimal} horas decimal")