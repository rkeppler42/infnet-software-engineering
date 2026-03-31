SELECT 
    nome_funcionario, 
    cidade, 
    estado
FROM 
    funcionarios
WHERE
    status_ativo = 'SIM';