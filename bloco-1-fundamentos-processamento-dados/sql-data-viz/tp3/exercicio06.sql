SELECT *
FROM
    clientes
WHERE
    estado = 'PR'
    OR estado = 'RS'
    OR tipo_plano = 'Gold';