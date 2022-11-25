from Token import Token
from Error import Error
from prettytable import PrettyTable

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
        x = PrettyTable()
        x.field_names = ['Descripcion','Linea','Columna']
        for error in self.errores:
            x.add_row([error.caracter,error.linea,error.columna])
        print(x)

    def verTokens(self):
        print('\nTOKENS')
        x = PrettyTable()
        x.field_names = ['Token','Tipo','Linea','Columna']
        for i in self.tokens:
            x.add_row([i.buffer,i.tipo,i.linea,i.columna])
        print(x)

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
                self.agregarToken(f'pr_{self.buffer}',self.buffer)
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

    def s6(self):
        self.agregarToken('temporada',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s7(self,caracter):
        if caracter == 'f':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter
        elif caracter == 'j':
            self.estado = 9
            self.columna += 1
            self.buffer += caracter
        elif caracter == 'n':
            self.estado = 12
            self.columna += 1
            self.buffer += caracter
    
    def s8(self):
        self.agregarToken(f'bd_{self.buffer}',self.buffer)
        self.buffer = ''
        self.estado = 0