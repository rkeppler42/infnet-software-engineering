SELECT
    categoria,
    COUNT(DISTINCT nome_produto),
    ROUND(AVG(preco), 2) AS preco_medio,
    SUM(preco) AS soma_preco,
    MIN(preco) AS preco_minimo,
    MAX(preco) AS preco_maximo
FROM
    produtos_mercado
WHERE 
    preco >= 20
    AND estoque > 10
    AND (status_venda = 'Disponível' OR status_venda = 'Promoção')
GROUP BY 
    categoria
HAVING 
    COUNT(DISTINCT nome_produto) >= 3
ORDER BY
    AVG(preco) DESC;