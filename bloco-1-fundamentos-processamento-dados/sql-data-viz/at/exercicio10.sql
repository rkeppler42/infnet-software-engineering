SELECT 
    nome_funcionario,
    salario,
    idade,
    estado
FROM 
    funcionarios
WHERE
    idade > 25
    AND salario > 4000
    AND estado in ('SP', 'RJ', 'MG')
    AND status_ativo = 'SIM'
ORDER BY 
    idade DESC;