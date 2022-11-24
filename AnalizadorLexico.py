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
        
    def agregarToken(self,tipo,token):
        self.tokens.append(Token(tipo,token,self.linea,self.columna))
        self.i -= 1

    def verErrores(self):
        print('\nERRORES')
        for i in self.errores:
            print(i.caracter,i.linea,i.columna)

    def verTokens(self):
        print('\nTOKENS')
        for i in self.tokens:
            print(i.buffer,i.tipo,i.linea,i.columna)