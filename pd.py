SALTO_DE_PAGINA = "\n"
POS_MINUTO_0 = 0
MINUTO_INICIAL = 1
MAXIMO_INICIAL = 0


def pd(archivo):
    minutos, oleadas, valoresFuncion = leer_csv(archivo)
    optimo_minuto = [POS_MINUTO_0]
    for i in range(MINUTO_INICIAL, minutos + 1):
        maximo = MAXIMO_INICIAL
        for j in range(i):
            valorF = valoresFuncion[j]
            oleada = oleadas[i-1]
            eliminados = min(valorF, oleada) + optimo_minuto[i - j - 1]
            if eliminados >= maximo:
                maximo = eliminados
        optimo_minuto.append(maximo)
    return optimo_minuto[minutos]


def leer_csv(archivo):
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

