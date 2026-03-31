mensagem = input("Entre com a frase a ser analizada!\n> ")  # pede a frase para o usuário e a guarda na variavel mensagem
contagem_vogais = 0  # variável que será utilizada para guardar a quantidade de vogais da frase
contagem_total = len(mensagem)  # a quantidade total de caractéres da frase

for char in mensagem:  # laço de recepção para passar por cada char da frase e verificar se está presente nas vogais
  if char.lower() in "aeiou":
    contagem_vogais += 1

porcentagem_vogais = round(contagem_vogais / contagem_total * 100, 2)  # calculo da porcentagem de vogais na frase arredondada para duas casas decimais

print(f"A porcentagem de vogais é de {porcentagem_vogais}%")  # printa na tela porcentagem com mensagem