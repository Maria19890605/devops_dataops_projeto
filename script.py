import duckdb

# Conectar ao banco DuckDB
conn = duckdb.connect("dados.db")

# Criar a tabela (sem autoincremento direto)
conn.execute("""
CREATE TABLE IF NOT EXISTS inscricoes (
    id BIGINT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade INTEGER,
    curso TEXT NOT NULL,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

print("✅ Banco e tabela 'inscricoes' criados com sucesso.")
conn.close()

