# prefixo = "ELT"
# numero_serie = "12345"

prefixo = input("Qual o prefixo?\n> ")
numero_serie = input("Qual o número de série?\n> ")


codigo_sku = f"{prefixo}{numero_serie}"

print(codigo_sku)