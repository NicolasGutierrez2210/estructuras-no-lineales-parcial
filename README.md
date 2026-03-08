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

## Ejercicio 1

Este ejercicio implementa un algoritmo basico enfocado en analizar la complejidad temporal mediante **Big-O**.

El objetivo es comprender como el tiempo de ejecucion crece dependiendo del tamaño de entrada.

Conceptos principales:

- analisis de complejidad
- eficiencia de algoritmos
- notacion Big-O


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

# Conclusion

Este proyecto muestra la implementacion practica de varias estructuras de datos fundamentales utilizadas en el desarrollo de software y sistemas complejos.

Cada modulo permite comprender como funcionan internamente estas estructuras y como se pueden implementar en Python.
