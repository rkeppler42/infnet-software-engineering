nome_arquivo = input("Qual nome do arquivo, incluindo sua extensão?\n> ")
prefixo_obrigatorio = input("Qual o prefixo obrigatório?\n> ")

prefixo_valido = nome_arquivo.startswith(prefixo_obrigatorio)
extensao_valida = nome_arquivo.endswith((".py", ".txt"))

if prefixo_valido and extensao_valida:
    print("VÁLIDO")
else:
    print("INVÁLIDO")
    
    if not prefixo_valido:
        print("O arquivo não começa com o prefixo obrigatório.")
    
    if not extensao_valida:
        print("O arquivo não termina com .py ou .txt.")