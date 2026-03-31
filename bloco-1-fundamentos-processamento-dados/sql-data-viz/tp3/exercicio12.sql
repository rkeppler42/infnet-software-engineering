SELECT
    *
FROM
    pedidos
WHERE
    (data_pedido >= '2024-01-20' AND valor_total < 200)
    OR status = 'PROCESSANDO';