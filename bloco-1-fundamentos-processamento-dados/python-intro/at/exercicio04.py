def calcular_fatorial(numero):
    """
    Calcula e exibe o fatorial de um número.

    :param numero: int - número a ser fatorado
    :return: NoneType
    """
    fatorial = 1
    if numero == 0:
        print(fatorial)
    else:
        for i in range(numero, 0, -1):
            fatorial *= i
        print(fatorial)
