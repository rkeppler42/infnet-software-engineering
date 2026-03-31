# Função que retorna lista com interseção de elementos de duas listas
def intersecao(lista_1, lista_2):
    """
    Retorna a inteseção de duas listas

    :param lista_1: list - primeira lista para calcular interseção
    :param lista_2: list - segunda lista para calcular interseção
    :return lista_intersecao: list - lista com interseção de lista_1 e lista_2
    """
    lista_intersecao = []
    for elem in lista_1:
        if duplicidade(elem, lista_2):
            lista_intersecao.append(elem)
    return lista_intersecao


# Função para checar se elemento está numa lista
def duplicidade(elem, lista):
    """
    Calcula se elemento está na lista

    :param elem: int - elemento a verificar se está numa lista
    :param lista: list - lista em que será verificada presença de elem
    :return elem in lista - bool - Booleano que representa se elem está ou não na lista
    """
    return elem in lista


# Teste
print(intersecao([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8]))