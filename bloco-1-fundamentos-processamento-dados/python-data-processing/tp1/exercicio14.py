entrada = input("Digite o caminho:\n> ")

if entrada[-1] == "/":
    print("NULO")
else:
    primeira_barra = entrada.find("/")
    ultima_barra = entrada.rfind("/")

    print(primeira_barra)
    print(ultima_barra)

    ultimo_trecho = entrada[ultima_barra + 1:]

    if ultimo_trecho.endswith((".exe", ".bin", ".sh")):
        print("Executavel")
    else:
        print("Arquivo comum")