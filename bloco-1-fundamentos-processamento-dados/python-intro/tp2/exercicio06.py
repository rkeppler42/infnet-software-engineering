senha = input("Informe a senha:\n> ")

contem_simbolos = "@" in senha and "!" in senha and "#" in senha
so_minusculas = senha.islower()
so_maisculas = senha.isupper()

print(f"Contem os símbolos? {contem_simbolos}")
print(f"Contem apenas minúsculas? {so_minusculas}")
print(f"Contem apenas maiúsculas? {so_maisculas}")