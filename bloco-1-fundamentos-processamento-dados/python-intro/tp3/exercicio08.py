anos_de_experiencia = int(input("Quantos anos de experiência o candidato possui?\n> "))
nivel_de_escolaridade = input("Qual o grau de escolaridade do candidato?\n> ").lower()
conhecimento_em_python = input("Qual o nível de Python do candidato?\n> ").lower()

if (anos_de_experiencia >= 8
    or ((nivel_de_escolaridade == "pós-graduação" or nivel_de_escolaridade == "mestrado") and conhecimento_em_python == "avançado")
    or ("infnet" in nivel_de_escolaridade or "infnet" in conhecimento_em_python)):
    print("Candidato Elegível")
else:
    print("Candidato Não Elegível")