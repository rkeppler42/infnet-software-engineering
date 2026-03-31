SELECT
    nome_produto,
    categoria,
    estoque,
    status_venda
FROM
    produtos_mercado
WHERE
    (categoria IN ('Alimentos', 'Bebidas') AND estoque < 50)
    OR status_venda = 'Indisponível';