# Entradas de teste
cpfs_validos = [
    "123.456.789-09",
    "987.654.321-00",
    "529.982.247-25",
    "111.444.777-35",
    "456.789.123-64"
]

cpfs_invalidos = [
    "123.456.789-19",
    "987.654.321-10",
    "529.982.247-35",
    "111.444.777-45",
    "456.789.123-74"
]


# Função que calcula se CPF é válido
def validador_de_cpf(cpf):
    """
    Valida se CPF inserido é válido

    :param cpf: string - CPF no formato xxx.xxx.xxx-xx
    :return bool - retorna se CPF é válido ou não
    """
    cpf = cpf.replace(".", "").replace("-", "")  # Limpando a string
    iguais = True  # iguais começa com valor True
    primeiro_digito_verificador = 0  # soma do primeiro numero verificador
    segundo_digito_verificador = 0  # soma do segundo numero verificador
    for i in range(1, len(cpf)):  # Laço para verificar se todos os numeros são iguais
        if cpf[i] != cpf[i - 1]:
            iguais = False
            break  # se qualquer número for diferente iguais é falso e o laço para
    if not iguais:  # se não forem iguais vai pra segunda parte do cálculo
        for i in range(11, 1, -1):  # laço que passa por todos os chars de cpf menos o último - ou dois últimos
            if i == 11:
                segundo_digito_verificador += int(cpf[-i]) * i
                continue
            primeiro_digito_verificador += int(cpf[-i - 1]) * i
            segundo_digito_verificador += int(cpf[-i]) * i
    primeiro_resto_verificador = 0 if primeiro_digito_verificador * 10 % 11 == 10 else primeiro_digito_verificador * 10 % 11
    segundo_resto_verificador = 0 if segundo_digito_verificador * 10 % 11 == 10 else segundo_digito_verificador * 10 % 11
    return primeiro_resto_verificador == int(cpf[-2]) and segundo_resto_verificador == int(cpf[-1]) and not iguais


# Testes
for cpf_valido in cpfs_validos:
  print(validador_de_cpf(cpf_valido))

for cpf_invalido in cpfs_invalidos:
  print(validador_de_cpf(cpf_invalido))