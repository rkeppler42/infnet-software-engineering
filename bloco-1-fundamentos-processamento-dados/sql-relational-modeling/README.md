# 🗄️ SQL and Relational Modeling

This course introduces the foundations of relational databases, focusing on data modeling, table creation, integrity constraints, and SQL schema definition. The activities explore how to design structured databases using primary keys, foreign keys, required fields, unique constraints, and relationships between entities.

> Exercise files are written in Portuguese as required by the institution.

## Topics Covered

- Relational database modeling
- Entity and table organization
- Primary keys and composite primary keys
- Foreign keys and referential integrity
- `NOT NULL` constraints
- `UNIQUE` constraints
- Table creation with `CREATE TABLE`
- Relational schema validation
- Basic academic database design
- DuckDB usage in Deepnote

## Structure

| Folder          | Description                                                                                          |
| :-------------- | :--------------------------------------------------------------------------------------------------- |
| [`tp1`](./tp1/) | First performance test covering relational table creation, keys, constraints, and schema validation. |
| `tp2`           | Upcoming performance test.                                                                           |
| `tp3`           | Upcoming performance test.                                                                           |
| `at`            | Final graded assessment.                                                                             |

## Highlights

- Modeling enrollments with a composite primary key to prevent duplicate student-class records.
- Applying foreign keys to preserve referential integrity between students, classes, professors, and disciplines.
- Combining `PRIMARY KEY`, `NOT NULL`, and `UNIQUE` constraints in coherent table definitions.
- Building a complete academic database schema with five related tables.
- Validating a relational structure designed for a real-world academic management scenario.

---

# 🗄️ SQL e Modelagem Relacional

Esta disciplina apresenta os fundamentos de bancos de dados relacionais, com foco em modelagem de dados, criação de tabelas, restrições de integridade e definição de esquemas SQL. As atividades exploram como projetar bancos estruturados usando chaves primárias, chaves estrangeiras, campos obrigatórios, restrições de unicidade e relacionamentos entre entidades.

> Os arquivos de exercício estão em português conforme exigido pela instituição.

## Tópicos Abordados

- Modelagem de bancos de dados relacionais
- Organização de entidades e tabelas
- Chaves primárias e chaves primárias compostas
- Chaves estrangeiras e integridade referencial
- Restrições `NOT NULL`
- Restrições `UNIQUE`
- Criação de tabelas com `CREATE TABLE`
- Validação de esquemas relacionais
- Modelagem básica de banco acadêmico
- Uso de DuckDB no Deepnote

## Estrutura

| Pasta           | Descrição                                                                                                         |
| :-------------- | :---------------------------------------------------------------------------------------------------------------- |
| [`tp1`](./tp1/) | Primeiro teste de performance cobrindo criação de tabelas relacionais, chaves, restrições e validação de esquema. |
| `tp2`           | Teste de performance futuro.                                                                                      |
| `tp3`           | Teste de performance futuro.                                                                                      |
| `at`            | Avaliação final com nota.                                                                                         |

## Destaques

- Modelagem de matrículas com chave primária composta para impedir registros duplicados de aluno e turma.
- Aplicação de chaves estrangeiras para preservar a integridade referencial entre alunos, turmas, professores e disciplinas.
- Combinação de restrições `PRIMARY KEY`, `NOT NULL` e `UNIQUE` em definições coerentes de tabelas.
- Construção de um esquema acadêmico completo com cinco tabelas relacionadas.
- Validação de uma estrutura relacional projetada para um cenário realista de gestão acadêmica.
