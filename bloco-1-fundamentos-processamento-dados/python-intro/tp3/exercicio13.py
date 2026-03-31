prova_a = float(input("Resultado da Prova A:\n> "))
prova_b = float(input("Resultado da Prova B:\n> "))
prova_c = int(input("Resultado da Prova C:\n> "))
prova_d = float(input("Resultado da Prova D:\n> "))

condicao_a = 15 < prova_a < 45 and prova_b <= 60
condicao_b = prova_c == 1 or (prova_c == 0 and prova_a < 20 and prova_b < 30 and prova_d == 10)
condicao_c = prova_d >= 5 or (prova_d < 5 and (prova_a == 10 or prova_a == 40) and prova_b == 0)

aprovado = condicao_a and condicao_b and condicao_c

print("APROVADO" if aprovado else "REPROVADO")
