exploracao = abs(int(input()))
combate = abs(int(input()))
estrategia = abs(int(input()))
sincronia_tatica = 2 * estrategia + exploracao // 2
gasto_excessivo = 3 * (combate % 10)
maestria = exploracao // 5 + 1

pontuacao_resultante = exploracao + combate + estrategia + sincronia_tatica - gasto_excessivo
pontuacao_final = pontuacao_resultante * maestria
print(f"Pontuação Final em Arcana Quest: {pontuacao_final} pontos.")