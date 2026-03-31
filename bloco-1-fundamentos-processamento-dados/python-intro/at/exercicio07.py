def calcula_limite(n_de_passos):
    """
    Calcula limite da função (x ** 2 - 1) / (x - 1) quando x tende a 1.

    :param n_de_passos: int - quantidade de passos para o cálculo do limite
    :return: list - lista com os valores convergentes
    """
    x = 0
    lista_convergente = []
    for i in range(1, n_de_passos + 1):
        x += 9 * 10 ** -i
        y = (x ** 2 - 1) / (x - 1)
        lista_convergente.append(y)
    return lista_convergente

numero_de_passos = int(input("Quantos passos você quer dar?\n> "))
print(calcula_limite(numero_de_passos))
