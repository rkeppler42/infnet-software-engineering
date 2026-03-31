mensagem = input("Qual frase você quer inverter a capitalização?\n> ")
print(f"Sua frase foi recebida. Ela é '{mensagem}'")

frase_final = mensagem.swapcase()
print(frase_final)