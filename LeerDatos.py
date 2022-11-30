from Encuentro import Encuentro

class Controlador:
    def __init__(self):
        self.encuentros = []

    def leerArchivo(self):
        ruta = 'LaLigaBot-LFP.csv'
        encuentros = open(ruta,encoding='utf-8').read().split('\n')
        for encuentro in encuentros:
            encuentro = encuentro.split(',')
            self.encuentros.append(Encuentro(encuentro[0],encuentro[1],encuentro[2],encuentro[3],encuentro[4],encuentro[5]))

    def mostrar(self):
        for encuentro in self.encuentros:
            print(encuentro.fecha,encuentro.temporada,encuentro.equipo1,encuentro.equipo2,encuentro.goles1,encuentro.goles2)

control = Controlador()
control.leerArchivo()
control.mostrar()