CREATE TABLE alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    curso TEXT
);

CREATE TABLE professores (
    id_professor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    departamento TEXT
);

CREATE TABLE disciplinas (
    id_disciplina INTEGER PRIMARY KEY,
    nome TEXT UNIQUE NOT NULL,
    carga_horaria INTEGER,
    area_conhecimento TEXT
);

CREATE TABLE turmas (
    id_turma INTEGER PRIMARY KEY,
    id_disciplina INTEGER NOT NULL REFERENCES disciplinas (id_disciplina),
    id_professor INTEGER NOT NULL REFERENCES professores (id_professor),
    semestre TEXT,
    horario TEXT
);

CREATE TABLE matriculas (
    id_aluno INTEGER NOT NULL REFERENCES alunos (id_aluno),
    id_turma INTEGER NOT NULL REFERENCES turmas (id_turma),
    nota REAL,
    frequencia INTEGER,
    CONSTRAINT matriculas_key PRIMARY KEY (id_aluno, id_turma)
);