dna = input("Entre com a sequência de DNA:\n> ")
alvo = input("Entre com o códon alvo:\n> ")

achou = -1

for indice in range(len(dna)):
    if dna.find(alvo, indice, indice + len(alvo)) != -1:
        achou = indice
        break

print(achou)