gabarito_oficial  = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']
respostas_aluno_1 = ['A', 'B', 'C', 'A', 'A', 'B', 'D', 'D', 'A', 'C']
respostas_aluno_2 = ['A', 'C', 'C', 'D', 'B', 'B', 'C', 'D', 'A', 'B']  # PARA TESTE!!!


# Função que calcula número de acertos do aluno
def calcular_acertos(resposta_aluno, gabarito):
    """
    Calcula número de acertos de um aluno dado um gabarito e suas respostas

    :param resposta_aluno: list - lista com as respostas do aluno
    :param gabarito: list - lista com o gabarito do teste
    :return acertos: int - número de acertos do aluno
    """
    acertos = 0
    for i in range(len(resposta_aluno)):
        if resposta_aluno[i] == gabarito[i]:
            acertos += 1
    return acertos


# Calculando acertos
acertos_aluno_1 = calcular_acertos(respostas_aluno_1, gabarito_oficial)
acertos_aluno_2 = calcular_acertos(respostas_aluno_2, gabarito_oficial)

# Saídas
print(f"Aluno 1 acertou {acertos_aluno_1}")
print(f"Aluno 2 acertou {acertos_aluno_2}")

if acertos_aluno_1 > acertos_aluno_2:
  print("Aluno 1 venceu")
elif acertos_aluno_2 > acertos_aluno_1:
  print("Aluno 2 venceu")
else:
  print("Empate")