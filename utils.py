from simulados import simulados
import numpy as np
from statistics import mode

def converter_respostas(resposta_aluno):
    respostas_dict = {}
    for i, resposta in enumerate(resposta_aluno, start=1):
        respostas_dict[str(i)] = resposta

    return respostas_dict

def calcularMetricas(gabarito_student, codigo, flag=0, simulados=simulados):
    gabarito_oficial = simulados[codigo]["Gabarito"]

    if flag == 0:
        gabarito_student = converter_respostas(gabarito_student)

    simulado = {
        "Acertos": {"Total": 0, "Português": 0, "Literatura": 0, "Matemática": 0, "Física": 0, "Química": 0, "Biologia": 0, "História": 0, "Geografia": 0, "Filosofia": 0, "Sociologia": 0, "Inglês": 0},
        "Score": {"Total": 0, "Português": 0, "Literatura": 0, "Matemática": 0, "Física": 0, "Química": 0, "Biologia": 0, "História": 0, "Geografia": 0, "Filosofia": 0, "Sociologia": 0, "Inglês": 0},
        "Gabarito": gabarito_student,
        "Erros": []
    }
    
    for i in gabarito_oficial.keys():
        if gabarito_oficial[i]["Resposta"] == gabarito_student[i]:
            simulado["Acertos"][gabarito_oficial[i]["Disciplina"]] += 1
            simulado["Acertos"]["Total"] += 1
        else:
            simulado["Erros"].extend(gabarito_oficial[i]["Conteudo"])

    for disciplina in simulado["Acertos"].keys():
        acertos = simulado["Acertos"][disciplina]
        try:
            score = round(acertos / simulados[codigo]["Questões"][disciplina], 2)
        except:
            score = 0
        simulado["Score"][disciplina] = score

    return simulado

def removeDuplicates(lista):
    lista_2 = []
    for disc in lista:
        if disc not in lista_2:
            lista_2.append(disc)
    
    return lista_2

def getMetricsSimuldo(students):
    metricas = {}
    x = list(students.keys())[0]
    disciplinas = students[x]["simulado"]["Acertos"].keys()
    
    for disciplina in disciplinas:
        metricas[disciplina] = {}
    
    for disciplina in metricas.keys():
        acertos = []
        
        for student in students:
            acertos_student = students[student]["simulado"]["Acertos"][disciplina]
            acertos.append(acertos_student)

        acertos_np = np.array(acertos)            
        metricas[disciplina]["Maxima"] = int(np.max(acertos_np))
        metricas[disciplina]["Media"] = round(float(np.mean(acertos_np)), 2)
        metricas[disciplina]["Moda"] = int(mode(acertos))
        metricas[disciplina]["Mediana"] = float(np.median(acertos_np))
        metricas[disciplina]["Minimo"] = float(np.min(acertos_np))
        metricas[disciplina]["DesvioPadrao"] = float(np.std(acertos_np))
        metricas[disciplina]["Variancia"] = float(np.var(acertos_np))
        metricas[disciplina]["Percentis"] = list(np.percentile(acertos_np, [25, 50, 75]))
        metricas[disciplina]["Amplitude"] = int(np.ptp(acertos_np))
        metricas[disciplina]["IQR"] = float(np.percentile(acertos_np, 75) - np.percentile(acertos_np, 25))

    return metricas