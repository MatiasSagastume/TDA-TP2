import random

PRIMER_LINEA = "# La primera línea indica la cantidad de minutos a considerar (n). Luego vienen n líneas que corresponden a los x_i, y luego los n valores que corresponden a la función f(.):"
SALTO_DE_LINEA = "\n"


def random_cases_generator(ruta, max_enemigos, max_recarga, minutos):
    with open(ruta, "w") as archivo:
        archivo.write(PRIMER_LINEA + SALTO_DE_LINEA)
        archivo.write(f"{minutos}\n")
        for i in range(minutos):
            archivo.write(str(random.randint(0, max_enemigos)) + SALTO_DE_LINEA)
        valor_funcion = random.randint(0, max_recarga)
        for i in range(minutos):
            archivo.write(str(valor_funcion) + SALTO_DE_LINEA)
            valor_funcion += random.randint(0, max_recarga)


for i in range(1, 11):
    random_cases_generator(f"../Casos/CasosNuestros/caso{i}.txt", 5000, 10, 1000)