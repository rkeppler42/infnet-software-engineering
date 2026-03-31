SELECT
    nome, preco_unitario
FROM
    produtos
WHERE
    estoque > 5
    AND categoria = 'Periféricos';