entrada = input().split(";")
saida = ""
for i in range(len(entrada)):
    entrada[i] = entrada[i].strip()
    saida += entrada[i]
    if i != len(entrada) - 1:
        saida += "/"
print(saida)