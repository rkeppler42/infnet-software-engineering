termos_a_higienizar = ["bobo", "chato", "idiota", "feio"]
termos_higienizados = ["****", "*****", "******", "****"]

mensagem = input().lower()

for i in range(len(termos_a_higienizar)):
    mensagem = mensagem.replace(termos_a_higienizar[i], termos_higienizados[i])
print(mensagem)