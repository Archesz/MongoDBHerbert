from Database import Database
import graphs as pg

simulados = ["Colmeias_Inicial", "Unicamp_00001", "USP_00001"]
simulado = simulados[2]

database = Database()
resultados_unicamp = database.getSimulado("Unicamp_00001")
resultados_usp = database.getSimulado("USP_00001")

# pg.compareSimulados(resultados_unicamp, resultados_usp)

# pg.viewStudent("47180957860", [resultados_unicamp, resultados_usp])