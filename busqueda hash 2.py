class TablaHashNombres:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        return hash(clave) % self.tamano

    def agregar(self, clave):
        indice = self.funcion_hash(clave)
        self.tabla[indice].append(clave)

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for k in self.tabla[indice]:
            if k == clave:
                return True
        return False

# Inicializar la tabla hash con un tamaño de 10
tabla_hash_nombres = TablaHashNombres(10)

# Agregar nombres a la tabla hash
nombres = ["Ana", "Luis", "Pedro", "Maria", "Juan", "Carla", "José"]
for nombre in nombres:
    tabla_hash_nombres.agregar(nombre)

# Nombre a buscar
nombre_a_buscar = "Maria"

# Ejecución de la búsqueda
encontrado = tabla_hash_nombres.buscar(nombre_a_buscar)

if encontrado:
    print(f"Nombre {nombre_a_buscar} encontrado en la tabla hash")
else:
    print(f"Nombre {nombre_a_buscar} no encontrado en la tabla hash")