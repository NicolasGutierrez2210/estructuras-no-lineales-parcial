# Ejercicio 2 - Diccionario Técnico (Trie)

## Descripción

Este ejercicio implementa una estructura de datos **Trie** para un sistema de **autocompletado de palabras**.

Un **Trie** es un árbol utilizado para almacenar cadenas de caracteres. Cada nodo representa un carácter y las rutas desde la raíz forman palabras completas.

En esta implementación cada nodo utiliza un **diccionario** para almacenar sus hijos, lo que permite acceder rápidamente al siguiente carácter.

Este tipo de estructura se usa comúnmente en:

- Motores de búsqueda  
- Autocompletado de texto  
- Correctores ortográficos  
- Diccionarios

---

# Explicación del código

## Clase `TrieNode`

Representa un nodo del Trie.

Cada nodo contiene dos elementos principales:

- `hijos`: un diccionario que conecta con los nodos hijos
- `es_palabra`: un valor booleano que indica si el nodo representa el final de una palabra

Ejemplo del código:

```python
self.hijos: Dict[str, TrieNode] = {}
self.es_palabra: bool = False
```

Esto permite construir el árbol carácter por carácter.

---

## Método `insertar`

Este método agrega una palabra al Trie carácter por carácter.

```python
def insertar(self, palabra: str) -> None:
```

Funcionamiento:

1. Se empieza desde la raíz.
2. Se recorre cada carácter de la palabra.
3. Si el carácter no existe en los hijos del nodo actual, se crea un nuevo nodo.
4. Al finalizar la palabra, se marca el nodo final como `es_palabra = True`.

Esto permite que múltiples palabras compartan prefijos.

Ejemplo:

Palabras insertadas:

```
data
database
datos
```

Todas comparten el prefijo **"da"** dentro del Trie.

---

## Método `sugerir`

Este método devuelve palabras que comienzan con un **prefijo específico**.

```python
def sugerir(self, prefijo: str) -> Generator[str, None, None]:
```

Funcionamiento:

1. Primero se recorre el Trie hasta encontrar el nodo correspondiente al prefijo.
2. Luego se realiza una búsqueda en profundidad (**DFS**) para encontrar todas las palabras posibles que continúan desde ese nodo.
3. Cada palabra encontrada se devuelve usando `yield`.

Esto permite implementar un sistema de **autocompletado eficiente**.

---

## Uso de `yield`

El método `sugerir` utiliza **generadores** mediante la palabra clave `yield`.

Ejemplo:

```python
yield prefijo
```

`yield` permite devolver valores **uno por uno** en lugar de devolver toda la lista de resultados al mismo tiempo.

Ventajas de usar `yield`:

- Reduce el uso de memoria
- Permite trabajar con grandes cantidades de datos
- Genera resultados de manera progresiva

Por esta razón es útil en estructuras como **Tries**, donde puede haber muchas sugerencias posibles.

---

# Cómo ejecutar el programa

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta del ejercicio

```bash
cd ejercicio2_trie
```

### 3. Ejecutar las pruebas

```bash
python -m unittest tests/test_trie.py
```

Si las pruebas pasan correctamente, significa que la implementación del Trie funciona de manera adecuada.

Este código también puede ejecutarse sin problema en **Google Colab**, siempre que los archivos estén organizados correctamente.

---

# Análisis de complejidad Big-O

## Insertar palabra

Complejidad:

```
O(m)
```

Donde **m** es la longitud de la palabra.

Se recorre cada carácter una sola vez para insertarlo en el Trie.

---

## Buscar prefijo

Complejidad:

```
O(m)
```

Se recorre el Trie carácter por carácter hasta llegar al nodo que representa el prefijo.

---

## Generar sugerencias

Complejidad:

```
O(n)
```

Donde **n** es el número de nodos recorridos para generar todas las palabras posibles.

En el peor caso se deben recorrer todos los nodos descendientes del prefijo.

---

# Conclusión

El Trie es una estructura de datos eficiente para manejar colecciones de palabras y realizar búsquedas por prefijo.

Su uso permite implementar sistemas de autocompletado con una complejidad mucho menor que revisar todas las palabras de una lista.

Además, el uso de **generadores (`yield`)** mejora la eficiencia al producir resultados de forma progresiva y reducir el uso de memoria.
