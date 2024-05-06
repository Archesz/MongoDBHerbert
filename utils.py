from simulados import simulados

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
        "Gabarito": gabarito_student,
        "Erros": []
    }
    
    for i in gabarito_oficial.keys():
        if gabarito_oficial[i]["Resposta"] == gabarito_student[i]:
            simulado["Acertos"][gabarito_oficial[i]["Disciplina"]] += 1
            simulado["Acertos"]["Total"] += 1
        else:
            simulado["Erros"].extend(gabarito_oficial[i]["Conteudo"])
            
    return simulado