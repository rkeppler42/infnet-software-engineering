CREATE TABLE turmas (
    id_turma INTEGER PRIMARY KEY,
    id_disciplina INTEGER REFERENCES disciplinas (id_disciplina) NOT NULL,
    id_professor INTEGER REFERENCES professores (id_professor) NOT NULL,
    semestre TEXT,
    horario TEXT
);