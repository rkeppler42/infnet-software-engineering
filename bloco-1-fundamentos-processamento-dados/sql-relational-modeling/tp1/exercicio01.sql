CREATE TABLE matriculas (
    id_aluno INTEGER,
    id_turma INTEGER,
    nota REAL,
    frequencia INTEGER,
    CONSTRAINT matriculas_key PRIMARY KEY (id_aluno, id_turma)
);