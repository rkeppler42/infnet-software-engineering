quantidade_total = int(input("Quantidade total de itens no início do dia:\n> "))
quantidade_retirada = int(input("Quantidade total de itens retirados:\n> "))
quantidade_restante = quantidade_total - quantidade_retirada

print(f"Após a retirada de {quantidade_retirada} itens, o saldo atual é de {quantidade_restante} unidades.")