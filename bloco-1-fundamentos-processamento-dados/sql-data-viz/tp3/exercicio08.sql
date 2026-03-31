SELECT
    nome_completo,
    estado
FROM
    clientes
WHERE
    tipo_plano != 'Free';