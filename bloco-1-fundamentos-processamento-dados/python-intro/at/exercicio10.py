# Importando pacote math
import math


# Entradas
principal = float(input("Entre com o valor do capital principal inicial:\n> "))
taxa_juros = float(input("Entre com a taxa de juros em formato decimal:\n> "))
tempo = int(input("Entre com a quantidade de meses do investimento:\n> "))


# Função para calcular montante final com tempo menor que 3 meses
def calcula_penalidade(principal):
    """
    Calcula montante final quando tempo de investimento menor do que 3 meses

    :param principal: float - o montante principal do investimento
    :return m: float - o montante final do investimento após aplicação da penalidade
    """
    m = math.trunc(principal * 0.98 * 100) / 100  # O enunciado pediu para truncar com duas casas decimais ao invés de arredondar
    return m


# Calculo do principal a partir do bonus de 0.5%
def calcula_bonus(c):
    """
    Calcula principal com bonus se investimento maior ou igual a 18 meses

    :param c: float - montante inicial do investimento
    :return c * 1.005 - float - calculo do principal com bônus
    """
    return c * 1.005


# Função para montante final com 3 meses ou mais de investimento:
def calcula_montante(c, i, t):
    """
    Calcula montante final do investimento com tempo de 3 ou mais meses

    :param c: float - capital inicial
    :param i: float - taxa de juros em decimal
    :param t: int - tempo de investimento
    :return m: float - montante final do investimento
    """
    m = math.trunc((c * (1 + i) ** t) * 100) / 100
    return m


# Calcula e printa montante final de acordo com tempo em meses
if tempo < 3:
  montante_final = calcula_penalidade(principal)
else:
  if tempo >= 18:
    principal = calcula_bonus(principal)
  montante_final = calcula_montante(principal, taxa_juros, tempo)

# Saída
print(montante_final)