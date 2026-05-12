# TP1 – SQL and Relational Modeling

This assignment covers relational table creation, primary keys, foreign keys, uniqueness constraints, required fields, and complete database schema validation.

## Reference Schema

| Table         | Attributes                                                                                                                                      |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `alunos`      | `id_aluno` (`INTEGER`, PK)<br>`nome` (`TEXT`, `NOT NULL`)<br>`email` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`curso` (`TEXT`)                         |
| `professores` | `id_professor` (`INTEGER`, PK)<br>`nome` (`TEXT`, `NOT NULL`)<br>`email` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`departamento` (`TEXT`)              |
| `disciplinas` | `id_disciplina` (`INTEGER`, PK)<br>`nome` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`carga_horaria` (`INTEGER`)<br>`area_conhecimento` (`TEXT`)         |
| `turmas`      | `id_turma` (`INTEGER`, PK)<br>`id_disciplina` (`INTEGER`, FK)<br>`id_professor` (`INTEGER`, FK)<br>`semestre` (`TEXT`)<br>`horario` (`TEXT`)    |
| `matriculas`  | `id_aluno` (`INTEGER`, FK)<br>`id_turma` (`INTEGER`, FK)<br>`nota` (`REAL`)<br>`frequencia` (`INTEGER`)<br>Composite PK: `id_aluno`, `id_turma` |

---

## Exercises

### Ex01 – Composite Primary Key

Define a composite `PRIMARY KEY` in the `matriculas` table to prevent duplicate enrollments for the same student in the same class.

### Ex02 – Foreign Keys

Add `FOREIGN KEY` constraints to the `matriculas` table so each enrollment references valid students and classes.

### Ex03 – NOT NULL Constraints

Create the `alunos` table with required `nome` and `email` fields using `NOT NULL`.

### Ex04 – UNIQUE Constraint

Create the `professores` table with a unique and required `email` field to prevent duplicate professor records.

### Ex05 – UNIQUE and NOT NULL

Create the `disciplinas` table ensuring each discipline name is required and unique.

### Ex06 – Multiple Foreign Keys

Create the `turmas` table with foreign keys linking each class to a valid discipline and professor.

### Ex07 – Primary Key, NOT NULL, and UNIQUE

Create the `alunos` table combining a primary key, required fields, and a unique email constraint.

### Ex08 – Relational Decomposition

Reorganize fields from a spreadsheet into coherent relational tables using `alunos`, `disciplinas`, and `matriculas`.

### Ex09 – Chained Relationships

Implement related tables where enrollments reference students and classes, and classes reference existing disciplines.

### Ex10 – Complete Schema Validation

Create the full database schema with all main tables and their primary keys, foreign keys, required fields, and uniqueness constraints.

---

# TP1 – SQL e Modelagem Relacional

Este trabalho cobre criação de tabelas relacionais, chaves primárias, chaves estrangeiras, restrições de unicidade, campos obrigatórios e validação completa de esquema de banco de dados.

## Esquema de Referência

| Tabela        | Atributos                                                                                                                                      |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `alunos`      | `id_aluno` (`INTEGER`, PK)<br>`nome` (`TEXT`, `NOT NULL`)<br>`email` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`curso` (`TEXT`)                        |
| `professores` | `id_professor` (`INTEGER`, PK)<br>`nome` (`TEXT`, `NOT NULL`)<br>`email` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`departamento` (`TEXT`)             |
| `disciplinas` | `id_disciplina` (`INTEGER`, PK)<br>`nome` (`TEXT`, `UNIQUE`, `NOT NULL`)<br>`carga_horaria` (`INTEGER`)<br>`area_conhecimento` (`TEXT`)        |
| `turmas`      | `id_turma` (`INTEGER`, PK)<br>`id_disciplina` (`INTEGER`, FK)<br>`id_professor` (`INTEGER`, FK)<br>`semestre` (`TEXT`)<br>`horario` (`TEXT`)   |
| `matriculas`  | `id_aluno` (`INTEGER`, FK)<br>`id_turma` (`INTEGER`, FK)<br>`nota` (`REAL`)<br>`frequencia` (`INTEGER`)<br>PK composta: `id_aluno`, `id_turma` |

---

## Exercícios

### Ex01 – Chave Primária Composta

Definir uma `PRIMARY KEY` composta na tabela `matriculas` para impedir matrículas duplicadas do mesmo aluno na mesma turma.

### Ex02 – Chaves Estrangeiras

Adicionar restrições de `FOREIGN KEY` na tabela `matriculas` para que cada matrícula referencie alunos e turmas válidos.

### Ex03 – Restrições NOT NULL

Criar a tabela `alunos` com os campos obrigatórios `nome` e `email` usando `NOT NULL`.

### Ex04 – Restrição UNIQUE

Criar a tabela `professores` com o campo `email` obrigatório e único para evitar cadastros duplicados.

### Ex05 – UNIQUE e NOT NULL

Criar a tabela `disciplinas` garantindo que o nome de cada disciplina seja obrigatório e exclusivo.

### Ex06 – Múltiplas Chaves Estrangeiras

Criar a tabela `turmas` com chaves estrangeiras ligando cada turma a uma disciplina e a um professor válidos.

### Ex07 – Primary Key, NOT NULL e UNIQUE

Criar a tabela `alunos` combinando chave primária, campos obrigatórios e restrição de unicidade para o e-mail.

### Ex08 – Decomposição Relacional

Reorganizar campos vindos de uma planilha em tabelas relacionais coerentes usando `alunos`, `disciplinas` e `matriculas`.

### Ex09 – Relacionamentos Encadeados

Implementar tabelas relacionadas em que matrículas referenciam alunos e turmas, e turmas referenciam disciplinas existentes.

### Ex10 – Validação de Esquema Completo

Criar o esquema completo do banco com todas as tabelas principais e suas chaves primárias, chaves estrangeiras, campos obrigatórios e restrições de unicidade.
