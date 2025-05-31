import streamlit as st
import duckdb
from datetime import datetime

# Título da aplicação
st.title("🎓 Formulário de Inscrição na Faculdade")

# Conectar ao banco de dados DuckDB
conn = duckdb.connect("dados.db")

# Formulário de inscrição
with st.form("form_inscricao"):
    nome = st.text_input("Nome completo *")
    email = st.text_input("E-mail *")
    idade = st.number_input("Idade", min_value=15, max_value=100, step=1)
    curso = st.selectbox("Curso desejado *", ["Selecione", "Engenharia de Dados", "Análise e Desenvolvimento de Sistemas", "Ciência da Computação", "Administração"])

    enviar = st.form_submit_button("Enviar inscrição")

    if enviar:
        if nome.strip() and email.strip() and curso != "Selecione":
            # Gerar próximo ID manualmente
            ultimo_id = conn.execute("SELECT MAX(id) FROM inscricoes").fetchone()[0]
            proximo_id = 1 if ultimo_id is None else ultimo_id + 1

            # Inserir os dados
            conn.execute("""
                INSERT INTO inscricoes (id, nome, email, idade, curso, data_inscricao)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (proximo_id, nome, email, idade, curso, datetime.now()))

            st.success("✅ Inscrição realizada com sucesso!")
        else:
            st.warning("⚠️ Por favor, preencha todos os campos obrigatórios marcados com *.")

# Visualização opcional dos dados
st.markdown("---")
if st.checkbox("📋 Visualizar inscrições realizadas"):
    df = conn.execute("SELECT * FROM inscricoes ORDER BY data_inscricao DESC").fetchdf()
    st.dataframe(df, use_container_width=True)

conn.close()
