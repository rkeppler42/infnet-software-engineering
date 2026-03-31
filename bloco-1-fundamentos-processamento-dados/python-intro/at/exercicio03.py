# Entrada
lista_de_numeros = input("Digite uma lista de números. Cada número deve ser separado por um espaço. Exemplo '1 2 3 4 5").split()

# Calcular soma passando por cada elemento da lista
soma = 0
for num in lista_de_numeros:
  soma += float(num)

# Saídas
print(soma)
print(soma / len(lista_de_numeros))