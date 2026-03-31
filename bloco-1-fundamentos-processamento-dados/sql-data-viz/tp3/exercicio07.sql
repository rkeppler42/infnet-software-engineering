SELECT
    nome_completo,
    cidade,
    estado
FROM
    clientes
WHERE
    tipo_plano != 'Free'
    AND estado != 'SP';