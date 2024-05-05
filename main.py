import json

from Database import Database
from Estudante import Estudante

import validate as pv

with open('alunos_atualizados.json', 'r', encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Iniciando o banco de dados
database = Database()
students = []

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

    if cpf == False:
        cpf = 00000000000

    if celular == False:
        celular = 11111111111

    if email == False:
        email = "provisorio@gmail.com"
    
    if cep == False:
        cep = "13060492"

    student = Estudante(nome, cpf, celular, email, cep, numero, periodo, curso, ano, nascimento, etnia, genero)
    database.insertStudent(student.__dict__)
    print(f"Adicionado - {nome}")
    #students.append(student.__dict__)

#database.insertStudents(students)