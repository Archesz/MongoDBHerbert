import json

from Database import Database
from Estudante import Estudante
from simulados import simulados
import utils
import validate as pv

with open('alunos_atualizados.json', 'r', encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

def recadastrar(dados, database):
    for i, data in enumerate(dados.values()):
        nome = pv.validar_name(data["nome"])
        cpf = pv.validar_cpf(data["cpf"])
        celular = pv.validar_celular(data["telefone"])
        email = pv.validar_email(data["email"])
        cep = pv.validar_cep(data["cep"])
        numero = data["num_casa"]
        periodo = data["periodo"]
        curso = data["curso"]
        ano = data["ano"]
        nascimento = data["nascimento"]
        etnia = data["etnia"]
        genero = data["genero"]

        if celular == False:
            celular = 11111111111

        if email == False:
            email = "provisorio@gmail.com"
        
        if cep == False:
            cep = "13060492"

        student = Estudante(nome, data["cpf"], celular, email, cep, numero, periodo, curso, ano, nascimento, etnia, genero)
        database.insertStudent(student.__dict__)
        print(f"Adicionado - {nome}")

def atualizarEstudantes():

    # Iniciando o banco de dados
    database = Database()

    for i, data in enumerate(dados.values()):
        try:
            database.updateStudent(data["cpf"], data["Simulados"])
        except:
            database.updateStudent(data["cpf"], {"Colmeias_Inicial": None, "Unicamp_00001": None})
            
def ajustarResposta(resposta_str):
    dict_res = {}
    
    for i in range(0, len(resposta_str)):
        dict_res[i + 1] = resposta_str[i]
    
    print(dict_res)

database = Database()

def addSimulados():
    for simulado in simulados.keys():
        students = database.getSimulado(simulado)
        metricas = utils.getMetricsSimuldo(students)
        simulados[simulado]["Métricas"] = metricas
        database.insertSimulado(simulados[simulado])
        
for simulado in simulados.keys():
    database.updateAllSimulados(simulado)