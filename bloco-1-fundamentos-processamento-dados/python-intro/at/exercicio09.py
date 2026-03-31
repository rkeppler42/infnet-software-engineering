# Importando o pacote math
import math


# Função para calcular a altura da parede dado x
def altura_parede(x):
    """
    Calcula a altura da parede dado um x

    :param x: float - x da parede
    :return math.sin(x) + 2: float - retorna altura do segmento da parede
    """
    return math.sin(x) + 2


# Função para calcular a área da parede
def calcula_area(n):
    """
    Calcula área da parede

    :param n: int - número de fatias em que a parede será dividida
    :return area: float - área total da parede de acordo com o numero de fatias
    """
    area = 0
    largura = 10 / n
    x = 0
    for i in range(n):
        area += altura_parede(x) * largura
        x += largura
    return area


# Testando para o valor de 10, 100 e 1000
area_dez = calcula_area(10)
area_cem = calcula_area(100)
area_mil = calcula_area(1000)  # Vou utilizar este no cálculo final pois ele pede apenas 3 saídas

# Calculando as outras saídas
litros = area_mil / 5
latas = math.ceil(litros / 3.6)

# Saídas
print(area_mil)
print(litros)
print(latas)