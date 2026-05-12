CREATE TABLE disciplinas (
    id_disciplina INTEGER PRIMARY KEY,
    nome TEXT UNIQUE NOT NULL,
    carga_horaria INTEGER,
    area_conhecimento TEXT
);