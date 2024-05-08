from pymongo import MongoClient
import utils

uri = "mongodb+srv://Arches:Giovana12@herbert.vp2ett8.mongodb.net/"

class Database():
    
    def __init__(self, uri=uri):
        self.uri = uri
        self.start()
        self.database = self.client.get_database("Herbert")

    def start(self):
        try:
            self.client = MongoClient(self.uri)
        except Exception as e:
            raise Exception("Erro ao iniciar o banco de dados")

    def insertStudent(self, student):
        try:
            collection = self.database.get_collection("Alunos")
            collection.insert_one(student)
        except Exception as e:
            raise Exception("Erro ao adicionar o estudante.")
    
    def insertStudents(self, students):
        try:
            collection = self.database.get_collection("Alunos")
            collection.insert_many(students)
        except Exception as e:
            raise Exception("Erro ao adicionar os estudantes.")
        
    def updateStudent(self, cpf, value):
        query_filter = {"cpf": cpf}
        update_operation = {"$set": 
                            {"Simulados": value}
                            }
        collection = self.database.get_collection("Alunos")
        collection.update_one(query_filter, update_operation)    
        print(f"Alterado - {cpf}.")

    def removeDuplicateStudents(self):
        try:
            collection = self.database.get_collection("Alunos")
            pipeline = [
                {"$match": {"cpf": {"$ne": False}}},
                {"$group": {"_id": "$cpf", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
                {"$match": {"count": {"$gt": 1}}}
            ]
            duplicates = list(collection.aggregate(pipeline))
            for duplicate in duplicates:
                del duplicate['unique_ids'][0]
                collection.delete_many({"_id": {"$in": duplicate['unique_ids']}})
        except Exception as e:
            print("Erro:", e)
            
    def insertSimuladoStudent(self, cpf, nome, respostas):
        simulado = utils.calcularMetricas(respostas, nome)
        
        try:
            query_filter = {"cpf": cpf}
            update_operation = {"$set": 
                                {f"Simulados.{nome}": simulado}
                            }
            collection = self.database.get_collection("Alunos")
            collection.update_one(query_filter, update_operation)  
        except:
            print("Erro")
            
    def updateAllSimulados(self, nome):
        try:
            collection = self.database.get_collection("Alunos")
            alunos = collection.find()
            
            for aluno in alunos:
                simulados = aluno.get("Simulados", {})
                if nome in simulados:
                    respostas = aluno["Simulados"][nome]["Gabarito"]
                    simulado_atualizado = utils.calcularMetricas(respostas, nome, flag=1)
                    
                    query_filter = {"_id": aluno["_id"]}
                    update_operation = {"$set": {f"Simulados.{nome}": simulado_atualizado}}
                    
                    collection.update_one(query_filter, update_operation)
        except Exception as e:
            print("Erro:", e)
            
    def getSimulado(self, nome_simulado):
        try:
            collection = self.database.get_collection("Alunos")
            alunos_com_simulado = {}
            
            # Iterar sobre os alunos e verificar se possuem o simulado
            alunos = collection.find({"Simulados." + nome_simulado: {"$exists": True, "$ne": None}})
            for aluno in alunos:
                simulado = aluno["Simulados"][nome_simulado]
                aluno_com_simulado = {
                    "cpf": aluno["cpf"],
                    "nome": aluno["nome"], 
                    "periodo": aluno["periodo"],
                    "etnia": aluno["etnia"],
                    "genero": aluno["genero"],
                    "simulado": simulado
                }
                
                alunos_com_simulado[aluno["cpf"]] = aluno_com_simulado
            
            return alunos_com_simulado
            
        except Exception as e:
            print("Erro:", e)
    
    def getNomeCpfDict(self):
        try:
            collection = self.database.get_collection("Alunos")
            nome_cpf_dict = {}
            
            # Iterar sobre os alunos e construir o dicionário
            alunos = collection.find({}, {"nome": 1, "cpf": 1})
            for aluno in alunos:
                nome_cpf_dict[aluno["nome"]] = aluno["cpf"]
            
            return nome_cpf_dict
            
        except Exception as e:
            print("Erro:", e)
    
    def findStudent(self, cpf):
        try:
            collection = self.database.get_collection("Alunos")
            student = collection.find_one({"cpf": cpf})
            return student
        except Exception as e:
            print("Erro:", e)
            
    # Funções para a parte de simulados
    def insertSimulado(self, simulado):
        try:
            collection = self.database.get_collection("Simulados")
            collection.insert_one(simulado)
        except Exception as e:
            raise Exception("Erro:", e)
    
    def findSimulado(self, nome):
        try:
            collection = self.database.get_collection("Simulados")
            simulado = collection.find_one({"Nome": nome})
            return simulado
        except Exception as e:
            raise Exception("Erro:", e)

    def updateSimulados(self, simulado):
        nome = simulado["Nome"]
        try:
            collection = self.database.get_collection("Simulados")

            query_filter = {"Nome": nome}
            update_operation = {"$set": simulado}
            collection.update_one(query_filter, update_operation)
            
        except Exception as e:
            print("Erro:", e)
    