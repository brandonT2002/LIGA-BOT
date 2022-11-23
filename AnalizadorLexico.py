from Token import Token
from Error import Error

class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.linea = 1
        self.columna = 1
        self.estado = 0
        self.buffer = ''

    def agregarError(self,caracter):
        self.errores.append(Error(f'Caracter sin reconocer: {caracter}',self.linea,self.columna))
        