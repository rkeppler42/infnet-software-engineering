SELECT
    nome_produto,
    preco,
    status_venda
FROM
    produtos_mercado
WHERE
    status_venda IN ('Disponível', 'Promoção')
ORDER BY 
    preco DESC;