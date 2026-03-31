-- Também coloquei na ordem de título pra ficar bonitinho
SELECT
    titulo,
    genero,
    nota_media
FROM
    filmes
WHERE
    genero IN ('Ação', 'Drama', 'Ficção Científica')
ORDER BY nota_media ASC, titulo;