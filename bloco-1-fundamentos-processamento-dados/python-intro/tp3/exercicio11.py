velocidade_do_vento = int(input("Qual a velocidade do vento?\n> "))
temperatura = int(input("Qual a temperatura em graus Celsius?\n> "))
umidade_do_ar = int(input("Qual a umidade do ar?\n> "))
tipo_de_precipitacao = input("Qual o tipo de precipitação? ('Chuva', 'Neve', 'Granizo' ou 'Nenhum')").lower()

if velocidade_do_vento > 80 or (tipo_de_precipitacao == "granizo" and velocidade_do_vento > 60):
  print("ALERTA VERMELHO (Perigo Iminente)")
elif (temperatura < -10
      or (tipo_de_precipitacao == "neve" and velocidade_do_vento > 40)
      or (tipo_de_precipitacao == "neve" and temperatura < 0)
      or velocidade_do_vento > 50):
  print("ALERTA LARANJA (Cuidado)")
elif ((tipo_de_precipitacao == "chuva" and velocidade_do_vento > 40 and umidade_do_ar > 90)
      or velocidade_do_vento > 20
      or umidade_do_ar > 80): 
  print("ALERTA AMARELO (Atenção)")
elif ((tipo_de_precipitacao == "nenhum" and temperatura < 5 and velocidade_do_vento > 30)
      or temperatura < 10
      or umidade_do_ar > 75
      or tipo_de_precipitacao == "chuva"):
  print("ALERTA AZUL (Observação)")
else:
  print("SEM ALERTA")