mensagem_candidata = "Desconto exclusivo para você! Válido por tempo limitado."
prefixo_padrao = "Voz Digital: "
sufixo_padrao = " Acesse nosso site para detalhes."

mensagem_completa = f"{prefixo_padrao}{mensagem_candidata}{sufixo_padrao}"

tamanho_total = len(mensagem_completa)
diferenca_limite = 160 - tamanho_total

print(f"A mensagem tem ao todo {tamanho_total} caractéres")
print(f"Se negativo, passou do limite, se positivo, sobraram caractéres: {diferenca_limite}")