from Fachascript_Indentado_Lexer import Lexer, palabras_clave

# Clase Linter
class Linter:
    def __init__(self, codigo):
        self.codigo = codigo
        self.lexer = Lexer(codigo)
        self.tokens = self.lexer.tokenizar()
        self.errores = []
        self.variables_definidas = set()

    def lint(self):
        self.verificar_tokens_no_definidos()
        self.verificar_uso_correcto_de_variables()
        self.mostrar_errores()

    def verificar_tokens_no_definidos(self):
        for token in self.tokens:
            if token[0] == 'IDENTIFICADOR' and token[1] not in self.variables_definidas:
                if token[1] not in palabras_clave:
                    self.errores.append(f"Error: Identificador no definido '{token[1]}' en la línea {self.lexer.linea_actual}.")

    def verificar_uso_correcto_de_variables(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]
            if token[0] == 'PALABRA_CLAVE' and token[1] == 'Variable':
                if i + 1 < len(self.tokens) and self.tokens[i + 1][0] == 'IDENTIFICADOR':
                    self.variables_definidas.add(self.tokens[i + 1][1])
                    i += 2  # Saltar 'Variable' y el identificador
                else:
                    self.errores.append(f"Error: Se esperaba un identificador después de 'Variable' en la línea {self.lexer.linea_actual}.")
                    i += 1
            else:
                i += 1

    def mostrar_errores(self):
        if not self.errores:
            print("No se encontraron errores.")
        else:
            for error in self.errores:
                print(error)

# Ejemplo de uso del linter
if __name__ == "__main__":
    codigo = '''
    Variable a = 10
    Variable b = 20
    imprimir(sumar(a, b))
    '''
    linter = Linter(codigo)
    linter.lint()