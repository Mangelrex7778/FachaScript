class ASTNode:
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0

    def obtener_token_actual(self):
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        return None

    def avanzar(self):
        self.posicion += 1

    def parsear(self):
        return self.parsear_programa()

    def parsear_programa(self):
        nodo = ASTNode('Programa')
        while self.posicion < len(self.tokens):
            declaracion = self.parsear_declaracion()
            if declaracion:
                nodo.hijos.append(declaracion)
            else:
                self.avanzar()  # Saltar tokens no reconocidos
        return nodo

    def parsear_declaracion(self):
        token_actual = self.obtener_token_actual()
        if token_actual and token_actual[0] == 'PALABRA_CLAVE':
            if token_actual[1] == 'imprimir':
                return self.parsear_imprimir()
            elif token_actual[1] == 'Variable':
                return self.parsear_variable()
            # Se agregan funciones de audio a la lista de funciones soportadas
            elif token_actual[1] in {
                'sumar', 'restar', 'multiplicar', 'dividir', 'potencia', 'raiz',
                'redondear', 'promedio', 'aleatorio', 'factorial', 'suma_decimal',
                'resta_decimal', 'mult_decimal', 'divi_decimal', 'Ventana',
                'Nombre_Ventana', 'Dimensiones', 'Interfaz', 'Texto', "Boton",
                "Barra_De_Progreso", "Tiempo_De_Barra", "Efecto_De_Barra",
                "Audio", "Detener_Audio", "Volumen_Audio"
            }:
                return self.parsear_operacion()
            elif token_actual[1] in {'Si', 'No'}:
                return self.parsear_constante()
        return None

    def parsear_imprimir(self):
        self.avanzar()  # Consumir 'imprimir'
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == '(':
            self.avanzar()  # Consumir '('
            expresiones = []
            while self.obtener_token_actual() and self.obtener_token_actual()[0] != 'SIMBOLO' and self.obtener_token_actual()[1] != ')':
                expresion = self.parsear_expresion()
                if expresion:
                    expresiones.append(expresion)
                if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == ',':
                    self.avanzar()  # Consumir la coma
                else:
                    break  # Salir si no hay coma después de la expresión
            if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == ')':
                self.avanzar()  # Consumir ')'
                return ASTNode('Expresion', 'imprimir', expresiones)
            else:
                print("Error: Se esperaba ')' después de la expresión en imprimir()")
                return None
        else:
            print("Error: Se esperaba '(' después de imprimir")
            return None

    def parsear_variable(self):
        self.avanzar()  # Consumir 'Variable'
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'IDENTIFICADOR':
            nombre_variable = self.obtener_token_actual()[1]
            self.avanzar()  # Consumir el identificador
            if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'OPERADOR' and self.obtener_token_actual()[1] == '=':
                self.avanzar()  # Consumir '='
                expresion = self.parsear_expresion()
                if expresion:  # Verificar si la expresión se parseó correctamente
                    return ASTNode('Expresion', 'asignar', [ASTNode('Identificador', nombre_variable), expresion])
                else:
                    print("Error: Expresión inválida después de '='")
                    return None
            else:
                print("Error: Se esperaba '=' después del nombre de la variable")
                return None
        else:
            print("Error: Se esperaba un identificador después de Variable")
            return None

    def parsear_operacion(self):
        nombre_funcion = self.obtener_token_actual()[1]
        self.avanzar()  # Consumir la palabra clave de la operación
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == '(':
            self.avanzar()  # Consumir '('
            
            argumentos = []  # Lista para almacenar los argumentos
            while self.obtener_token_actual() and self.obtener_token_actual()[1] != ')':
                expresion = self.parsear_expresion()
                if expresion:
                    argumentos.append(expresion)
                
                if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO':
                    if self.obtener_token_actual()[1] == ',':
                        self.avanzar()  # Consumir la coma
                    elif self.obtener_token_actual()[1] == ')':
                        break  # Terminar si encontramos el paréntesis de cierre
                    else:
                        print(f"Error: Se esperaba ',' o ')' después del argumento en {nombre_funcion}")
                        return None
                else:
                    print(f"Error: Se esperaba ',' o ')' después del argumento en {nombre_funcion}")
                    return None
            
            if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == ')':
                self.avanzar()  # Consumir ')'
                return ASTNode('Expresion', nombre_funcion, argumentos)
            else:
                print("Error: Se esperaba ')' en la llamada a la función " + nombre_funcion)
                return None
        else:
            print("Error: Se esperaba '(' en la llamada a la función " + nombre_funcion)
            return None

    def parsear_expresion(self):
        token_actual = self.obtener_token_actual()
        if token_actual:
            if token_actual[0] == 'NUMERO':
                valor = token_actual[1]
                self.avanzar()  # Consumir el número
                return ASTNode('Numero', valor)
            elif token_actual[0] == 'IDENTIFICADOR':
                nombre_variable = token_actual[1]
                self.avanzar()  # Consumir el identificador
                return ASTNode('Identificador', nombre_variable)
            elif token_actual[0] == 'CADENA':
                valor = token_actual[1]
                self.avanzar()  # Consumir la cadena
                return ASTNode('Cadena', valor)
            elif token_actual[0] == 'PALABRA_CLAVE' and token_actual[1] in {
                'sumar', 'restar', 'multiplicar', 'dividir', 'potencia', 'raiz',
                'redondear', 'promedio', 'aleatorio', 'factorial', 'suma_decimal',
                'resta_decimal', 'mult_decimal', 'divi_decimal', 'Ventana',
                'Nombre_Ventana', 'Dimensiones', 'Interfaz', 'Texto', "Boton",
                "Barra_De_Progreso", "Tiempo_De_Barra", "Efecto_De_Barra",
                "Audio", "Detener_Audio", "Volumen_Audio"
            }:
                return self.parsear_operacion()
            elif token_actual[0] == 'PALABRA_CLAVE' and token_actual[1] == 'Si':
                self.avanzar()  # Consumir 'Si'
                return ASTNode('Constante', 'Si')
            elif token_actual[0] == 'PALABRA_CLAVE' and token_actual[1] == 'No':
                self.avanzar()  # Consumir 'No'
                return ASTNode('Constante', 'No')
            elif token_actual[0] == 'SIMBOLO' and token_actual[1] == '[':
                return self.parsear_lista()
        return ASTNode('Constante', 'No')

    def parsear_lista(self):
        self.avanzar()  # Consumir '['
        expresiones = []
        while self.obtener_token_actual() and self.obtener_token_actual()[0] != 'SIMBOLO' and self.obtener_token_actual()[1] != ']':
            expresion = self.parsear_expresion()
            if expresion:
                expresiones.append(expresion)
            if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == ',':
                self.avanzar()  # Consumir la coma
            else:
                break  # Salir si no hay coma después de la expresión
        if self.obtener_token_actual() and self.obtener_token_actual()[0] == 'SIMBOLO' and self.obtener_token_actual()[1] == ']':
            self.avanzar()  # Consumir ']'
        return ASTNode('Lista', None, expresiones)
