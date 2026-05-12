CREATE TABLE alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    curso TEXT
);

CREATE TABLE disciplinas (
    id_disciplina INTEGER PRIMARY KEY,
    nome TEXT UNIQUE NOT NULL,
    carga_horaria INTEGER,
    area_conhecimento TEXT
);

CREATE TABLE turmas (
    id_turma INTEGER PRIMARY KEY,
    id_disciplina INTEGER REFERENCES disciplinas (id_disciplina) NOT NULL,
    id_professor INTEGER REFERENCES professores (id_professor) NOT NULL,
    semestre TEXT,
    horario TEXT
);

CREATE TABLE matriculas (
    id_aluno INTEGER REFERENCES alunos (id_aluno),
    id_turma INTEGER REFERENCES turmas (id_turma),
    nota REAL,
    frequencia INTEGER,
    CONSTRAINT matriculas_key PRIMARY KEY (id_aluno, id_turma)
);