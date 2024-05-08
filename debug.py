from disciplinas import disciplinas

assuntos = ["Matemática Básica", "Álgebra", "Geometria", "Estatística"]
n_min = 1,
n_max = 5

class Plano():
    
    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.disciplinas = disciplinas

    def getConteudos(self, assunto, n_min, n_max):
        disciplinas = self.disciplinas
        conteudos = list(disciplinas[assunto].keys())
        disciplinas = disciplinas[assunto]
        lista_estudo = []
        
        for key in conteudos:
            if disciplinas[key]["Nível"] >= n_min and disciplinas[key]["Nível"] <= n_max:
                disciplinas[key]["Nome"] = key
                lista_estudo.append(disciplinas[key])
        
        lista_estudo = sorted(lista_estudo, key=lambda x: x['Nível'])

        return lista_estudo

    def createPlan(self, assuntos, nivel_min, nivel_max):
        plano = []
        
        for assunto in assuntos:
            lista = self.getConteudos(assunto, nivel_min, nivel_max)
            plano.extend(lista)

        self.plano = plano

    def exibirPlano(self):
        checks = []
        
        i = 1
        for cont in self.plano:
            print(f"{i} - {cont['Nome']}")
            if cont["Requisitos"] != []:
                j = 1
                for req in cont["Requisitos"]:
                    if req not in checks:
                        print(f"{i}.{j} - {req}")
                        checks.append(req)                
                        j += 1
            i += 1
            checks.append(cont["Nome"])
            
        

plano = Plano("João Vitor Souza de Alcantara", disciplinas)
plano.createPlan(assuntos, 1, 5)
plano.exibirPlano()     