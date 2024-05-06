import plotly.express as px
import pandas as pd

def plotScatter(data, disciplina, disciplina2):
    for i in range(0, len(data)):
        try:
            data[i][f"{disciplina}"] = data[i]["simulado"]["Acertos"][disciplina]
        except:
            pass

    for i in range(0, len(data)):
        try:
            data[i][f"{disciplina2}"] = data[i]["simulado"]["Acertos"][disciplina2]
        except:
            pass

    df = pd.DataFrame(data)
    
    fig = px.scatter(df, x=disciplina, y=disciplina2, color="genero", hover_data=["nome"])
    fig.show()

def viewStudent(cpf, resultados):
    aluno = resultados[0][cpf]
    
    for simulado in resultados:
        print(simulado)