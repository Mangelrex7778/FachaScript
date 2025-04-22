import sys
from Fachascript_Indentado_Lexer import Lexer
from Fachascript_Indentado_parser import Parser
import FachaScript_Indentado_AL as AL
import FachaScript_Indentado_BL as BL

class Interprete:
    def __init__(self, codigo):
        self.codigo = codigo
        self.lexer = Lexer(codigo)
        self.tokens = self.lexer.tokenizar()
        self.parser = Parser(self.tokens)
        self.ast = self.parser.parsear()
        self.variables = {"Si": AL.Si, "No": AL.No}
        self.abrir_interfaz = False

    def ejecutar(self):
        try:
            self.ejecutar_nodo(self.ast)
            AL.ventana.mainloop()
        except Exception as e:
            print(f"Error: {e}")

    def ejecutar_nodo(self, nodo):
        if nodo is None:
            return None

        if nodo.tipo == "Programa":
            for hijo in nodo.hijos:
                self.ejecutar_nodo(hijo)

        elif nodo.tipo == "Expresion":
            if nodo.valor == "imprimir":
                args = [self.ejecutar_nodo(hijo) for hijo in nodo.hijos]
                print(*args)
            elif nodo.valor == "asignar":
                nombre_variable = nodo.hijos[0].valor
                valor = self.ejecutar_nodo(nodo.hijos[1])
                self.variables[nombre_variable] = valor
            elif nodo.valor == "Ventana":
                valor = self.ejecutar_nodo(nodo.hijos[0])
                if hasattr(AL, "Ventana"):
                    AL.Ventana(valor)
                else:
                    print("Función Ventana no encontrada en AL")
            elif nodo.valor in {"Nombre_Ventana", "Dimensiones", "Interfaz", "Texto", "Boton", 
                                "Barra_De_Progreso", "Tiempo_De_Barra", "Efecto_De_Barra",
                                "Audio", "Detener_Audio", "Volumen_Audio"}:
                args = [self.ejecutar_nodo(hijo) for hijo in nodo.hijos]
                try:
                    if hasattr(AL, nodo.valor):
                        funcion = getattr(AL, nodo.valor)
                        funcion(*args)
                    else:
                        print(f"Función {nodo.valor} no encontrada en AL")
                except Exception as e:
                    print(f"Error al llamar a la función {nodo.valor}: {e}")

        elif nodo.tipo == "Identificador":
            nombre = nodo.valor
            if nombre in self.variables:
                return self.variables[nombre]
            else:
                raise Exception(f"Variable {nombre} no definida.")
        elif nodo.tipo == "Numero":
            return int(nodo.valor) if nodo.valor.isdigit() else float(nodo.valor)
        elif nodo.tipo == "Cadena":
            return str(nodo.valor)
        elif nodo.tipo == "Constante":
            if nodo.valor == "Si":
                return AL.Si
            elif nodo.valor == "No":
                return AL.No
        elif nodo.tipo == "Lista":
            return [self.ejecutar_nodo(hijo) for hijo in nodo.hijos]

        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        if archivo.endswith((".fch", ".facha")):
            try:
                with open(archivo, "r") as f:
                    codigo = f.read()
                    interprete = Interprete(codigo)
                    interprete.ejecutar()
            except FileNotFoundError:
                print(f"Error: File '{archivo}' not found.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Error: Archivo debe tener extensión .fch o .facha")
    else:
        print("No se proporcionó archivo para interpretar.")
