tipo_sanguineo_1 = input("Qual o tipo sanguíneo da Pessoa 1?\n> ")
rh_1 = input("Qual o Rh da Pessoa 1?\n> ")
tipo_sanguineo_2 = input("Qual o tipo sanguíneo da Pessoa 2?\n> ")
rh_2 = input("Qual o Rh da Pessoa 2\n> ")
compatibilidade_tipo_sanguineo= False
compatibilidade_rh = False

if tipo_sanguineo_1 == "A" and (tipo_sanguineo_2 == "A" or tipo_sanguineo_2 == "O"):
  compatibilidade_tipo_sanguineo = True
elif tipo_sanguineo_1 == "B" and (tipo_sanguineo_2 == "B" or tipo_sanguineo_2 == "O"):
  compatibilidade_tipo_sanguineo = True
elif tipo_sanguineo_1 == "AB" and (tipo_sanguineo_2 == "A"
    or tipo_sanguineo_2 == "B"
    or tipo_sanguineo_2 == "AB"
    or tipo_sanguineo_2 == "O"):
  compatibilidade_tipo_sanguineo = True
elif tipo_sanguineo_1 == "O" and tipo_sanguineo_2 == "O":
  compatibilidade_tipo_sanguineo = True

if (rh_1 == "+" and (rh_2 == "+" or rh_2 == "-"))  or (rh_1 == "-" and rh_2 == "-"):
  compatibilidade_rh = True

if compatibilidade_tipo_sanguineo and compatibilidade_rh:
  print("Doacao compativel")
else:
  print("Doacao incompatível")