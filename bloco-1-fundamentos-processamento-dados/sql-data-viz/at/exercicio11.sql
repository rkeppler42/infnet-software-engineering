SELECT
    nome_funcionario,
    estado,
    salario
FROM 
    funcionarios
WHERE
    (estado in ('RJ', 'MG') AND salario > 3000)
    OR estado = 'SP'
ORDER BY 
    estado DESC,
    nome_funcionario ASC;