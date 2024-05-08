from Database import Database
import plotly.express as px
import pandas as pd

database = Database()

student = database.findStudent("47180957860")
print(student["nome"])
print("-----")

def removeDuplicates(lista):
    lista_2 = []
    for disc in lista:
        if disc not in lista_2:
            lista_2.append(disc)
    
    return lista_2

# Função que recebe um estudante e exibe suas pontuações nos simulados feitos

def compareSimulates(student, database, focus="Total"):
    simulados = student["Simulados"].keys()

    disciplinas = []
        
    for simulado in simulados:
        disciplinas.extend(student['Simulados'][simulado]['Acertos'].keys())

    disciplinas = removeDuplicates(disciplinas)
    
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

    fig = px.bar(df, x="Disciplinas", y="Acertos", color="Simulados", barmode="group", title=f"Comparação de Provas | {student['nome']} | Focus = {focus}",
                 color_discrete_map=color_map)

    for simulado in metricas_simulados.keys():
        y = metricas_simulados[simulado]["Métricas"][focus]["Media"]
        fig.add_hline(y=y, line_dash="dash", annotation_text=f"Média {simulado}", annotation_position="top left",
                      line_color=color_map.get(simulado, "black"))

    fig.show()
    
    return df

compareSimulates(student, database, focus="Total")   
