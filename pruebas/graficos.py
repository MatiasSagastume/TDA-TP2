import matplotlib.pyplot as plt
import random
import time

SALTO_DE_PAGINA = "\n"
POS_MINUTO_0 = 0
MINUTO_INICIAL = 1
MAXIMO_INICIAL = 0

MAX_ENEMIGOS = 5000
MAX_RECARGA = 10

TAMANIO_INICIAL = 1
TAMANIO_FINAL = 10000
TAMANIO_SALTO = 100


def pd(minutos, oleadas, valoresFuncion):
    valoresFuncion = optimizar_funcion(valoresFuncion, oleadas)
    optimo_minuto = [POS_MINUTO_0]
    padres = {}
    for i in range(MINUTO_INICIAL, minutos + 1):
        maximo = MAXIMO_INICIAL
        for j in range(i):
            valorF = valoresFuncion[j]
            oleada = oleadas[i-1]
            eliminados = min(valorF, oleada) + optimo_minuto[i - j - 1]
            if eliminados >= maximo:
                padres[i] = i - j - 1
                maximo = eliminados
            if valorF >= oleada:
                break
        optimo_minuto.append(maximo)
    return optimo_minuto[minutos]

def optimizar_funcion(valores_funcion, oleadas):
    maximo_enemigos = max(oleadas)
    funcion_optimizada = []
    for valor in valores_funcion:
        funcion_optimizada.append(valor)
        if valor >= maximo_enemigos:
            break
    return funcion_optimizada


def random_generator(max_enemigos, max_recarga, minutos):
    oleadas = []
    valoresFuncion = []
    for i in range(minutos):
        oleadas.append(random.randint(0, max_enemigos))
    valor_funcion = random.randint(0, max_recarga)
    for i in range(minutos):
        valoresFuncion.append(valor_funcion)
        valor_funcion += random.randint(0, max_recarga)
    return oleadas, valoresFuncion


def crear_tamanio_vs_tiempo(max_enemigos, max_recarga, minutos):
    oleadas, valoresFuncion = random_generator(max_enemigos, max_recarga, minutos)
    inicio = time.time()
    pd(minutos, oleadas, valoresFuncion)
    fin = time.time()
    duracion = fin - inicio
    return duracion * 1000


def graficarFuncionTamanio():
    listaTamanios = []
    listaDuraciones = []
    for i in range(TAMANIO_INICIAL, TAMANIO_FINAL, TAMANIO_SALTO):
        tiempo = crear_tamanio_vs_tiempo(MAX_ENEMIGOS, MAX_RECARGA, i)
        listaTamanios.append(i)
        listaDuraciones.append(tiempo)
    plt.figure(figsize=(10, 6))
    plt.plot(listaTamanios, listaDuraciones, marker='o', linestyle='-')
    plt.title('Gráfico de Tamaño vs Tiempo')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (milisegundos)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def graficarxcuadrado():
    listaTamanios = []
    listaDuraciones = []
    for i in range(TAMANIO_INICIAL, TAMANIO_FINAL, TAMANIO_SALTO):
        listaTamanios.append(i)
        listaDuraciones.append(i * i)
    plt.figure(figsize=(10, 6))
    plt.plot(listaTamanios, listaDuraciones, marker='o', linestyle='-')
    plt.title('Gráfico de $x^2$')
    plt.xlabel('x')
    plt.ylabel("$x^2$")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


graficarxcuadrado()
