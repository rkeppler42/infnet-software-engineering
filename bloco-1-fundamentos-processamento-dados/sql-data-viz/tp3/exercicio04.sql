SELECT
    nome,
    categoria,
    estoque
FROM
    produtos
WHERE
    categoria != 'Periféricos'
    AND preco_unitario > 500
    AND estoque < 10;