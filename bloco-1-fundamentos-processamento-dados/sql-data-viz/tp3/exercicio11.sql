SELECT
    *
FROM
    pedidos
WHERE
    status != 'CANCELADO'
    AND (valor_total >= 300 OR data_pedido >= '2024-02-01');