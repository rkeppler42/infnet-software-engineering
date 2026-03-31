identificador_transacao = input("Qual é o identificador? (ex. 'ABC123')\n> ")
data_transacao = input("Qual a data da transação? (ex. 'AAAA-MM-DD')\n> ")
hora_transacao = input("Qual a hora da transação? (ex. 'HH:MM:SS')\n> ")
tipo_transacao = input("Qual tipo da transação? ('DEB' para débito, 'CRED' para crédito)\n> ")
conta_origem = input("Qual número da conta de origem?\n> ")
conta_destino = input("Qual número da conta de destino?\n> ")
conta_destino = "N/A" if conta_destino == "" else conta_destino
valor_transacao = round(float(input("Digite o valor da transação com 2 casas decimais:\n> ")), 2)

registro_log = f"[LOG: {identificador_transacao}] - DATA: {data_transacao} {hora_transacao} | TIPO: {tipo_transacao} {{ORIGEM: {conta_origem} -> DESTINO: {conta_destino}}} R${valor_transacao:.2f};"
print(registro_log)