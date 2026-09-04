from __future__ import annotations

import sys
from typing import Any, Optional



class Nodo:
    """Nodo utilizado por la lista enlazada."""

    def __init__(self, dato: Any):
        self.dato = dato
        self.siguiente: Optional[Nodo] = None


class ListaEnlazada:
    """Lista enlazada simple para almacenar estudiantes."""

    def __init__(self):
        self.head: Optional[Nodo] = None

    def insertar_inicio(self, dato: Any) -> None:
        nuevo = Nodo(dato)
        nuevo.siguiente = self.head
        self.head = nuevo

    def insertar_final(self, dato: Any) -> None:
        nuevo = Nodo(dato)
        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def insertar_posicion(self, dato: Any, posicion: int) -> bool:
        if posicion < 0:
            return False

        nuevo = Nodo(dato)
        if posicion == 0:
            nuevo.siguiente = self.head
            self.head = nuevo
            return True

        actual = self.head
        indice = 0
        while actual is not None and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1

        if actual is None:
            return False

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        return True

    def eliminar(self, dato: Any) -> bool:
        actual = self.head
        anterior: Optional[Nodo] = None

        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return False

        if anterior is None:
            self.head = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        return True

    def buscar(self, dato: Any) -> bool:
        actual = self.head
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def contar_nodos(self) -> int:
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self) -> None:
        if self.head is None:
            print("La lista está vacía.")
            return

        actual = self.head
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def convertir_a_lista(self) -> list[Any]:
        datos: list[Any] = []
        actual = self.head
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos


class Pila:
    """Pila LIFO utilizada para mantener el historial de acciones."""

    def __init__(self):
        self.elementos: list[str] = []

    def is_empty(self) -> bool:
        return len(self.elementos) == 0

    def push(self, accion: str) -> None:
        self.elementos.append(accion)

    def pop(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.elementos.pop()

    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.elementos[-1]

    def size(self) -> int:
        return len(self.elementos)

    def mostrar(self) -> None:
        if self.is_empty():
            print("No existen acciones registradas.")
            return

        print("----- ACCIÓN MÁS RECIENTE -----")
        for indice in range(len(self.elementos) - 1, -1, -1):
            print(self.elementos[indice])
        print("----- PRIMERA ACCIÓN -----")


class Cola:
    """Cola FIFO utilizada para gestionar solicitudes de atención."""

    def __init__(self):
        self.elementos: list[str] = []

    def is_empty(self) -> bool:
        return len(self.elementos) == 0

    def enqueue(self, solicitud: str) -> None:
        self.elementos.append(solicitud)

    def dequeue(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.elementos.pop(0)

    def peek(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.elementos[0]

    def ultimo(self) -> Optional[str]:
        if self.is_empty():
            return None
        return self.elementos[-1]

    def size(self) -> int:
        return len(self.elementos)

    def mostrar(self) -> None:
        if self.is_empty():
            print("No existen solicitudes pendientes.")
            return

        print("Frente -> ", end="")
        for solicitud in self.elementos:
            print(solicitud, end=" -> ")
        print("Final")



class NodoArbol:
    """Nodo del árbol: dato, hijo izquierdo e hijo derecho."""

    def __init__(self, dato: int):
        self.dato = dato
        self.izquierda: Optional[NodoArbol] = None
        self.derecha: Optional[NodoArbol] = None


class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda integrado al sistema."""

    def __init__(self):
        self.raiz: Optional[NodoArbol] = None

    def insertar(self, dato: int) -> bool:
        """Inserta un dato respetando la regla izquierda < raíz < derecha."""
        antes = self.contar_nodos()
        self.raiz = self._insertar_recursivo(self.raiz, dato)
        return self.contar_nodos() > antes

    def _insertar_recursivo(
        self,
        raiz: Optional[NodoArbol],
        dato: int,
    ) -> NodoArbol:
        if raiz is None:
            return NodoArbol(dato)

        if dato < raiz.dato:
            raiz.izquierda = self._insertar_recursivo(raiz.izquierda, dato)
        elif dato > raiz.dato:
            raiz.derecha = self._insertar_recursivo(raiz.derecha, dato)
 
        return raiz

    def contar_nodos(self) -> int:
        def contar(raiz: Optional[NodoArbol]) -> int:
            if raiz is None:
                return 0
            return 1 + contar(raiz.izquierda) + contar(raiz.derecha)

        return contar(self.raiz)

    
    def preorden(self) -> list[int]:
        resultado: list[int] = []

        def recorrer(raiz: Optional[NodoArbol]) -> None:
            if raiz is None:
                return
            resultado.append(raiz.dato)
            recorrer(raiz.izquierda)
            recorrer(raiz.derecha)

        recorrer(self.raiz)
        return resultado

    def inorden(self) -> list[int]:
        resultado: list[int] = []

        def recorrer(raiz: Optional[NodoArbol]) -> None:
            if raiz is None:
                return
            recorrer(raiz.izquierda)
            resultado.append(raiz.dato)
            recorrer(raiz.derecha)

        recorrer(self.raiz)
        return resultado

    def postorden(self) -> list[int]:
        resultado: list[int] = []

        def recorrer(raiz: Optional[NodoArbol]) -> None:
            if raiz is None:
                return
            recorrer(raiz.izquierda)
            recorrer(raiz.derecha)
            resultado.append(raiz.dato)

        recorrer(self.raiz)
        return resultado

    def mostrar_recorridos(self) -> None:
        print("Preorden :", " -> ".join(map(str, self.preorden())))
        print("Inorden  :", " -> ".join(map(str, self.inorden())))
        print("Postorden:", " -> ".join(map(str, self.postorden())))



class Grafo:
    """Grafo no dirigido ponderado.

    La estructura de aristas se amplía para incorporar un peso:
        (origen, destino)
    a:
        (origen, destino, peso)

    El peso representa, para la práctica, tiempo de traslado en minutos.
    """

    def __init__(self):
        self.vertices: list[str] = []
        self.aristas: dict[str, tuple[str, str, float]] = {}

    def agregar_vertice(self, vertice: str, mostrar_mensaje: bool = True) -> bool:
        vertice = vertice.strip()
        if vertice == "":
            if mostrar_mensaje:
                print("El vértice no puede estar vacío.")
            return False

        if vertice in self.vertices:
            if mostrar_mensaje:
                print("El vértice ya existe:", vertice)
            return False

        self.vertices.append(vertice)
        if mostrar_mensaje:
            print("Vértice agregado:", vertice)
        return True

    def agregar_arista(
        self,
        nombre: str,
        origen: str,
        destino: str,
        peso: float,
        mostrar_mensaje: bool = True,
    ) -> bool:
        """Agrega una conexión ponderada; Dijkstra exige pesos no negativos."""
        nombre = nombre.strip()
        origen = origen.strip()
        destino = destino.strip()

        if nombre == "" or origen == "" or destino == "":
            if mostrar_mensaje:
                print("La arista, el origen y el destino no pueden estar vacíos.")
            return False

        if peso < 0:
            if mostrar_mensaje:
                print("El peso no puede ser negativo.")
            return False

        if nombre in self.aristas:
            if mostrar_mensaje:
                print("Ya existe una arista llamada", nombre)
            return False

        if origen not in self.vertices:
            if mostrar_mensaje:
                print("No existe el vértice:", origen)
            return False

        if destino not in self.vertices:
            if mostrar_mensaje:
                print("No existe el vértice:", destino)
            return False

        self.aristas[nombre] = (origen, destino, float(peso))
        if mostrar_mensaje:
            print(f"Arista agregada: {nombre} = {origen} -- {destino} (peso={peso})")
        return True

    def actualizar_peso(
        self,
        nombre_arista: str,
        nuevo_peso: float,
        mostrar_mensaje: bool = True,
    ) -> bool:
        """Permite probar cómo cambia Dijkstra al modificar un peso."""
        if nuevo_peso < 0:
            if mostrar_mensaje:
                print("El peso no puede ser negativo.")
            return False

        if nombre_arista not in self.aristas:
            if mostrar_mensaje:
                print("La arista no existe:", nombre_arista)
            return False

        origen, destino, _ = self.aristas[nombre_arista]
        self.aristas[nombre_arista] = (origen, destino, float(nuevo_peso))
        if mostrar_mensaje:
            print(f"Peso actualizado: {nombre_arista} = {nuevo_peso}")
        return True


    def mostrar_grafo(self) -> None:
        print("\n--- GRAFO PONDERADO ---")
        print("Vértices:")
        for vertice in self.vertices:
            print("-", vertice)

        print("\nAristas con peso:")
        if not self.aristas:
            print("No existen conexiones registradas.")
            return

        for nombre, (origen, destino, peso) in self.aristas.items():
            print(f"{nombre}: {origen} -- {destino} | peso={peso:g}")

    def es_bucle(self, nombre_arista: str) -> bool:
        if nombre_arista not in self.aristas:
            return False
        origen, destino, _ = self.aristas[nombre_arista]
        return origen == destino

    def son_paralelas(self, arista1: str, arista2: str) -> bool:
        if arista1 not in self.aristas or arista2 not in self.aristas:
            return False
        if arista1 == arista2:
            return False

        origen1, destino1, _ = self.aristas[arista1]
        origen2, destino2, _ = self.aristas[arista2]
        mismos_extremos = origen1 == origen2 and destino1 == destino2
        extremos_invertidos = origen1 == destino2 and destino1 == origen2
        return mismos_extremos or extremos_invertidos

    def obtener_aristas_paralelas(self) -> list[tuple[str, str]]:
        paralelas: list[tuple[str, str]] = []
        nombres = list(self.aristas.keys())
        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                if self.son_paralelas(nombres[i], nombres[j]):
                    paralelas.append((nombres[i], nombres[j]))
        return paralelas

    def obtener_bucles(self) -> list[str]:
        return [nombre for nombre in self.aristas if self.es_bucle(nombre)]

    def grado(self, vertice: str) -> Optional[int]:
        if vertice not in self.vertices:
            return None

        contador = 0
        for origen, destino, _ in self.aristas.values():
            if origen == vertice and destino == vertice:
                contador += 2
            elif origen == vertice or destino == vertice:
                contador += 1
        return contador

    def es_aislado(self, vertice: str) -> bool:
        grado_vertice = self.grado(vertice)
        return grado_vertice == 0 if grado_vertice is not None else False

    def obtener_vertices_aislados(self) -> list[str]:
        return [vertice for vertice in self.vertices if self.es_aislado(vertice)]

    def grado_total(self) -> int:
        total = 0
        for vertice in self.vertices:
            grado_vertice = self.grado(vertice)
            if grado_vertice is not None:
                total += grado_vertice
        return total

    def matriz_adyacencia(self) -> list[list[int]]:
        """Matriz estructural que registra la cantidad de conexiones."""
        cantidad = len(self.vertices)
        matriz = [[0] * cantidad for _ in range(cantidad)]

        for origen, destino, _ in self.aristas.values():
            i = self.vertices.index(origen)
            j = self.vertices.index(destino)
            if i == j:
                matriz[i][j] += 2
            else:
                matriz[i][j] += 1
                matriz[j][i] += 1
        return matriz

    def matriz_incidencia(self) -> list[list[int]]:
        cantidad_vertices = len(self.vertices)
        cantidad_aristas = len(self.aristas)
        matriz = [[0] * cantidad_aristas for _ in range(cantidad_vertices)]
        nombres = list(self.aristas.keys())

        for j, nombre in enumerate(nombres):
            origen, destino, _ = self.aristas[nombre]
            i_origen = self.vertices.index(origen)
            i_destino = self.vertices.index(destino)
            if i_origen == i_destino:
                matriz[i_origen][j] = 2
            else:
                matriz[i_origen][j] = 1
                matriz[i_destino][j] = 1
        return matriz

    def obtener_vecinos(self, vertice: str) -> list[str]:
        if vertice not in self.vertices:
            return []

        vecinos: list[str] = []
        for origen, destino, _ in self.aristas.values():
            if origen == vertice and destino not in vecinos:
                vecinos.append(destino)
            if destino == vertice and origen not in vecinos:
                vecinos.append(origen)
        return vecinos

    def lista_adyacencia(self) -> dict[str, list[str]]:
        lista: dict[str, list[str]] = {vertice: [] for vertice in self.vertices}
        for origen, destino, _ in self.aristas.values():
            lista[origen].append(destino)
            if origen != destino:
                lista[destino].append(origen)
        return lista

    def lista_adyacencia_ponderada(self) -> dict[str, list[tuple[str, float]]]:
        """Lista de adyacencia con pares (vecino, peso).

        Es la representación recomendada para Dijkstra en este proyecto porque el
        grafo es pequeño y relativamente disperso, y permite obtener directamente
        los vecinos y el costo de cada conexión.
        """
        lista: dict[str, list[tuple[str, float]]] = {
            vertice: [] for vertice in self.vertices
        }

        for origen, destino, peso in self.aristas.values():
            lista[origen].append((destino, peso))
            if origen != destino:
                lista[destino].append((origen, peso))
        return lista

    def obtener_vecinos_con_peso(self, vertice: str) -> list[tuple[str, float]]:
        """Devuelve los pares (vecino, peso) que Dijkstra necesita relajar."""
        if vertice not in self.vertices:
            return []
        return self.lista_adyacencia_ponderada()[vertice]

    def mostrar_lista_adyacencia_ponderada(self) -> None:
        print("\n--- LISTA DE ADYACENCIA PONDERADA ---")
        lista = self.lista_adyacencia_ponderada()
        for vertice, vecinos in lista.items():
            texto = ", ".join(f"{vecino}({peso:g})" for vecino, peso in vecinos)
            print(f"{vertice} -> {texto}")


    def dijkstra(
        self,
        inicio: str,
    ) -> tuple[dict[str, float], dict[str, Optional[str]]]:
        """Calcula costos mínimos desde 'inicio' hacia todos los vértices.

        Implementación didáctica O(V^2), alineada con la lógica de la guía:
        1) infinito para todos;
        2) cero al origen;
        3) seleccionar no visitado con menor distancia;
        4) relajar cada arista hacia sus vecinos;
        5) guardar el nodo anterior.
        """
        if inicio not in self.vertices:
            return {}, {}

        distancias: dict[str, float] = {}
        anteriores: dict[str, Optional[str]] = {}
        visitados: set[str] = set()

        for vertice in self.vertices:
            distancias[vertice] = float("inf")
            anteriores[vertice] = None

        distancias[inicio] = 0.0

        while len(visitados) < len(self.vertices):
            actual: Optional[str] = None
            menor_distancia = float("inf")

            for vertice in self.vertices:
                if vertice not in visitados and distancias[vertice] < menor_distancia:
                    actual = vertice
                    menor_distancia = distancias[vertice]

            if actual is None:
                break

            visitados.add(actual)

            for vecino, peso in self.obtener_vecinos_con_peso(actual):
                if vecino in visitados:
                    continue

                nueva_distancia = distancias[actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual

        return distancias, anteriores

    def reconstruir_ruta(
        self,
        anteriores: dict[str, Optional[str]],
        destino: str,
    ) -> list[str]:
        """Reconstruye la ruta retrocediendo desde el destino y luego invierte."""
        if destino not in anteriores:
            return []

        ruta: list[str] = []
        actual: Optional[str] = destino
        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.reverse()
        return ruta

    def ruta_minima(self, origen: str, destino: str) -> tuple[list[str], float]:
        """Atajo seguro para obtener ruta y costo en una sola llamada."""
        if origen not in self.vertices or destino not in self.vertices:
            return [], float("inf")

        distancias, anteriores = self.dijkstra(origen)
        if not distancias or distancias[destino] == float("inf"):
            return [], float("inf")

        ruta = self.reconstruir_ruta(anteriores, destino)
        if not ruta or ruta[0] != origen:
            return [], float("inf")
        return ruta, distancias[destino]

    def resumen(self) -> None:
        print("\n========== RESUMEN DEL GRAFO ==========")
        print("Cantidad de vértices:", len(self.vertices))
        print("Cantidad de aristas:", len(self.aristas))
        print("Grado total:", self.grado_total())
        print("Vértices aislados:", self.obtener_vertices_aislados())
        print("Aristas paralelas:", self.obtener_aristas_paralelas())
        print("Bucles:", self.obtener_bucles())


def registrar_estudiante(
    estudiantes: ListaEnlazada,
    historial: Pila,
    nombre: str,
    mostrar_mensaje: bool = True,
) -> bool:
    nombre = nombre.strip()
    if nombre == "":
        if mostrar_mensaje:
            print("El nombre no puede estar vacío.")
        return False

    estudiantes.insertar_final(nombre)
    historial.push("Registrar estudiante: " + nombre)
    if mostrar_mensaje:
        print("Estudiante registrado.")
    return True


def eliminar_estudiante(
    estudiantes: ListaEnlazada,
    historial: Pila,
    nombre: str,
    mostrar_mensaje: bool = True,
) -> bool:
    nombre = nombre.strip()
    eliminado = estudiantes.eliminar(nombre)
    if eliminado:
        historial.push("Eliminar estudiante: " + nombre)
        if mostrar_mensaje:
            print("Estudiante eliminado.")
    elif mostrar_mensaje:
        print("El estudiante no existe.")
    return eliminado


def registrar_solicitud(
    estudiantes: ListaEnlazada,
    solicitudes: Cola,
    historial: Pila,
    nombre: str,
    mostrar_mensaje: bool = True,
) -> bool:
    nombre = nombre.strip()
    if nombre == "":
        if mostrar_mensaje:
            print("El nombre no puede estar vacío.")
        return False

    if not estudiantes.buscar(nombre):
        if mostrar_mensaje:
            print("El estudiante no existe.")
        return False

    if solicitudes.ultimo() == nombre:
        if mostrar_mensaje:
            print("Solicitud rechazada: no se permiten duplicados consecutivos.")
        return False

    solicitudes.enqueue(nombre)
    historial.push("Registrar solicitud: " + nombre)
    if mostrar_mensaje:
        print("Solicitud registrada.")
    return True


def atender_solicitud(
    solicitudes: Cola,
    historial: Pila,
    mostrar_mensaje: bool = True,
) -> Optional[str]:
    nombre = solicitudes.dequeue()
    if nombre is None:
        if mostrar_mensaje:
            print("No existen solicitudes pendientes.")
        return None

    historial.push("Atender solicitud: " + nombre)
    if mostrar_mensaje:
        print("Atendiendo a:", nombre)
    return nombre


def crear_arbol_guia() -> ArbolBinarioBusqueda:
    """Árbol usado por la guía: 50, 30, 70, 20, 40, 60, 80."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)
    return arbol


def crear_grafo_guia() -> Grafo:
    """Grafo ponderado exactamente con los vértices y pesos de la guía."""
    grafo = Grafo()
    for vertice in ["Bodega", "Norte", "Centro", "Sur", "Aeropuerto"]:
        grafo.agregar_vertice(vertice, mostrar_mensaje=False)

    conexiones = [
        ("e1", "Bodega", "Norte", 4),
        ("e2", "Bodega", "Centro", 2),
        ("e3", "Norte", "Centro", 1),
        ("e4", "Norte", "Sur", 5),
        ("e5", "Centro", "Sur", 8),
        ("e6", "Centro", "Aeropuerto", 10),
        ("e7", "Sur", "Aeropuerto", 2),
    ]

    for nombre, origen, destino, peso in conexiones:
        grafo.agregar_arista(nombre, origen, destino, peso, mostrar_mensaje=False)
    return grafo


def mostrar_matriz(titulo: str, filas: list[list[int]], encabezados: list[str]) -> None:
    print("\n" + titulo)
    print(f"{'':>12}", end="")
    for encabezado in encabezados:
        print(f"{encabezado[:8]:>10}", end="")
    print()
    for i, fila in enumerate(filas):
        etiqueta = encabezados[i] if i < len(encabezados) else str(i)
        print(f"{etiqueta[:10]:>12}", end="")
        for valor in fila:
            print(f"{valor:>10}", end="")
        print()


def mostrar_menu() -> None:
    """Ejecuta todas las estructuras desde un único menú integrado."""
    estudiantes = ListaEnlazada()
    historial = Pila()
    solicitudes = Cola()
    arbol = crear_arbol_guia()
    grafo = crear_grafo_guia()

    while True:
        print("\n================ SISTEMA DE GESTIÓN ================")
        print(" 1. Registrar estudiante")
        print(" 2. Mostrar estudiantes")
        print(" 3. Buscar estudiante")
        print(" 4. Eliminar estudiante")
        print(" 5. Contar estudiantes")
        print(" 6. Insertar estudiante al inicio")
        print(" 7. Insertar estudiante en una posición")
        print(" 8. Registrar solicitud de atención")
        print(" 9. Atender siguiente solicitud")
        print("10. Consultar siguiente solicitud")
        print("11. Mostrar solicitudes pendientes")
        print("12. Mostrar historial de acciones")
        print("13. Consultar última acción")
        print("14. Insertar valor en el árbol")
        print("15. Mostrar recorrido preorden")
        print("16. Mostrar recorrido inorden")
        print("17. Mostrar recorrido postorden")
        print("18. Mostrar todos los recorridos del árbol")
        print("19. Mostrar grafo ponderado")
        print("20. Mostrar lista de adyacencia ponderada")
        print("21. Agregar vértice al grafo")
        print("22. Agregar conexión con peso")
        print("23. Modificar peso de una conexión")
        print("24. Calcular ruta mínima con Dijkstra")
        print("25. Mostrar matriz de adyacencia")
        print("26. Mostrar resumen del grafo")
        print("27. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante(estudiantes, historial, input("Nombre: "))

        elif opcion == "2":
            print("\n--- ESTUDIANTES REGISTRADOS ---")
            estudiantes.mostrar()

        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            print("Encontrado." if estudiantes.buscar(nombre) else "No encontrado.")

        elif opcion == "4":
            eliminar_estudiante(estudiantes, historial, input("Nombre a eliminar: "))

        elif opcion == "5":
            print("Cantidad de estudiantes:", estudiantes.contar_nodos())

        elif opcion == "6":
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
            else:
                estudiantes.insertar_inicio(nombre)
                historial.push("Insertar estudiante al inicio: " + nombre)
                print("Estudiante insertado al inicio.")

        elif opcion == "7":
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue
            try:
                posicion = int(input("Posición (desde 0): "))
            except ValueError:
                print("La posición debe ser un entero.")
                continue

            if estudiantes.insertar_posicion(nombre, posicion):
                historial.push(f"Insertar estudiante {nombre} en posición {posicion}")
                print("Estudiante insertado.")
            else:
                print("Posición no válida.")

        elif opcion == "8":
            registrar_solicitud(
                estudiantes,
                solicitudes,
                historial,
                input("Nombre del estudiante: "),
            )

        elif opcion == "9":
            atender_solicitud(solicitudes, historial)

        elif opcion == "10":
            siguiente = solicitudes.peek()
            if siguiente is None:
                print("No existen solicitudes pendientes.")
            else:
                print("Siguiente estudiante:", siguiente)

        elif opcion == "11":
            solicitudes.mostrar()
            print("Cantidad:", solicitudes.size())

        elif opcion == "12":
            historial.mostrar()

        elif opcion == "13":
            accion = historial.peek()
            if accion is None:
                print("No existen acciones registradas.")
            else:
                print("Última acción:", accion)

        elif opcion == "14":
            try:
                valor = int(input("Valor entero: "))
            except ValueError:
                print("Entrada no válida: debe ingresar un entero.")
                continue

            if arbol.insertar(valor):
                historial.push(f"Insertar valor en árbol: {valor}")
                print("Valor insertado.")
            else:
                print("El valor ya existe en el árbol.")

        elif opcion == "15":
            print("Preorden:", " -> ".join(map(str, arbol.preorden())))

        elif opcion == "16":
            print("Inorden:", " -> ".join(map(str, arbol.inorden())))

        elif opcion == "17":
            print("Postorden:", " -> ".join(map(str, arbol.postorden())))

        elif opcion == "18":
            print("\n--- RECORRIDOS DEL ÁRBOL ---")
            arbol.mostrar_recorridos()

        elif opcion == "19":
            grafo.mostrar_grafo()

        elif opcion == "20":
            grafo.mostrar_lista_adyacencia_ponderada()

        elif opcion == "21":
            vertice = input("Nuevo vértice: ").strip()
            if grafo.agregar_vertice(vertice):
                historial.push("Agregar vértice al grafo: " + vertice)

        elif opcion == "22":
            nombre = input("Nombre de arista: ").strip()
            origen = input("Origen: ").strip()
            destino = input("Destino: ").strip()
            try:
                peso = float(input("Peso: "))
            except ValueError:
                print("El peso debe ser numérico.")
                continue

            if grafo.agregar_arista(nombre, origen, destino, peso):
                historial.push(
                    f"Agregar conexión ponderada: {nombre} "
                    f"{origen}--{destino} peso={peso:g}"
                )

        elif opcion == "23":
            nombre = input("Arista a modificar: ").strip()
            try:
                peso = float(input("Nuevo peso: "))
            except ValueError:
                print("El peso debe ser numérico.")
                continue

            if grafo.actualizar_peso(nombre, peso):
                historial.push(f"Actualizar peso: {nombre}={peso:g}")

        elif opcion == "24":
            origen = input("Origen: ").strip()
            destino = input("Destino: ").strip()
            ruta, costo = grafo.ruta_minima(origen, destino)

            if not ruta:
                print("No se pudo calcular una ruta. Revise los vértices o la conectividad.")
            else:
                print("Ruta mínima:", " -> ".join(ruta))
                print("Costo total:", f"{costo:g}")
                historial.push(f"Dijkstra: {origen}->{destino} costo={costo:g}")

        elif opcion == "25":
            mostrar_matriz(
                "--- MATRIZ DE ADYACENCIA ---",
                grafo.matriz_adyacencia(),
                grafo.vertices,
            )

        elif opcion == "26":
            grafo.resumen()

        elif opcion == "27":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")



def ejecutar_pruebas_lista() -> bool:
    """Comprueba inserción, recorrido, búsqueda y eliminación."""
    lista = ListaEnlazada()
    for nombre in ["Ana", "Luis", "Marta", "Pedro"]:
        lista.insertar_final(nombre)

    insercion_ok = lista.convertir_a_lista() == ["Ana", "Luis", "Marta", "Pedro"]
    busqueda_ok = lista.buscar("Marta") and not lista.buscar("Carlos")
    conteo_ok = lista.contar_nodos() == 4
    posicion_ok = lista.insertar_posicion("Carlos", 2)
    posicion_ok = posicion_ok and lista.convertir_a_lista() == [
        "Ana", "Luis", "Carlos", "Marta", "Pedro"
    ]
    eliminacion_ok = lista.eliminar("Carlos") and lista.convertir_a_lista() == [
        "Ana", "Luis", "Marta", "Pedro"
    ]

    correcto = all([insercion_ok, busqueda_ok, conteo_ok, posicion_ok, eliminacion_ok])
    print("LISTA ENLAZADA:", "CORRECTA" if correcto else "REVISAR")
    return correcto


def ejecutar_pruebas_pila_cola() -> bool:
    resultados: list[bool] = []

    pila = Pila()
    resultados.append(pila.peek() is None and pila.pop() is None)

    cola = Cola()
    resultados.append(cola.peek() is None and cola.dequeue() is None)

    estudiantes = ListaEnlazada()
    historial = Pila()
    solicitudes = Cola()
    for nombre in ["Ana", "Luis", "Marta", "Pedro"]:
        registrar_estudiante(estudiantes, historial, nombre, False)

    antes = list(solicitudes.elementos)
    aceptada = registrar_solicitud(
        estudiantes, solicitudes, historial, "Carlos", False
    )
    resultados.append(not aceptada and antes == solicitudes.elementos)

    prueba_pila = Pila()
    for accion in ["A", "B", "C"]:
        prueba_pila.push(accion)
    resultados.append(
        [prueba_pila.pop(), prueba_pila.pop(), prueba_pila.pop()] == ["C", "B", "A"]
    )

    prueba_cola = Cola()
    for nombre in ["Luis", "Ana", "Pedro", "Marta"]:
        prueba_cola.enqueue(nombre)
    resultados.append(
        [prueba_cola.dequeue(), prueba_cola.dequeue()] == ["Luis", "Ana"]
        and prueba_cola.elementos == ["Pedro", "Marta"]
    )

    reto = Cola()
    historial_reto = Pila()
    for nombre in ["Ana", "Marta", "Luis"]:
        registrar_solicitud(estudiantes, reto, historial_reto, nombre, False)
    duplicada = registrar_solicitud(
        estudiantes, reto, historial_reto, "Luis", False
    )
    resultados.append(not duplicada and reto.elementos == ["Ana", "Marta", "Luis"])

    correcto = all(resultados)
    print("PILA Y COLA:", "CORRECTAS" if correcto else "REVISAR")
    return correcto


def ejecutar_pruebas_no_lineales() -> bool:
    """Comprueba árbol, grafo ponderado, Dijkstra y entradas inválidas."""
    resultados: list[bool] = []

    print("\n========== PRUEBAS DE ESTRUCTURAS NO LINEALES ==========")

    arbol = crear_arbol_guia()
    pre = arbol.preorden()
    ino = arbol.inorden()
    post = arbol.postorden()
    arbol_ok = (
        pre == [50, 30, 20, 40, 70, 60, 80]
        and ino == [20, 30, 40, 50, 60, 70, 80]
        and post == [20, 40, 30, 60, 80, 70, 50]
    )
    resultados.append(arbol_ok)
    print("1. Recorridos del árbol:", "OK" if arbol_ok else "ERROR")
    print("   Preorden :", pre)
    print("   Inorden  :", ino)
    print("   Postorden:", post)

    grafo = crear_grafo_guia()
    ruta1, costo1 = grafo.ruta_minima("Bodega", "Aeropuerto")
    dijkstra_inicial_ok = (
        ruta1 == ["Bodega", "Centro", "Norte", "Sur", "Aeropuerto"]
        and costo1 == 10
    )
    resultados.append(dijkstra_inicial_ok)
    print("2. Dijkstra inicial:", "OK" if dijkstra_inicial_ok else "ERROR")
    print("   Ruta :", " -> ".join(ruta1))
    print("   Costo:", costo1)

    grafo.actualizar_peso("e6", 1, mostrar_mensaje=False)
    ruta2, costo2 = grafo.ruta_minima("Bodega", "Aeropuerto")
    cambio_ok = ruta2 == ["Bodega", "Centro", "Aeropuerto"] and costo2 == 3
    resultados.append(cambio_ok)
    print("3. Cambio de peso e6=1:", "OK" if cambio_ok else "ERROR")
    print("   Ruta :", " -> ".join(ruta2))
    print("   Costo:", costo2)

    negativo_aceptado = grafo.agregar_arista(
        "negativa", "Bodega", "Sur", -5, mostrar_mensaje=False
    )
    negativo_ok = not negativo_aceptado
    resultados.append(negativo_ok)
    print("4. Rechazo de peso negativo:", "OK" if negativo_ok else "ERROR")

    ruta_invalida, costo_invalido = grafo.ruta_minima("Inexistente", "Aeropuerto")
    invalida_ok = ruta_invalida == [] and costo_invalido == float("inf")
    resultados.append(invalida_ok)
    print("5. Entrada no válida:", "OK" if invalida_ok else "ERROR")

    correcto = all(resultados)
    print(
        "RESULTADO DE ESTRUCTURAS NO LINEALES:",
        "TODAS LAS PRUEBAS CORRECTAS" if correcto else "REVISAR",
    )
    return correcto


def ejecutar_todas_las_pruebas() -> bool:
    lista = ejecutar_pruebas_lista()
    pila_cola = ejecutar_pruebas_pila_cola()
    no_lineales = ejecutar_pruebas_no_lineales()
    correcto = lista and pila_cola and no_lineales
    print("\nRESULTADO GENERAL:", "CORRECTO" if correcto else "REVISAR")
    return correcto


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--pruebas-lista":
        sys.exit(0 if ejecutar_pruebas_lista() else 1)

    if len(sys.argv) > 1 and sys.argv[1] == "--pruebas-pila-cola":
        sys.exit(0 if ejecutar_pruebas_pila_cola() else 1)

    if len(sys.argv) > 1 and sys.argv[1] == "--pruebas-no-lineales":
        sys.exit(0 if ejecutar_pruebas_no_lineales() else 1)

    if len(sys.argv) > 1 and sys.argv[1] == "--pruebas":
        sys.exit(0 if ejecutar_todas_las_pruebas() else 1)

    mostrar_menu()
