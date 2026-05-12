CREATE TABLE professores (
    id_professor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    departamento TEXT
);