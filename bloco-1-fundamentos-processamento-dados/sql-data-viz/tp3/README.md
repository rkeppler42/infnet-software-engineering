# TP3 – Introdução à Visualização de Dados e SQL

Performance Test 3. Covers SQL SELECT queries with filtering using WHERE, AND, OR, and NOT operators across four related tables.

> 🗄️ All queries run against the same database schema: `produtos`, `clientes`, `pedidos`, and `vendedores`.

---

## Schema

```sql
-- produtos: id, nome, categoria, preco_unitario, estoque
-- clientes: id_cliente, nome_completo, cidade, estado, tipo_plano
-- pedidos:  num_pedido, data_pedido, id_cliente, valor_total, status
-- vendedores: id_vendedor, nome_vendedor, regiao, vendas_mes, meta_atingida
```

---

## Exercises

### Ex01 – Full Table Scan
Return all columns and rows from the `produtos` table.

### Ex02 – SELECT with Multiple Filters (Marketing)
Return `nome` and `preco_unitario` of products in the 'Periféricos' category with more than 5 units in stock.

### Ex03 – WHERE with Exact Match
Return all columns of products whose category is exactly 'Periféricos'.

### Ex04 – WHERE with AND and NOT
Return `nome`, `categoria`, and `estoque` of products with `preco_unitario` above 500.00, `estoque` below 10, and category not equal to 'Periféricos'.

### Ex05 – WHERE with String Filter
Return `nome_completo` and `cidade` of customers from the state of 'SP'.

### Ex06 – WHERE with OR (State and Plan)
Return all columns of customers whose state is 'PR' or 'RS', or whose plan is 'Gold'.

### Ex07 – WHERE with AND and NOT
Return `nome`, `cidade`, and `estado` of customers whose plan is not 'Free' and state is not 'SP'.

### Ex08 – WHERE with NOT
Return `nome` and `estado` of all customers whose plan is not 'Free'.

### Ex09 – WHERE with AND and OR (Orders)
Return all details of orders with `valor_total` above 1000.00 and status 'ENVIADO' or 'PROCESSANDO'.

### Ex10 – WHERE with AND (Delivered High-Value Orders)
Return `num_pedido` and `valor_total` of orders with status 'ENTREGUE' and `valor_total` above 300.00.

### Ex11 – WHERE with AND, OR and NOT
Return all columns of orders where status is not 'CANCELADO' and `valor_total` >= 300.00, or `data_pedido` is after 2024-02-01.

### Ex12 – WHERE with AND and OR (Date and Value)
Return orders with `data_pedido` >= 2024-01-20 and `valor_total` < 200.00, or status 'PROCESSANDO'.

### Ex13 – WHERE with AND and NOT (Salespeople)
Return `nome_vendedor` and `regiao` of salespeople who reached their target and are not from the 'Sudeste' region.

### Ex14 – WHERE with Multiple AND (Top Performers)
Return `nome_vendedor` and `vendas_mes` of salespeople from 'Sudeste' who reached their target and made more than 40 sales.

### Ex15 – WHERE with BETWEEN-like Filter
Return all data of salespeople with `vendas_mes` greater than 20 and less than 40.

### Ex16 – WHERE with OR and AND (Regional Conference)
Return `nome_vendedor` and `regiao` of salespeople from 'Sul' or 'Norte' who reached their target.

---

# TP3 – Introdução à Visualização de Dados e SQL

Teste de Performance 3. Cobre queries SQL SELECT com filtragem usando WHERE, AND, OR e NOT em quatro tabelas relacionadas.

> 🗄️ Todas as queries rodam no mesmo schema: `produtos`, `clientes`, `pedidos` e `vendedores`.

---

## Schema

```sql
-- produtos:   id, nome, categoria, preco_unitario, estoque
-- clientes:   id_cliente, nome_completo, cidade, estado, tipo_plano
-- pedidos:    num_pedido, data_pedido, id_cliente, valor_total, status
-- vendedores: id_vendedor, nome_vendedor, regiao, vendas_mes, meta_atingida
```

---

## Exercícios

### Ex01 – Varredura Completa da Tabela
Retornar todas as colunas e linhas da tabela `produtos`.

### Ex02 – SELECT com Múltiplos Filtros (Marketing)
Retornar `nome` e `preco_unitario` dos produtos da categoria 'Periféricos' com mais de 5 unidades em estoque.

### Ex03 – WHERE com Correspondência Exata
Retornar todas as colunas dos produtos cuja categoria seja exatamente 'Periféricos'.

### Ex04 – WHERE com AND e NOT
Retornar `nome`, `categoria` e `estoque` dos produtos com `preco_unitario` acima de 500.00, `estoque` abaixo de 10 e categoria diferente de 'Periféricos'.

### Ex05 – WHERE com Filtro de String
Retornar `nome_completo` e `cidade` dos clientes do estado 'SP'.

### Ex06 – WHERE com OR (Estado e Plano)
Retornar todas as colunas dos clientes cujo estado seja 'PR' ou 'RS', ou cujo plano seja 'Gold'.

### Ex07 – WHERE com AND e NOT
Retornar `nome`, `cidade` e `estado` dos clientes cujo plano não seja 'Free' e o estado não seja 'SP'.

### Ex08 – WHERE com NOT
Retornar `nome` e `estado` de todos os clientes cujo plano não seja 'Free'.

### Ex09 – WHERE com AND e OR (Pedidos)
Retornar todos os detalhes dos pedidos com `valor_total` acima de 1000.00 e status 'ENVIADO' ou 'PROCESSANDO'.

### Ex10 – WHERE com AND (Pedidos Entregues de Alto Valor)
Retornar `num_pedido` e `valor_total` dos pedidos com status 'ENTREGUE' e `valor_total` acima de 300.00.

### Ex11 – WHERE com AND, OR e NOT
Retornar todas as colunas dos pedidos onde o status não seja 'CANCELADO' e `valor_total` >= 300.00, ou `data_pedido` seja após 2024-02-01.

### Ex12 – WHERE com AND e OR (Data e Valor)
Retornar pedidos com `data_pedido` >= 2024-01-20 e `valor_total` < 200.00, ou status 'PROCESSANDO'.

### Ex13 – WHERE com AND e NOT (Vendedores)
Retornar `nome_vendedor` e `regiao` dos vendedores que atingiram a meta e não são do Sudeste.

### Ex14 – WHERE com Múltiplos AND (Top Performers)
Retornar `nome_vendedor` e `vendas_mes` dos vendedores do Sudeste que atingiram a meta e fizeram mais de 40 vendas.

### Ex15 – WHERE com Filtro tipo BETWEEN
Retornar todos os dados dos vendedores com `vendas_mes` maior que 20 e menor que 40.

### Ex16 – WHERE com OR e AND (Conferência Regional)
Retornar `nome_vendedor` e `regiao` dos vendedores do 'Sul' ou 'Norte' que atingiram a meta.