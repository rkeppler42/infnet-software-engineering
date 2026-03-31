-- Produtos em Promoção também estão disponíveis para venda
SELECT *
FROM produtos_mercado
WHERE status_venda = 'Disponível' OR status_venda = 'Promoção';

-- Se não estiverem segue query correta:
SELECT *
FROM produtos_mercado
WHERE status_venda = 'Disponível';