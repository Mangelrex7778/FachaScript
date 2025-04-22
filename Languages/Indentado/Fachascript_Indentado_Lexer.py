# -*- coding: utf-8 -*-
import re

# Palabras clave del lenguaje Fachascript
palabras_clave = {
    'imprimir', 'crear', 'asignar', 'sumar', 'restar', 'multiplicar', 'dividir', 'potencia', 'si', 'no',
    'Variable', 'constante', 'entero', 'decimal', 'booleano', 'cadena', 'carácter', 'arreglo',
    'diccionario', 'nulo', 'raiz', 'redondear', 'promedio', 'aleatorio', 'factorial',
    'modulo', 'suma_decimal', 'resta_decimal', 'mult_decimal', 'divi_decimal', 'mayusculas',
    'minusculas', 'reemplazar', 'concatenar', 'subcadena', 'convertir_a_entero',
    'convertir_a_decimal', 'convertir_a_cadena', 'convertir_a_booleano', 'tipo_de_dato',
    'lista', 'agregar', 'remover', 'longitud', 'invertir', 'ordenar', 'mezclar', 'copiar',
    'vaciar', 'abrir_archivo', 'leer_archivo', 'escribir_archivo', 'cerrar_archivo', 'esperar',
    'temporizador', 'fecha_actual', 'hora_actual', 'hoy', 'ahora', 'zona_horaria', 'Interfaz',
    'Ventana', 'Dimensiones', 'Nombre_Ventana', 'Texto', 'Boton',
    'usuario', 'sistema', 'memoria_libre', 'cpu', 'lista_procesos', 'red_ip',
    'facha_sistema', 'facha_ruta_script', 'facha_lenguaje', 'modo_terminal',
    'limpiar', 'retroceder', 'cerrar', 'binario', 'datos', 'funcion', 'comparar', 'leer_entrada',
    'parsear_json', 'encadenar_json', 'parsear_entero', 'medicion', 'altura', 'longitud', 'Negrita', 'Cursiva', 'Sombreado', 'Tachado',
    'Rojo', 'Verde', 'Azul', 'Amarillo', 'Cian', 'Magenta', 'Blanco', 'Negro', 'Gris', 'Marrón', 'Naranja', 'Rosa', 'Violeta', 'SegoeLight', 'Frutiger', 'SegoeUI', 'Consola', 'SegoeUIC', 'SegoeUIN', 'SegoeLightC', 'SegoeUIN', 'FrutigerC', 'FrutigerN', 'ConsolaC', 'ConsolaN', 'Barra_De_Progreso', 'Tiempo_De_Barra', 'Efecto_De_Barra', 'Detener_Audio', 'Volumen_Audio'
}

# Tipos de tokens del lenguaje Fachascript
tokens = [
    'ESPACIOS', 'IDENTIFICADOR', 'NUMERO', 'OPERADOR', 'SIMBOLO',
    'CADENA', 'NUEVA_LINEA'
]

# Expresiones regulares para los tokens
regex_tokens = {
    'ESPACIOS': r'\s+',
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'NUMERO': r'\d+(\.\d+)?',
    'OPERADOR': r'[\+\-\*/=<>!]+',
    'SIMBOLO': r'[\(\)\[\]\{\},;:]',
    'CADENA': r'\".*?\"',
    'NUEVA_LINEA': r'\n',
    'COMENTARIO': r'#.*'
}

# Clase Lexer
class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.posicion = 0
        self.linea_actual = 1

    def obtener_token(self):
        if self.posicion >= len(self.codigo):
            return None

        for token, regex in regex_tokens.items():
            patron = re.compile(regex)
            coincidencia = patron.match(self.codigo, self.posicion)
            if coincidencia:
                valor = coincidencia.group(0)
                self.posicion = coincidencia.end(0)
                if token == 'ESPACIOS' or token == 'COMENTARIO':
                    continue
                elif token == 'NUEVA_LINEA':
                    self.linea_actual += 1
                    return (token, valor)
                elif token == 'IDENTIFICADOR' and valor in palabras_clave:
                    return ('PALABRA_CLAVE', valor)
                elif token == 'CADENA':
                    # Remover las comillas de las cadenas
                    valor = valor.strip('"')
                    return (token, valor)
                else:
                    return (token, valor)
        return None

    def tokenizar(self):
        tokens = []
        while self.posicion < len(self.codigo):
            try:
                token = self.obtener_token()
                if token:
                    tokens.append(token)
            except Exception as e:
                print(e)
                self.posicion += 1  # Avanza para evitar bucles infinitos
        return tokens