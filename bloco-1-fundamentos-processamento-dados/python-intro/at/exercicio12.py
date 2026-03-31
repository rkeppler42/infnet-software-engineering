# Importa módulo random
import random


# Função para calcular pi a partir de n tentativas
def calcula_pi(tentativas):
    """
    Calcula pi a partir de x jogadas de dardo no alvo

    :param tentativas: int - número de tentativas que o dardo será jogado
    :return 4 * (pontos_dentro_circulo / tentativas) - float: aproximação do PI
    """
    pontos_dentro_circulo = 0
    for i in range(tentativas):

        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) <= 1:  # fórmula de pitágoras para verificar se ponto está dentro do círculo
            pontos_dentro_circulo += 1
    return 4 * (pontos_dentro_circulo / tentativas)

# Saídas
print(f"10 tentativas: {calcula_pi(10)}")
print(f"100 tentativas: {calcula_pi(100)}")
print(f"1000 tentativas: {calcula_pi(1000)}")
print(f"10000 tentativas: {calcula_pi(10000)}")
print(f"100000 tentativas: {calcula_pi(100000)}")