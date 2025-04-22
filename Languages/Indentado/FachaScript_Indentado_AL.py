import math
import random
import time
from datetime import datetime
from collections import deque
import tkinter as tk
from tkinter import ttk, PhotoImage, font
import winsound
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import sys
import os


def imprimir(*args):
    # Imprimir cada argumento sin comillas
    print(*args)

def crear(variable, valor):
    globals()[variable] = valor

def asignar(variable, valor):
    globals()[variable] = valor

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def Si():
    return True

def No():
    return False

# Variables y estructuras de datos
Variable = lambda nombre, valor: globals().update({nombre: valor})
constante = lambda nombre, valor: globals().update({nombre: valor})
entero = int
decimal = float
booleano = bool
cadena = str
carácter = lambda x: x[0] if isinstance(x, str) and len(x) == 1 else None
arreglo = list
diccionario = dict
nulo = None

def potencia(a):
    return a ** 2

def raiz(a):
    if a < 0:
        return "Error: Raíz de un número negativo"
    return a ** 0.5

def redondear(a, b=None):
    if b is None:
        return round(a)
    return round(a) + round(b)

def promedio(*args):
    if len(args) < 2:
        return "Error: Se necesitan al menos dos argumentos"
    return sum(args) / len(args)

def aleatorio(a=None, b=None):
    if a is None and b is None:
        return random.randint(0, 1_000_000)  # Genera un número entero aleatorio entre 0 y 1,000,000
    elif a is not None and b is not None:
        return random.randint(a, b)  # Genera un número entero aleatorio en el rango [a, b]
    else:
        return "Error: Ambos argumentos deben ser proporcionados o ninguno"

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: El argumento debe ser un entero no negativo"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def modulo(a, b):
    if a is None or b is None:
        print("Advertencia: modulo() recibió un argumento None")
        return None
    return a % b

def suma_decimal(a, b):
    return float(a) + float(b)

def resta_decimal(a, b):
    return float(a) - float(b)

def mult_decimal(a, b):
    return float(a) * float(b)

def divi_decimal(a, b):
    if b == 0:
        return "Error: División por cero"
    return float(a) / float(b)

# Manejo de cadenas
def mayusculas(cadena):
    if cadena is None:
        print("Advertencia: mayusculas() recibió un argumento None")
        return None
    return cadena.upper()

def minusculas(cadena):
    if cadena is None:
        print("Advertencia: minusculas() recibió un argumento None")
        return None
    return cadena.lower()

def reemplazar(cadena, viejo, nuevo):
    if cadena is None or viejo is None or nuevo is None:
        print("Advertencia: reemplazar() recibió un argumento None")
        return None
    return cadena.replace(viejo, nuevo)

def concatenar(*cadenas):
    cadenas_validas = [c for c in cadenas if c is not None]
    print("Advertencia: concatenar() recibió un argumento None")
    return ''.join(cadenas_validas)

def subcadena(cadena, inicio, fin=None):
    if cadena is None or inicio is None:
        print("Advertencia: subcadena() recibió un argumento None")
        return None
    if fin is None:
        return cadena[inicio:]
    else:
        return cadena[inicio:fin]

def convertir_a_entero(cadena):
    if cadena is None:
        print("Advertencia: convertir_a_entero() recibió un argumento None")
        return None
    return int(cadena)

def convertir_a_decimal(cadena):
    if cadena is None:
        print("Advertencia: convertir_a_decimal() recibió un argumento None")
        return None
    return float(cadena)

def convertir_a_cadena(valor):
    if valor is None:
        print("Advertencia: convertir_a_cadena() recibió un argumento None")
        return "None"
    return str(valor)

def convertir_a_booleano(cadena):
    if cadena is None:
        print("Advertencia: convertir_a_booleano() recibió un argumento None")
        return None
    return cadena.lower() in ['true', '1', 'yes']

def tipo_de_dato(valor):
    if valor is None:
        print("Advertencia: tipo_de_dato() recibió un argumento None")
        return "NoneType"
    return type(valor).__name__

# Manejo de listas y diccionarios
lista = list

def agregar(lista, elemento):
    if lista is not None:
        lista.append(elemento)
    else:
        print("Advertencia: agregar() recibió una lista None")

def remover(lista, elemento):
    if lista is not None and elemento in lista:
        lista.remove(elemento)
    else:
        print("Advertencia: remover() recibió una lista None o el elemento no está en la lista")

def longitud(coleccion):
    if coleccion is None:
        print("Advertencia: longitud() recibió una colección None")
        return 0
    return len(coleccion)

def invertir(lista):
    if lista is not None:
        lista.reverse()
    else:
        print("Advertencia: invertir() recibió una lista None")

def ordenar(lista):
    if lista is not None:
        lista.sort()
    else:
        print("Advertencia: ordenar() recibió una lista None")

def mezclar(lista):
    if lista is not None:
        random.shuffle(lista)
    else:
        print("Advertencia: mezclar() recibió una lista None")

def copiar(coleccion):
    if coleccion is None:
        print("Advertencia: copiar() recibió una colección None")
        return None
    return coleccion.copy()

def vaciar(coleccion):
    if coleccion is not None:
        coleccion.clear()
    else:
        print("Advertencia: vaciar() recibió una colección None")

# Manipulación de archivos
def abrir_archivo(ruta, modo):
    if ruta is None or modo is None:
        print("Advertencia: abrir_archivo() recibió un argumento None")
        return None
    return open(ruta, modo)

def leer_archivo(archivo):
    if archivo is None:
        print("Advertencia: leer_archivo() recibió un archivo None")
        return None
    return archivo.read()

def escribir_archivo(archivo, contenido):
    if archivo is None or contenido is None:
        print("Advertencia: escribir_archivo() recibió un argumento None")
        return None
    return archivo.write(contenido)

def cerrar_archivo(archivo):
    if archivo is not None:
        archivo.close()
    else:
        print("Advertencia: cerrar_archivo() recibió un archivo None")

# Tiempo y fechas
def esperar(segundos):
    if segundos is not None:
        time.sleep(segundos)
    else:
        print("Advertencia: esperar() recibió un argumento None")

def temporizador(funcion, segundos):
    if segundos is not None and funcion is not None:
        time.sleep(segundos)
        return funcion()
    else:
        print("Advertencia: temporizador() recibió un argumento None")
    return None

def fecha_actual():
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d")

def hora_actual():
    ahora = datetime.now()
    return ahora.strftime("%H:%M:%S")

def hoy():
    return datetime.today()

def ahora():
    return datetime.now()

def zona_horaria():
    return datetime.now().astimezone().tzinfo

# Definición de colores
colores_definidos = {
    "Rojo": "red",
    "Verde": "green",
    "Azul": "blue",
    "Amarillo": "yellow",
    "Cian": "cyan",
    "Magenta": "magenta",
    "Blanco": "white",
    "Negro": "black",
    "Gris": "gray",
    "Marrón": "brown",
    "Naranja": "orange",
    "Rosa": "pink",
    "Violeta": "violet",
    "Sombra": "#808080"  # Agregamos un color para la sombra
}

# Definición de estilos de fuente
estilos_fuente = {
    "Cursiva": "italic",
    "Negrita": "bold"
}

Si = True
No = False

# Variable global para el efecto de barra (Normal o Segmentada)
efecto_barra_global = "Normal"

# Variables globales para audio usando pydub
current_audio_segment = None
current_playback = None

# Clase Ventana
class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Programa de FachaScript")
        try:
            self.root.iconbitmap("FCHW.ico")
        except Exception as e:
            print(f"Error loading icon: {e}")
        self.root.geometry("800x600")
        self.style = ttk.Style()
        self.tiempo_de_barra = ""
        # No se crean estilos fijos; se generarán de forma dinámica

    def agregar_texto(self, texto, orientacion, tamano, color, efecto=None):
        x, y = orientacion
        color_tk = colores_definidos.get(color, "black")
        font_weight = estilos_fuente.get(efecto, "normal") if efecto else "normal"
        fuente = ("Arial", tamano, font_weight)
        label = tk.Label(self.root, text=texto, font=fuente, fg=color_tk, bg="white")
        label.place(x=x, y=y)

    def agregar_boton(self, texto, orientacion, color, ancho, alto):
        x, y = orientacion
        color_boton = colores_definidos.get(color, "gray")
        color_texto = "white" if color in ["Rojo", "Verde", "Azul", "Magenta", "Marrón", "Naranja", "Violeta", "Negro"] else "black"
        sombra_color = colores_definidos.get("Sombra", "#808080")
        sombra = tk.Frame(self.root, bg=sombra_color, borderwidth=0, relief="flat")
        sombra.place(x=x + 2, y=y + 2, width=ancho, height=alto)
        boton = tk.Button(self.root, text=texto, bg=color_boton, fg=color_texto,
                          borderwidth=0, relief="flat",
                          command=lambda: print(f"¡Botón '{texto}' presionado!"))
        boton.place(x=x, y=y, width=ancho, height=alto)

    def agregar_barra_de_progreso(self, texto, orientacion, color, ancho, alto, tiempo, orientacion_string="Horizontal"):
        x, y = orientacion
        color_barra = colores_definidos.get(color, "green")
        es_horizontal = orientacion_string.lower() == "horizontal"
        
        # Mostrar el texto primario (por ejemplo, "Cargando archivos...") arriba de la barra
        if texto:
            label_texto = tk.Label(self.root, text=texto, font=("Arial", 10), bg="white", fg="black")
            label_texto.place(x=x, y=y - 20)
        
        # Determinar la orientación de la barra
        orientacion_barra = tk.HORIZONTAL if es_horizontal else tk.VERTICAL
        
        # Generar un nombre de estilo único para esta barra
        style_name = f"Custom.{orientacion_string}.{color}.{x}.{y}.TProgressbar"
        self.style.configure(style_name, background=color_barra, troughcolor="white", borderwidth=0)
        
        # Definir el layout según la orientación
        if es_horizontal:
            self.style.layout(style_name,
                              [('Horizontal.TProgressbar.trough',
                                {'children': [('Horizontal.TProgressbar.pbar',
                                               {'side': 'left', 'sticky': 'nswe'})],
                                 'sticky': 'nswe'})])
        else:
            self.style.layout(style_name,
                              [('Vertical.TProgressbar.trough',
                                {'children': [('Vertical.TProgressbar.pbar',
                                               {'side': 'bottom', 'sticky': 'nswe'})],
                                 'sticky': 'nswe'})])
        
        # Aplicar efecto segmentada si está configurado
        if efecto_barra_global.lower() == "segmentada":
            self.style.configure(style_name, relief="sunken", borderwidth=2)
        
        # Crear la barra de progreso
        barra = ttk.Progressbar(self.root, orient=orientacion_barra, length=ancho, mode="determinate", style=style_name)
        barra.place(x=x, y=y, width=ancho, height=alto)
        barra["maximum"] = 100
        
        # Iniciar la animación de la barra
        self.animar_barra(tiempo, x, y, ancho, alto, orientacion_string, barra)

    def animar_barra(self, tiempo, x, y, ancho, alto, orientacion_string, barra):
        tiempo_segundos = self.convertir_tiempo_a_segundos(tiempo)
        tiempo_por_incremento = (tiempo_segundos * 1000) / 100

        # Etiqueta del porcentaje (se muestra el avance en %)
        porcentaje_label = tk.Label(self.root, text="0%", font=("Arial", 10), bg="white", fg="black")
        if orientacion_string.lower() == "horizontal":
            porcentaje_label.place(x=x + ancho + 10, y=y)
        else:
            porcentaje_label.place(x=x, y=y + alto + 5)
            
        def step():
            if barra["value"] < 100:
                barra["value"] += 1
                porcentaje_label.config(text=f"{int(barra['value'])}%")
                self.root.after(int(tiempo_por_incremento), step)
            else:
                porcentaje_label.destroy()
        barra["value"] = 0
        step()

    def convertir_tiempo_a_segundos(self, tiempo):
        if "Minutos" in tiempo:
            valor = float(tiempo.replace("Minutos", "").strip())
            return valor * 60
        elif "Segundos" in tiempo:
            return float(tiempo.replace("Segundos", "").strip())
        elif "Milisegundos" in tiempo:
            return float(tiempo.replace("Milisegundos", "").strip()) / 1000
        elif "Hora" in tiempo:
            valor = float(tiempo.replace("Hora", "").strip())
            return valor * 3600
        elif "Dia" in tiempo:
            valor = float(tiempo.replace("Dia", "").strip())
            return valor * 86400
        else:
            return 60

    def asignar_tiempo(self, tiempo):
        self.tiempo_de_barra = tiempo
        print(f"Tiempo para la barra: {tiempo}")

    def asignar_efecto_barra(self, efecto):
        global efecto_barra_global
        efecto = efecto.capitalize()
        if efecto in ["Normal", "Segmentada"]:
            efecto_barra_global = efecto
            print(f"Efecto de barra establecido en: {efecto}")
        else:
            print("Efecto inválido. Usando 'Normal'.")
            efecto_barra_global = "Normal"

    def mostrar(self):
        self.root.deiconify()
        self.root.update()
        self.root.lift()

    def mainloop(self):
        self.root.mainloop()

    def ocultar(self):
        self.root.withdraw()

# Funciones globales para el intérprete de FachaScript
ventana = Ventana()

def Nombre_Ventana(nombre):
    ventana.root.title(nombre)

def Dimensiones(dim):
    ventana.root.geometry(dim)

def Interfaz(valor):
    if valor == Si:
        ventana.mostrar()
    else:
        ventana.ocultar()

def Texto(texto, orientacion, tamano, color, efecto=""):
    ventana.agregar_texto(texto, orientacion, tamano, color, efecto)

def Boton(texto, orientacion, color, ancho, alto):
    ventana.agregar_boton(texto, orientacion, color, ancho, alto)

def Ventana(valor):
    if valor == Si:
        ventana.mostrar()
    else:
        ventana.ocultar()

def Barra_De_Progreso(texto, orientacion, color, ancho, alto, tiempo, orientacion_string="Horizontal"):
    ventana.agregar_barra_de_progreso(texto, orientacion, color, ancho, alto, tiempo, orientacion_string)

def Tiempo_De_Barra(tiempo):
    ventana.asignar_tiempo(tiempo)

def Efecto_De_Barra(efecto="Normal"):
    ventana.asignar_efecto_barra(efecto)

def mainloop():
    ventana.mainloop()

# ===================== NUEVAS FUNCIONES DE AUDIO CON PYDUB =====================
# Variables globales para audio
current_audio_segment = None
current_playback = None

def Audio(ruta):
    """
    Reproduce el audio en la ruta especificada.
    Soporta múltiples formatos (MP3, OGG, WAV, etc.) siempre que ffmpeg esté instalado.
    """
    global current_audio_segment, current_playback
    try:
        # Extraer la extensión y usarla como formato
        _, ext = os.path.splitext(ruta)
        formato = ext[1:].lower()  # Quita el punto y convierte a minúsculas
        current_audio_segment = AudioSegment.from_file(ruta, format=formato)
        current_playback = _play_with_simpleaudio(current_audio_segment)
        print(f"Reproduciendo audio: {ruta}")
    except Exception as e:
        print(f"Error al reproducir audio: {e}")

def Detener_Audio(tiempo):
    """
    Espera el tiempo especificado y detiene el audio actual.
    Ejemplos: "5 Segundos", "1 Minutos", "500 Milisegundos".
    """
    global current_playback
    try:
        segundos = 0
        if "Minutos" in tiempo:
            segundos = float(tiempo.replace("Minutos", "").strip()) * 60
        elif "Milisegundos" in tiempo:
            segundos = float(tiempo.replace("Milisegundos", "").strip()) / 1000
        elif "Segundos" in tiempo:
            segundos = float(tiempo.replace("Segundos", "").strip())
        else:
            segundos = float(tiempo.strip())
        print(f"Esperando {segundos} segundos para detener el audio...")
        time.sleep(segundos)
        if current_playback:
            current_playback.stop()
            print("Audio detenido.")
    except Exception as e:
        print(f"Error al detener audio: {e}")

def Volumen_Audio(decibeles):
    """
    Ajusta el volumen del audio actual.
    Se espera un valor numérico (porcentaje de 0 a 100).
    Debido a que la reproducción es asíncrona, se recomienda esperar un instante
    después de llamar a Audio() antes de ajustar el volumen.
    """
    global current_audio_segment, current_playback
    try:
        vol = float(decibeles)
        gain = 20 * math.log10(vol / 100.0)
        if current_audio_segment:
            new_audio = current_audio_segment.apply_gain(gain)
            if current_playback:
                current_playback.stop()
            current_playback = _play_with_simpleaudio(new_audio)
            print(f"Volumen ajustado a: {vol}%")
        else:
            print("No hay audio reproduciéndose para ajustar el volumen.")
    except Exception as e:
        print(f"Error al ajustar volumen: {e}")