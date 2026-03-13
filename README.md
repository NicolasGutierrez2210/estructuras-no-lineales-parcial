# Estructuras de Datos - Parcial parte 2


Los ejercicios estan organizados en carpetas independientes con su propio codigo, pruebas y documentacion.

---

# Estructura del repositorio

```
ejercicio1_.../
ejercicio2_trie/
ejercicio3_hash_table/
ej4_planificador/
```

Cada carpeta contiene:

```
src o nucleo/ -> implementacion principal
tests/ -> pruebas unitarias
README.md -> explicacion del ejercicio
```

---

# Modulo 1 - Algoritmos

# Ejercicio 1 - Estructura Organizacional (Arbol N-ario)

Este ejercicio modela la **jerarquia de una organizacion universitaria** utilizando un **arbol N-ario**.

La estructura representa diferentes niveles dentro de la institucion, por ejemplo:

```
Rectoria
├── Facultad de Ingenieria
│   ├── Programa de Sistemas
│   └── Programa de Electronica
└── Facultad de Ciencias
    └── Programa de Matematicas
```

Cada nodo del arbol representa una unidad dentro de la organizacion.

La implementacion utiliza la clase `OrganizacionNode`, donde cada nodo puede tener multiples hijos.

Para almacenar los hijos se utiliza la estructura:

```python
dict[str, OrganizacionNode]
```

Esto permite acceder a los nodos hijos **en tiempo O(1)** usando su nombre.

Conceptos principales:

- arboles N-arios
- estructuras jerarquicas
- acceso eficiente mediante diccionarios
- modelado de organizaciones

Ademas, se implementa el metodo magico `__iter__`, que permite recorrer el arbol utilizando un bucle `for`.


## Ejercicio 2 - Diccionario Tecnico (Trie)

En este ejercicio se implementa una estructura **Trie** utilizada para almacenar palabras y permitir busquedas por prefijo.

Este tipo de estructura es utilizada en:

- autocompletado de buscadores
- correctores ortograficos
- diccionarios

Conceptos principales:

- estructura de arbol
- busqueda por prefijo
- generadores con `yield`

---
# Modulo 2 - Tablas Hash
## Ejercicio 3 - Registro de Estudiantes (Hash Table)

Este ejercicio implementa una **tabla hash desde cero** para almacenar registros de estudiantes usando su ID como clave.

La implementacion no utiliza el diccionario nativo de Python para la logica interna.

Conceptos principales:

- funcion hash
- manejo de colisiones
- encadenamiento (chaining)
- metodos magicos `__setitem__` y `__getitem__`

---

# Modulo 3 - Monticulos (Heaps)

## Ejercicio 4 - Planificador de Tareas (Priority Queue)

Este ejercicio simula una **cola de prioridad similar a la utilizada por un kernel de sistema operativo**.

Se utiliza el modulo `heapq` para implementar un **min-heap** que organiza automaticamente las tareas segun su prioridad.

Conceptos principales:

- monticulos (heaps)
- colas de prioridad
- modulo `heapq`
- sobrecarga del operador `__lt__`

---

# Tecnologias utilizadas

- Python 3
- unittest para pruebas
- heapq para estructuras de monticulos

---

# Como ejecutar las pruebas

Desde la carpeta del ejercicio correspondiente ejecutar:

```bash
python -m unittest
```

Esto ejecutara las pruebas unitarias definidas para verificar el funcionamiento de cada estructura.

---

## Abstract (Sustentacion)

Este proyecto presenta la implementación y análisis de distintas estructuras de datos no lineales aplicadas a la resolución de problemas computacionales relacionados con organización de información, búsqueda eficiente y gestión de prioridades. En primer lugar, se desarrolló un árbol N-ario para modelar la estructura organizacional de una universidad, permitiendo representar jerarquías como rectoría, facultades y programas mediante nodos conectados de forma jerárquica. Posteriormente, se implementó una estructura Trie para construir un diccionario técnico capaz de realizar búsquedas por prefijo, lo cual resulta útil en sistemas de autocompletado y recuperación de información. También se diseñó una tabla hash para gestionar el registro de estudiantes utilizando identificadores únicos, lo que permite realizar operaciones de inserción y búsqueda en tiempo promedio constante mediante el uso de funciones hash y manejo de colisiones. Finalmente, se implementó una cola de prioridad basada en montículos (heaps) utilizando el módulo heapq de Python, con el fin de simular un planificador de tareas similar a los que se usan en sistemas operativos.Conjuntamente estas estructuras muestran cómo diferentes técnicas de almacenamiento y organización de datos pueden integrarse para construir sistemas computacionales eficientes capaces de manejar grandes volúmenes de información y datos y de esta manera priorizar operaciones de manera óptima.

