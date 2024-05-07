SALTO_DE_PAGINA = "\n"
POS_MINUTO_0 = 0
MINUTO_INICIAL = 1
MAXIMO_INICIAL = 0


def pd(archivo):
    minutos, oleadas, valoresFuncion = leer_archivo(archivo)
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
    return optimo_minuto[minutos], reconstruir_estrategia(padres, minutos)

def optimizar_funcion(valores_funcion, oleadas):
    maximo_enemigos = max(oleadas)
    funcion_optimizada = []
    for valor in valores_funcion:
        funcion_optimizada.append(valor)
        if valor >= maximo_enemigos:
            break
    return funcion_optimizada

def reconstruir_estrategia(padres, minuto):
    res = []
    minutos_en_que_atacan = set()
    minutos_en_que_atacan.add(minuto)
    actual = padres[minuto]
    while actual > 0:
        minutos_en_que_atacan.add(actual)
        actual = padres[actual]
    for i in range(1, minuto + 1):
        if i in minutos_en_que_atacan:
            res.append("Atacar")
            continue
        res.append("Cargar")
    return ", ".join(res)


def leer_archivo(archivo):
    oleadas = []
    funcion = []
    with open(archivo) as arch:
        arch.readline()
        n = int(arch.readline().rstrip(SALTO_DE_PAGINA))
        for i in range(n):
            oleadas.append(int(arch.readline().rstrip(SALTO_DE_PAGINA)))
        for i in range(n):
            funcion.append(int(arch.readline().rstrip(SALTO_DE_PAGINA)))
    return n, oleadas, funcion

