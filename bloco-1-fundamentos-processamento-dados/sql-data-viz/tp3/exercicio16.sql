SELECT
    nome_vendedor,
    regiao
FROM
    vendedores
WHERE
    (regiao = 'Sul' OR regiao = 'Norte')
    AND meta_atingida = 'SIM';