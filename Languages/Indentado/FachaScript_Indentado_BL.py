import os
import platform
import psutil
import subprocess
import json

# Gestión del sistema y hardware
def usuario():
    try:
        user = os.getenv("USERNAME", "Desconocido")
        print(f"usuario(): {user}")
        return user
    except Exception as e:
        print(f"usuario() - Error: {e}")
        return "Desconocido"

def sistema():
    try:
        system_info = f"{platform.system()} {platform.release()}"
        print(f"sistema(): {system_info}")
        return system_info
    except Exception as e:
        print(f"sistema() - Error: {e}")
        return "Desconocido"

def memoria_libre():
    try:
        mem = psutil.virtual_memory().available
        print(f"memoria_libre(): {mem}")
        return mem
    except Exception as e:
        print(f"memoria_libre() - Error: {e}")
        return 0

def cpu():
    try:
        cpu_info = f"CPU Cores: {os.cpu_count()}"
        print(f"cpu(): {cpu_info}")
        return cpu_info
    except Exception as e:
        print(f"cpu() - Error: {e}")
        return "Desconocido"

def lista_procesos():
    try:
        subprocess.run("tasklist", shell=True)
        print("lista_procesos(): Ejecutado")
    except Exception as e:
        print(f"lista_procesos() - Error: {e}")
        pass

def red_ip():
    try:
        result = subprocess.run('ipconfig | findstr /i "IPv4"', shell=True, capture_output=True, text=True)
        ip = result.stdout.strip() if result.stdout else "No disponible"
        print(f"red_ip(): {ip}")
        return ip
    except Exception as e:
        print(f"red_ip() - Error: {e}")
        return "No disponible"

def facha_sistema():
    sys = sistema()
    print(f"facha_sistema(): {sys}")
    return sys

def facha_ruta_script():
    try:
        path = os.path.abspath(__file__)
        print(f"facha_ruta_script(): {path}")
        return path
    except Exception as e:
        print(f"facha_ruta_script() - Error: {e}")
        return "Desconocido"

def facha_lenguaje():
    print("facha_lenguaje(): Python")
    return "Python"

# Manejo de terminal
def modo_terminal():
    try:
        os.system("cmd")
        print("modo_terminal(): Ejecutado")
    except Exception as e:
        print(f"modo_terminal() - Error: {e}")
        pass

def limpiar():
    try:
        os.system("cls")
        print("limpiar(): Ejecutado")
    except Exception as e:
        print(f"limpiar() - Error: {e}")
        pass

def retroceder():
    print("\b \b", end='', flush=True)

def cerrar():
    exit(0)

# Procesamiento de datos y bajo nivel
def binario(numero):
    if numero is None:
        print("binario() - Error: numero es None")
        return None
    try:
        binary = format(numero, '032b')
        print(f"binario(): {binary}")
        return binary
    except Exception as e:
        print(f"binario() - Error: {e}")
        return None

def datos(size):
    if size is None:
        print("datos() - Error: size es None")
        return None
    try:
        data = bytearray(size)
        print(f"datos(): {data}")
        return data
    except Exception as e:
        print(f"datos() - Error: {e}")
        return None

def funcion(func):
    if func is not None:
        try:
            func()
            print("funcion(): Ejecutado")
        except Exception as e:
            print(f"funcion() - Error: {e}")
    else:
        print("funcion() - Error: func es None")

def comparar(a, b):
    if a is None:
        print("comparar() - Error: a es None")
        return 0
    if b is None:
        print("comparar() - Error: b es None")
        return 0
    if not isinstance(a, (int, float)):
        print(f"comparar() - Error: a no es un número ({type(a)})")
        return 0
    if not isinstance(b, (int, float)):
        print(f"comparar() - Error: b no es un número ({type(b)})")
        return 0
    try:
        result = (a > b) - (a < b)
        print(f"comparar(): a={a}, b={b}, resultado={result}")
        return result
    except Exception as e:
        print(f"comparar() - Error: {e}")
        return 0

def leer_entrada():
    try:
        entrada = input().strip()
        print(f"leer_entrada(): {entrada}")
        return entrada
    except Exception as e:
        print(f"leer_entrada() - Error: {e}")
        return ""

def parsear_json(string):
    if string is None:
        print("parsear_json() - Error: string es None")
        return None
    try:
        parsed = json.loads(string)
        print(f"parsear_json(): {parsed}")
        return parsed
    except Exception as e:
        print(f"parsear_json() - Error: {e}")
        return None

def encadenar_json(value):
    if value is None:
        print("encadenar_json() - Error: value es None")
        return None
    try:
        encoded = json.dumps(value, indent=4)
        print(f"encadenar_json(): {encoded}")
        return encoded
    except Exception as e:
        print(f"encadenar_json() - Error: {e}")
        return None

def parsear_entero(string):
    if string is None:
        print("parsear_entero() - Error: string es None")
        return None
    try:
        integer = int(string)
        print(f"parsear_entero(): {integer}")
        return integer
    except Exception as e:
        print(f"parsear_entero() - Error: {e}")
        return None

# Medición y hardware
def medicion(valor, unidad):
    if valor is None:
        print("medicion() - Error: valor es None")
        return None
    if unidad is None:
        print("medicion() - Error: unidad es None")
        return None
    print(f"medicion(): valor={valor}, unidad={unidad}")
    return valor

def altura(valor):
    if valor is None:
        print("altura() - Error: valor es None")
        return None
    print(f"altura(): {valor}")
    return valor

def longitud(valor):
    if valor is None:
        print("longitud() - Error: valor es None")
        return None
    print(f"longitud(): {valor}")
    return valor
    