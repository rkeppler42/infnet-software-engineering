SELECT
    titulo,
    duracao_min,
    nota_media
FROM
    filmes
WHERE
    duracao_min > 90
    AND nota_media < 8.5
    AND disponivel_catal = 'SIM';