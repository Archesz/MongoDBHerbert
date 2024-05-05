from pymongo import MongoClient

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
#try:
#    database = client.get_database("sample_mflix")
#    movies = database.get_collection("movies")
    # Query for a movie that has the title 'Back to the Future'
    # query = { "title": "The Great Train Robbery" }
    # movie = movies.find_one(query)
    # print(movie)
    # client.close()

# except Exception as e:
#     raise Exception("Erro ao encontar o documento.")