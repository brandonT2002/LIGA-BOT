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
        elif caracter == '>':
            self.estado = 3
            self.columna += 1
            self.buffer += caracter
        elif caracter == '-':
            self.estado = 4
            self.columna += 1
            self.buffer += caracter
        elif caracter == '"':
            self.estado = 10
            self.columna += 1
            self.buffer += caracter
        elif caracter.isdigit():
            print('entra1')
            self.estado = 13
            self.columna += 1
            self.buffer += caracter
        elif caracter in [' ']:
            self.columna += 1
        elif caracter == '\n':
            self.linea += 1
            self.columna += 1
        elif caracter == '#':
            pass
        else:
            self.agregarError(caracter)
            self.estado = 0
            self.columna += 1
            self.buffer += ''

    def s1(self,caracter):
        if caracter.isalpha() or caracter.isdigit():
            self.estado == 1
            self.columna += 1
            self.buffer += caracter
        else:
            if self.buffer in ['RESULTADO','VS','TEMPORADA','JORNADA','LOCAL','VISITANTE','TOTAL','GOLES','TABLA','PARTIDOS','TOP','SUPERIOR','INFERIOR']:
                self.agregarToken(f'PR_{self.buffer}',self.buffer)
                self.buffer = ''
                self.estado = 0
            else:
                self.agregarToken('cadena',self.buffer)
                self.buffer = ''
                self.estado = 0

    def s2(self):
        self.agregarToken('menor_que',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s3(self):
        self.agregarToken('mayor_que',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s4(self,caracter):
        if caracter == 'f':
            self.estado = 5
            self.columna += 1
            self.buffer += caracter
        elif caracter == 'j':
            self.estado = 6
            self.columna += 1
            self.buffer += caracter
        elif caracter == 'n':
            self.estado = 9
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarToken('guion',self.buffer)
            self.buffer = ''
            self.estado = 0

    def s5(self):
        self.agregarToken(f'bd_{self.buffer}'.replace('-',''),self.buffer)
        self.buffer = ''
        self.estado = 0
        
    def s6(self,caracter):
        if caracter == 'i':
            self.estado = 7
            self.columna += 1
            self.buffer += caracter
        elif caracter == 'f':
            self.estado = 8
            self.columna += 1
            self.buffer += caracter

    def s7(self):
        self.agregarToken(f'bd_{self.buffer}'.replace('-',''),self.buffer)
        self.buffer = ''
        self.estado = 0

    def s8(self):
        self.agregarToken(f'bd_{self.buffer}'.replace('-',''),self.buffer)
        self.buffer = ''
        self.estado = 0

    def s9(self):
        self.agregarToken(f'bd_{self.buffer}'.replace('-',''),self.buffer)
        self.buffer = ''
        self.estado = 0

    def s10(self,caracter):
        if caracter.isalpha() or caracter == ' ':
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        elif caracter == '"':
            self.estado = 12
            self.columna += 1
            self.buffer += caracter

    def s11(self,caracter):
        if caracter.isalpha() or caracter == ' ':
            self.estado = 11
            self.columna += 1
            self.buffer += caracter
        elif caracter == '"':
            self.estado = 12
            self.columna += 1
            self.buffer += caracter

    def s12(self):
        self.agregarToken('equipo',self.buffer)
        self.buffer = ''
        self.estado = 0

    def s13(self,caracter):
        if caracter.isdigit():
            self.estado = 13
            self.columna += 1
            self.buffer += caracter
        else:
            self.agregarToken('numero',self.buffer)
            self.buffer = ''
            self.estado = 0

    def analizar(self,cadena):
        print('Analizando...')
        cadena += '#'
        self.i = 0
        while(self.i < len(cadena)):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2()
            elif self.estado == 3:
                self.s3()
            elif self.estado == 4:
                self.s4(cadena[self.i])
            elif self.estado == 5:
                self.s5()
            elif self.estado == 6:
                self.s6(cadena[self.i])
            elif self.estado == 7:
                self.s7()
            elif self.estado == 8:
                self.s8()
            elif self.estado == 9:
                self.s9()
            elif self.estado == 10:
                self.s10(cadena[self.i])
            elif self.estado == 11:
                self.s11(cadena[self.i])
            elif self.estado == 12:
                self.s12()
            elif self.estado == 13:
                self.s13(cadena[self.i])
            self.i += 1