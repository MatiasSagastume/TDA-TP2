import pd

optimo, estrategia = pd.pd("caso1.txt")
print(optimo)
print(estrategia)
assert optimo == 24 and estrategia == "Cargar, Cargar, Cargar, Atacar, Atacar"
print("OK")