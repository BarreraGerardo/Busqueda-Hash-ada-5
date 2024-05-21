class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        return hash(clave) % self.tamano

    def agregar(self, clave, valor):
        indice = self.funcion_hash(clave)
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

# Inicializar la tabla hash con un tamaño de 10
tabla_hash = TablaHash(10)

# Agregar elementos a la tabla hash
elementos = [10, 22, 31, 4, 15, 28, 17, 88, 59]
for elem in elementos:
    tabla_hash.agregar(elem, elem)

# Número a buscar
numero_a_buscar = 15

# Ejecución de la búsqueda
resultado = tabla_hash.buscar(numero_a_buscar)

if resultado is not None:
    print(f"Número {numero_a_buscar} encontrado en la tabla hash")
else:
    print(f"Número {numero_a_buscar} no encontrado en la tabla hash")