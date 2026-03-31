SELECT
    num_pedido,
    valor_total
FROM
    pedidos
WHERE
    status = 'ENTREGUE'
    AND valor_total > 300;