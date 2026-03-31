SELECT
    estado,
    COUNT(nome_funcionario) AS funcionarios_ativos,
    COUNT(DISTINCT setor) as numero_de_setores,
    MIN(salario) As menor_salario,
    MAX(salario) AS maior_salario
FROM
    funcionarios
WHERE
    status_ativo = 'SIM'
    AND idade >= 18
    AND estado In ('SP', 'RJ', 'MG', 'PR')
GROUP BY 
    estado
HAVING 
    COUNT(nome_funcionario) > 2
ORDER By 
    COUNT(nome_funcionario) DESC;