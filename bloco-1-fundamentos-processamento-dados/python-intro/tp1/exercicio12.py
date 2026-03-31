dias_percorridos = 125
dias_ininterruptos = 8

fase_atual = 125 % 8
dias_ate_parada = (dias_ininterruptos - fase_atual) % dias_ininterruptos
parada_tecnica = dias_percorridos + dias_ate_parada

print(f"Estamos na fase: {fase_atual}")
print(f"A parada técnica será no dia: {parada_tecnica}")