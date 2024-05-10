import streamlit as st
from Database import Database

st.set_page_config(page_title="Cadastro de Professores")

st.title("Cadastrar Professores")

tab1, tab2 = st.tabs(["Cadastro", "Visualização"])

with tab1:
    
    nome = st.text_input("Nome: ")
    genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Não Binário", "Outros"])
    contato = st.text_input("Whatsapp: ")
    disciplinas = st.multiselect("Disciplinas", ["Matemática", "Física", "Química", "Biologia", "Geografia", "História", "Lingua Portuguesa", "Redação", "Literatura", "Sociologia", "Filosofia", "Humanidades"])
    cursos = st.multiselect("Cursos", ["Pré-Vestibular", "Pré-Técnico"])
    periodos = st.multiselect("Períodos", ["Matutino", "Vespertino", "Noturno", "Sábado"])
    vinculo = st.multiselect("Vinculo", ["Voluntário", "BAS", "Extensão", "Extensão - Pós"])

    cadastrar = st.button("Cadastrar")

    prof = {"Nome": nome, "Genero": genero, "Contato": contato, "Disciplinas": disciplinas, "Cursos": cursos, "Periodo": periodos, "Status": "Ativo", "Vínculo": vinculo}
    
    if cadastrar:
        database = Database()
        database.cadastrarProfessor(prof)
