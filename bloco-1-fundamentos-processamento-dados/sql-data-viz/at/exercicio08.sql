SELECT
    genero,
    COUNT(genero) as numero_de_filmes,
    ROUND(AVG(nota_media), 2) as nota_media,
    MIN(nota_media),
    MAX(nota_media)
FROM
    filmes
WHERE
    duracao_min >= 80
    AND (classificacao = 'Livre' OR classificacao = '12 anos')
GROUP BY 
    genero
HAVING 
    COUNT(genero) > 1
ORDER BY 
    ROUND(AVG(nota_media), 2) DESC;
