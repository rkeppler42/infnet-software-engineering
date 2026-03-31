tipo_pessoa = input("Qual o tipo de pessoa? (PF ou PJ)").lower()

if tipo_pessoa == "pf":
  cpf = input("Informe o CPF (apenas números):")
  idade = int(input("Qual sua idade?"))
  if len(cpf) != 11:
    documentacao_complementar = input("Há documentação complementar? ('S' ou 'N')")
    if documentacao_complementar == "S" and idade >= 18:
      print("Cadastro em Revisao")
    else:
      print("Cadastro Recusado")
  elif idade >= 18:
    print("Cadastro Aprovado")
  else:
    print("Cadastro Recusado")
elif tipo_pessoa == "pj":
  cnpj = input("Qual o CNPJ da empresa? (apenas números)")
  if len(cnpj) != 14:
    registro_provisorio = input("Há registro provisório? ('S' ou 'N')")
    if registro_provisorio == "S":
      print("Cadastro em Revisao")
    else:
      print("Cadastro Recusado")
  else:
    print("Cadastro Aprovado")
else:
  print("Você entrou com um tipo de pessoa inválido")