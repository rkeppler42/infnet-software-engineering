# Função que calcula horas e minutos a partir de minutos
def calcula_horas_minutos(minutos):
    """
    Converte minutos em horas.

    :param minutos: int - número de minutos à ser convertido em horas
    :return: NoneType - função apenas imprime no console a quantidade de horas
    """
    horas = minutos // 60
    minutos = minutos % 60
    print(f"{horas} {'hora' if horas == 1 else 'horas'} e {minutos} {'minuto' if minutos == 1 else 'minutos'}")

# Para teste
calcula_horas_minutos(int(input("Quantos minutos durou o percurso?\n> ")))