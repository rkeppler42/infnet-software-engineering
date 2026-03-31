SELECT
    nome_vendedor,
    regiao
FROM
    vendedores
WHERE
    meta_atingida = 'SIM'
    AND regiao != 'Sudeste';