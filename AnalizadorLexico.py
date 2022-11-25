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

    def s0(self,caracter):
        if caracter.isalpha():
            self.estado = 1
            self.columna += 1
            self.buffer += caracter
        elif caracter == '<':
            self.estado = 2
            self.columna += 1
            self.buffer += caracter
        elif caracter == '-':
            self.estado = 7
            self.columna += 1
            self.buffer += caracter
        elif caracter.isdigit():
            self.estado == 13
            self.columna += 1
            self.buffer += caracter
        elif caracter == ' ':
            self.columna += 1
        elif caracter == '[':
            self.columna += 1
        elif caracter == ']':
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna += 1
        elif caracter  == '#':
            pass
        else:
            self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer += ''

    def s1(self,caracter):
        if caracter.isalpha():
            self.estado = 1
            self.columna += 1
            self.buffer += caracter
        else:
            if self.buffer in ['RESULTADO','VS','TEMPORADA','JORNADA','LOCAL','VISITANTE','TOTAL']:
                self.agregarToken(f'pr-{self.buffer}',self.buffer)
                self.buffer = ''
                self.estado = 0
            else:
                self.agregarError(self.buffer)
                self.buffer += ''
                self.estado = 0

    def s2(self,caracter):
        if caracter.isdigit():
            self.estado = 3
            self.columna += 1
            self.buffer += caracter

    def s3(self,caracter):
        if caracter.isdigit():
            self.estado = 3
            self.columna += 1
            self.buffer += caracter
        elif caracter == '-':
            self.estado = 4
            self.columna += 1
            self.buffer += caracter

    def s4(self,caracter):
        if caracter.isdigit():
            self.estado = 5
            self.columna += 1
            self.buffer += caracter

    def s5(self,caracter):
        if caracter.isdigit():
            self.estado = 5
            self.columna += 1
            self.buffer += caracter
        elif caracter == '>':
            self.estado = 6
            self.columna += 1
            self.buffer += caracter