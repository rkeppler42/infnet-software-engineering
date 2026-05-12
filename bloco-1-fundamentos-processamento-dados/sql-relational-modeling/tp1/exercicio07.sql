CREATE TABLE alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    curso TEXT
);