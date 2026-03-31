nota_do_aluno = int(input("Qual a nota do aluno?\n> "))
nota_aprovacao = int(input("Qual a nota mínima de aprovação?\n> "))

if nota_do_aluno >= nota_aprovacao:
  print("APROVADO")
else:
  print("REPROVADO")