from Database import Database
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import graphs as pg
from simulados import simulados

database = Database()

simulados = list(simulados.keys())
disciplinas = ["Total", "Matemática", "Física", "Química", "Biologia", "Geografia", "História", "Sociologia", "Filosofia", "Literatura", "Português", "Inglês"]
students = database.getNomeCpfDict()
students_list = list(students.keys())

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="Dashboard de Análise"),
    dcc.Dropdown(simulados, id="select_simulado", value=simulados[0]),
    dcc.Dropdown(disciplinas, id="select_disciplina", value=disciplinas[0]),
    html.Div([
        html.Div(id='dd-boxplot-1'),
        html.Div(id='dd-boxplot-2')
    ], style={"display": "flex", "gap": "20px"}),
    html.Div(
        id='dd-boxplot-3'
    ),
    html.Div(id='dd-boxplot-4'),
    html.Div(id='dd-table-5'),
    html.H2(children="Por aluno"),
    dcc.Dropdown(students_list, id="select_students", value=students_list[0]),
    html.Div(id="dd-bar-1")

], style={"display": "flex", "flexDirection": "column", "box-sizing": "border-box", "padding": "20px"})

@callback(
    Output("dd-boxplot-1", "children"),
    Input("select_simulado", 'value'),
    Input("select_disciplina", 'value'),
)
def updateBox1(value, disciplina):
    students = database.getSimulado(value) 
    fig = pg.plotBoxDisciplinas(students, disciplina=disciplina, distincao="Periodo")
    return dcc.Graph(figure=fig)

@callback(
    Output("dd-boxplot-2", "children"),
    Input("select_simulado", 'value'),
    Input("select_disciplina", 'value'),
)
def updateBox2(value, disciplina):
    students = database.getSimulado(value) 
    fig = pg.plotBoxDisciplinas(students, disciplina=disciplina, distincao="Etnia")
    return dcc.Graph(figure=fig)

@callback(
    Output("dd-boxplot-3", "children"),
    Input("select_simulado", 'value'),
    Input("select_disciplina", 'value'),
)
def updateBox3(value, disciplina):
    students = database.getSimulado(value) 
    fig = pg.plotBoxDisciplinas(students, disciplina=disciplina, distincao="Genero")
    return dcc.Graph(figure=fig)

@callback(
    Output("dd-boxplot-4", "children"),
    Input("select_simulado", 'value'),
    Input("select_disciplina", 'value'),
)
def updateScatter1(value, disciplina):
    students = database.getSimulado(value) 
    fig = pg.scatterNotas(students, disciplina=disciplina)
    return dcc.Graph(figure=fig)

@callback(
    Output("dd-table-5", "children"),
    Input("select_simulado", 'value'),
    Input("select_disciplina", 'value'),
)
def createTable(value, disciplina):
    students = database.getSimulado(value) 
    fig = pg.getTable(students, disciplina=disciplina)
    return dcc.Graph(figure=fig)

@callback(
    Output("dd-bar-1", "children"),
    Input("select_students", "value"),
)
def createTable(value):
    print(value)
    cpf = students[value]
    print(cpf)
    student = database.findStudent(cpf)
    fig = pg.compareSimulates(student, database)
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run(debug=True)