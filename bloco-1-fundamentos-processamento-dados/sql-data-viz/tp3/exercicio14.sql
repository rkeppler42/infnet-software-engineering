SELECT
    nome_vendedor,
    vendas_mes
FROM
    vendedores
WHERE
    regiao = 'Sudeste'
    AND meta_atingida = 'SIM'
    AND vendas_mes > 40/