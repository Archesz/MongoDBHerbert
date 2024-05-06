from Database import Database

database = Database()

student = database.findStudent("47180957860")
print(student["nome"])
print("-----")

simulados = student["Simulados"].keys()

for simulado in simulados:
    print(f"{simulado}: {student['Simulados'][simulado]['Acertos']['Total']} Acertos.")