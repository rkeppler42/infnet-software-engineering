entrada = input().split()

deslocamentos = entrada[-1].count(".")
saida = []

for palavra in entrada[:-1]:
    if len(palavra) > 3:
        palavra_saida = ""

        for char in palavra:
            ascii_entrada = ord(char)
            ascii_saida = chr(ascii_entrada - deslocamentos)
            palavra_saida += ascii_saida

        saida.append(palavra_saida)
    else:
        saida.append(palavra)

saida = " ".join(saida)

print(saida)