CREATE TABLE matriculas (
    id_aluno INTEGER REFERENCES alunos (id_aluno),
    id_turma INTEGER REFERENCES turmas (id_turma),
    nota REAL,
    frequencia INTEGER,
    CONSTRAINT matriculas_key PRIMARY KEY (id_aluno, id_turma)
);