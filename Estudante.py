import uuid
import requests
import time

def generate_id():
    length = 6
    hex_digits = uuid.uuid4().hex
    return f"HS{hex_digits[:length]}"

def getEndereco(cep):    
    try:
        url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"
        headers = {'Authorization': 'Token token=fa78fa7dccc395c6c414415bb0ec1fd7'}
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            time.sleep(10)
            return getEndereco(cep)
        elif response.status_code == 403:
            return None
        else:
            data = response.json()
            return data
    
    except Exception as e:
        print("Error:", e)
        return None

def getDesempenho():
    simulados = {}
    score = {'Matemática': 0, "Física": 0, "Química": 0, "Biologia": 0, "Biologia": 0,
             "Geografia": 0, "História": 0, "Sociologia": 0, "Filosofia": 0,
             "Gramática": 0, "Literatura": 0}

    data = {"Simulados": simulados, "Score": score}
    return data
                    

class Estudante():

    def __init__(self, nome, cpf, contato, email, cep, numero, periodo, curso, ano, nascimento, etnia, genero):
        self.id = generate_id()
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.email = email
        self.endereco = getEndereco(cep)
        self.numero = numero
        self.curso = curso
        self.periodo = periodo
        self.ano = ano
        self.nascimento = nascimento
        self.etnia = etnia
        self.genero = genero
        self.desempenho = getDesempenho()
        self.aprovacoes = []
        self.sala = None

    