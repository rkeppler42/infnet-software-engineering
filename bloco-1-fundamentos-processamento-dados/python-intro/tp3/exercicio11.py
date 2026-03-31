import string

senha = input("Entre com sua senha:\n> ")
contagem_numeros = 0
tem_um_numero = False
tem_caracter_especial = False



for char in senha:
  if char in "!@#":  # se tem pelo menos um dos caractéres especiais
    tem_caracter_especial = True
  elif char in string.digits:
    contagem_numeros += 1  

tem_um_numero = contagem_numeros == 1  # se tem 1 e apenas - segundo enunciado - 1 número

caracteres_minimos = len(senha) >= 8  # se tem pelo menos 8 caractéres

seguranca = [tem_caracter_especial, tem_um_numero, caracteres_minimos]

if seguranca.count(True) >= 2:
  print("Segura")
else:
  print("Fraca")