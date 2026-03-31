SELECT *
FROM pedidos
WHERE
    valor_total > 1000
    AND (status = 'ENVIADO' OR status = 'PROCESSANDO');