import pd
import sys

UBICACION_RUTA = 1
UBICACION_COMANDO = 2
UBICACION_RUTA_GUARDAR = 3
GUARDAR = "-guardar"
TEXTO_SUMA = "Suma Ponderada"
SEPARADOR = " = "
MENSAJE_ERROR_PARAMETROS = "Error: parametros insuficientes"
MENSAJE_ERROR_RUTA = "Error: Ruta Inválida"
RUTA_GENERICA = "resultado.txt"


def main():
    args = sys.argv
    ruta = args[UBICACION_RUTA]
    if len(args) < 1:
        print(MENSAJE_ERROR_PARAMETROS)
        return
    rutaGuardado = None
    if len(args) > 2:
        if args[UBICACION_COMANDO] == GUARDAR:
            rutaGuardado = args[UBICACION_RUTA_GUARDAR]
    enemigos_eliminados, estrategia = pd.pd(ruta)
    if not rutaGuardado:
        rutaGuardado = RUTA_GENERICA
    try:
        with open(rutaGuardado, "w") as archivo:
            archivo.write(f"Estrategia: {estrategia}")
            archivo.write(f"\nCantidad de tropas eliminadas: {enemigos_eliminados}")
    except Exception:
        print(MENSAJE_ERROR_RUTA)


main()
