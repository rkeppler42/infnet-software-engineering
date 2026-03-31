# AT – Introdução à Visualização de Dados e SQL

Assessment (graded). Covers Google Looker Studio dashboard building and SQL queries using SELECT, WHERE, GROUP BY, HAVING, ORDER BY, and aggregation functions.

> 📊 The Looker Studio report is linked directly from the published report.
> 📝 SQL exercise files are written in Portuguese, as required by the institution.

---

## Part 1 – Data Visualization (Google Looker Studio)

All four exercises are part of a single report with a consistent visual identity themed around a fitness academy.

**Data source:** `uso_academia` CSV imported into Google Sheets and connected to Looker Studio.

### Ex01 – Data Table (Page 1)
Connect the CSV data source via Google Sheets and display a table with the fields: `data_aula`, `unidade`, `modalidade`, `professor`, `inscritos`, and `presentes`.

### Ex02 – Participation Indicators (Page 2)
Add scorecards for total enrolled and total present, plus a bar chart showing attendance by class type.

### Ex03 – Interactive Analysis (Page 3)
Build a bar chart by unit, a pie chart by class type, and a time series chart by `data_aula`. Add filters for unit, class type, and a date range control.

### Ex04 – Executive Dashboard (Page 4)
Design a final shareable dashboard with at least 2 scorecards, 2 charts, and 2 interactive controls. Configure the report for external sharing.

---

## Part 2 – SQL

### Schema
```sql
-- filmes:          titulo, genero, classificacao, duracao_min, nota_media, disponivel_catal
-- funcionarios:    nome_funcionario, cidade, estado, idade, salario, status_ativo, setor
-- produtos_mercado: nome_produto, categoria, estoque, preco, status_venda
```

### Ex05 – WHERE (Available Films)
List films available in the catalog, showing title, genre, and rating.

### Ex06 – WHERE with Multiple Filters (Editorial Selection)
Show films with more than 90 minutes, average rating below 8.5, and available in the catalog. Display title, duration, and rating.

### Ex07 – IN and ORDER BY (Genre Curation)
Present films from the genres Ação, Drama, and Ficção Científica, showing title, genre, and rating, sorted from lowest to highest rating.

### Ex08 – GROUP BY, HAVING and Aggregation (Genre Summary)
Summarize available films with at least 80 minutes and classification Livre or 12 years by genre, showing count, average, min, and max rating. Show only genres with more than one film, ordered by best average rating.

### Ex09 – WHERE (Active Employees)
List active employees showing name, city, and state.

### Ex10 – WHERE with AND and IN (HR Screening)
Show active employees over 25 years old, earning above 4000, located in SP, RJ, or MG. Display name, salary, age, and state, ordered from oldest to youngest.

### Ex11 – WHERE with AND, OR and ORDER BY (Regional Analysis)
Show employees from RJ and MG with salary above 3000, or any employee from SP. Display name, state, and salary, ordered by state descending and name ascending.

### Ex12 – GROUP BY, HAVING and Aggregation (State Summary)
Summarize active employees aged 18 or older in SP, RJ, MG, and PR by state, showing employee count, distinct sectors, min and max salary. Show only states with more than two employees, ordered by highest count.

### Ex13 – WHERE (Available Products)
List all products available for sale with all registered information.

### Ex14 – WHERE with AND, OR and IN (Stock Monitoring)
Show Alimentos and Bebidas products with stock below 50, or any product with status 'Indisponível'. Display name, category, stock, and sale status.

### Ex15 – WHERE and ORDER BY (Commercial Catalog)
Present products that are available or on promotion, showing name, price, and sale status, ordered from most to least expensive.

### Ex16 – GROUP BY, HAVING and Aggregation (Category Summary)
Summarize products with price >= 20, stock above 10, and available or on promotion by category, showing count, average price, sum, min, and max price. Show only categories with at least three products, ordered by highest average price.

---

# AT – Introdução à Visualização de Dados e SQL

Assessment (com nota). Cobre construção de dashboards no Google Looker Studio e queries SQL com SELECT, WHERE, GROUP BY, HAVING, ORDER BY e funções de agregação.

> 📊 O relatório do Looker Studio está vinculado pelo link do relatório publicado.
> 📝 Os arquivos de exercícios SQL estão escritos em português, conforme exigido pela instituição.

---

## Parte 1 – Visualização de Dados (Google Looker Studio)

Os quatro exercícios fazem parte de um único relatório com identidade visual consistente e temática de academia.

**Fonte de dados:** CSV `uso_academia` importado para o Google Sheets e conectado ao Looker Studio.

### Ex01 – Tabela de Dados (Página 1)
Conectar a fonte de dados via Google Sheets e exibir uma tabela com os campos: `data_aula`, `unidade`, `modalidade`, `professor`, `inscritos` e `presentes`.

### Ex02 – Indicadores de Participação (Página 2)
Adicionar scorecards com o total de inscritos e total de presentes, mais um gráfico de barras com a quantidade de presentes por modalidade.

### Ex03 – Análise Interativa (Página 3)
Construir um gráfico de barras por unidade, um gráfico de pizza por modalidade e um gráfico de série temporal por `data_aula`. Adicionar filtros por unidade, modalidade e controle de período.

### Ex04 – Dashboard Executivo (Página 4)
Montar uma página final compartilhável com pelo menos 2 scorecards, 2 gráficos e 2 controles interativos. Configurar o relatório para compartilhamento externo.

---

## Parte 2 – SQL

### Schema
```sql
-- filmes:           titulo, genero, classificacao, duracao_min, nota_media, disponivel_catal
-- funcionarios:     nome_funcionario, cidade, estado, idade, salario, status_ativo, setor
-- produtos_mercado: nome_produto, categoria, estoque, preco, status_venda
```

### Ex05 – WHERE (Filmes Disponíveis)
Listar os filmes disponíveis no catálogo, exibindo título, gênero e classificação indicativa.

### Ex06 – WHERE com Múltiplos Filtros (Seleção Editorial)
Mostrar filmes com mais de 90 minutos, nota média abaixo de 8.5 e disponíveis no catálogo. Exibir título, duração e nota média.

### Ex07 – IN e ORDER BY (Curadoria por Gênero)
Apresentar filmes dos gêneros Ação, Drama e Ficção Científica, exibindo título, gênero e nota média, ordenados do menor para o maior valor de nota.

### Ex08 – GROUP BY, HAVING e Agregação (Resumo por Gênero)
Resumir os filmes disponíveis com pelo menos 80 minutos e classificação Livre ou 12 anos por gênero, exibindo contagem, média, mínimo e máximo de nota. Mostrar apenas gêneros com mais de um filme, ordenados pela melhor nota média.

### Ex09 – WHERE (Funcionários Ativos)
Listar os funcionários ativos exibindo nome, cidade e estado.

### Ex10 – WHERE com AND e IN (Triagem de RH)
Mostrar funcionários ativos com mais de 25 anos, salário acima de 4000 e localizados em SP, RJ ou MG. Exibir nome, salário, idade e estado, ordenados do mais velho para o mais novo.

### Ex11 – WHERE com AND, OR e ORDER BY (Análise Regional)
Mostrar funcionários de RJ e MG com salário acima de 3000, ou qualquer funcionário de SP. Exibir nome, estado e salário, ordenados por estado decrescente e nome crescente.

### Ex12 – GROUP BY, HAVING e Agregação (Resumo por Estado)
Resumir funcionários ativos com 18 anos ou mais nos estados SP, RJ, MG e PR por estado, exibindo contagem, setores distintos, menor e maior salário. Mostrar apenas estados com mais de dois funcionários, ordenados pela maior quantidade.

### Ex13 – WHERE (Produtos Disponíveis)
Listar todos os produtos disponíveis para venda com todas as informações cadastradas.

### Ex14 – WHERE com AND, OR e IN (Monitoramento de Estoque)
Mostrar produtos de Alimentos e Bebidas com estoque abaixo de 50, ou qualquer produto com status 'Indisponível'. Exibir nome, categoria, estoque e situação de venda.

### Ex15 – WHERE e ORDER BY (Catálogo Comercial)
Apresentar produtos disponíveis ou em promoção, exibindo nome, preço e situação de venda, ordenados do mais caro para o mais barato.

### Ex16 – GROUP BY, HAVING e Agregação (Resumo por Categoria)
Resumir produtos com preço >= 20, estoque acima de 10 e disponíveis ou em promoção por categoria, exibindo contagem, preço médio, soma, mínimo e máximo. Mostrar apenas categorias com pelo menos três produtos, ordenadas pelo maior preço médio.
