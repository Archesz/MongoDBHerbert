import plotly.express as px
import pandas as pd
import utils 
import plotly.graph_objects as go

def compareSimulates(student, database):
    
    simulados = student["Simulados"].keys()

    disciplinas = []
        
    for simulado in simulados:
        disciplinas.extend(student['Simulados'][simulado]['Acertos'].keys())

    disciplinas = utils.removeDuplicates(disciplinas)
        
    metricas_simulados = {}
    
    for simulado in simulados:    
        simulado_find = database.findSimulado(simulado)
        metricas_simulados[simulado] = simulado_find

    provas = []
    disciplinas_list = []
    acertos = []
    
    for simulado in simulados:
        for disciplina in disciplinas:
            try:
                acertos.append(student["Simulados"][simulado]["Acertos"][disciplina])
                provas.append(simulado)
                disciplinas_list.append(disciplina)
            except:
                acertos.append(0)
                provas.append(simulado)
                disciplinas_list.append(disciplina)
            
    df = pd.DataFrame({"Acertos": acertos, "Simulados": provas, "Disciplinas": disciplinas_list})

    color_map = {
        "Colmeias_Inicial": "#585191",
        "Unicamp_00001": "#EF6461",
        "USP_00001": "#61D095"
    }

    fig = px.bar(df, x="Disciplinas", y="Acertos", color="Simulados", barmode="group", title=f"Comparação de Provas | {student['nome']}",
                 color_discrete_map=color_map)
    
    return fig

def compareTotal(student, database, focus="Total"):
    simulados = student["Simulados"].keys()

    disciplinas = []
        
    for simulado in simulados:
        disciplinas.extend(student['Simulados'][simulado]['Acertos'].keys())

    disciplinas = utils.removeDuplicates(disciplinas)
    
    metricas_simulados = {}
    
    for simulado in simulados:    
        simulado_find = database.findSimulado(simulado)
        metricas_simulados[simulado] = simulado_find
        
    provas = []
    disciplinas_list = []
    acertos = []
    
    for simulado in simulados:
        for disciplina in disciplinas:
            try:
                acertos.append(student["Simulados"][simulado]["Acertos"][disciplina])
                provas.append(simulado)
                disciplinas_list.append(disciplina)
            except:
                acertos.append(0)
                provas.append(simulado)
                disciplinas_list.append(disciplina)
            
    df = pd.DataFrame({"Acertos": acertos, "Simulados": provas, "Disciplinas": disciplinas_list}).query("Disciplinas == 'Total'")

    color_map = {
        "Colmeias_Inicial": "#585191",
        "Unicamp_00001": "#EF6461",
        "USP_00001": "#61D095"
    }

    fig = px.bar(df, x="Disciplinas", y="Acertos", color="Simulados", barmode="group", title=f"Comparação de Provas | {student['nome']} | Focus = {focus}",
                 color_discrete_map=color_map)

    for simulado in metricas_simulados.keys():
        y = metricas_simulados[simulado]["Métricas"][focus]["Media"]
        fig.add_hline(y=y, line_dash="dash", annotation_text=f"Média {simulado}", annotation_position="top left",
                      line_color=color_map.get(simulado, "black"))
    
    return fig

def plotBoxDisciplinas(students, disciplina="Matemática", distincao="Periodo"):
    cpfs = list(students.keys()) 
    disciplinas_list = []
    acertos = []
    periodos = []
    generos = []
    etnias = []

    for cpf in cpfs:
        v = students[cpf]["simulado"]["Acertos"][disciplina]
        disciplinas_list.append(disciplina)
        periodos.append(students[cpf]["periodo"])
        generos.append(students[cpf]["genero"])
        etnias.append(students[cpf]["etnia"])
        acertos.append(v)
            
    df = pd.DataFrame({"Disciplina": disciplinas_list, "Periodo": periodos, "Genero": generos, "Etnia": etnias, "Acertos": acertos})
    
    fig = px.box(df, y="Acertos", x=distincao, color=distincao)

    fig.update_layout(
        height=500, 
        width=700,
        title=f"Desempenho & {distincao}",
        yaxis_title="Acertos",
        showlegend=False
    )
    
    return fig

def scatterNotas(students, disciplina="Matemática"):
    cpfs = list(students.keys()) 
    nomes = []
    totais = []
    disciplinas_list = []
    acertos = []
    periodos = []
    generos = []
    etnias = []

    for cpf in cpfs:
        v = students[cpf]["simulado"]["Acertos"][disciplina]
        disciplinas_list.append(disciplina)
        totais.append(students[cpf]["simulado"]["Acertos"]["Total"])
        periodos.append(students[cpf]["periodo"])
        generos.append(students[cpf]["genero"])
        etnias.append(students[cpf]["etnia"])
        acertos.append(v)
        nomes.append(students[cpf]["nome"])
        
    df = pd.DataFrame({"Nome": nomes, "Total": totais, "Disciplina": disciplinas_list, "Periodo": periodos, "Genero": generos, "Etnia": etnias, "Acertos": acertos})
    
    fig = px.scatter(df, y="Total", x=acertos, hover_data=["Nome"])

    fig.update_layout(
        height=500, 
        width=900,
        title=f"Desempenho",
        showlegend=False,
        xaxis_title=disciplina
    )
    
    return fig

def getTable(students, disciplina="Matemática"):
    cpfs = list(students.keys()) 
    nomes = []
    acertos = []

    for cpf in cpfs:
        v = students[cpf]["simulado"]["Acertos"][disciplina]
        acertos.append(v)
        nomes.append(students[cpf]["nome"])
        
    df = pd.DataFrame({"Nome": nomes, "Acertos": acertos})
    
    # Ordenando o DataFrame em ordem decrescente de acertos
    df = df.sort_values(by="Acertos", ascending=False)
    
    # Criando a tabela com estilo
    table = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df.Nome, df.Acertos],
                   fill_color='lavender',
                   align='left'))
    ])
    
    table.update_layout(
        title="Tabela de Acertos por Aluno",
        height=400,
        width=600
    )
    
    return table

