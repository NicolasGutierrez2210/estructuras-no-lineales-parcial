# Ejercicio 3 - Registro de Estudiantes (Hash Table)

## Descripcion

Este ejercicio implementa una **Hash Table** desde cero para gestionar un registro de estudiantes usando sus **IDs como claves**.

Las **tablas hash** permiten almacenar y recuperar datos de forma muy eficiente mediante una funcion hash que transforma una clave en un indice dentro de una estructura de almacenamiento.

En este caso, la tabla hash se utiliza para almacenar pares **(id, estudiante)**.

---

# Explicacion del codigo

## Clase `HashTable`

La clase `HashTable` representa una tabla hash implementada desde cero.

La estructura interna utiliza **listas**, ya que el ejercicio no permite usar el **diccionario (`dict`) de Python** para la logica interna.

```python
self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(size)]
```

Cada posicion de la tabla contiene una **lista de pares `(key, value)`**, lo que permite manejar colisiones.

---

## Funcion Hash

La funcion hash transforma una clave en un indice dentro de la tabla.

```python
def _hash(self, key: Any) -> int:
    return hash(key) % self.size
```

Esto asegura que el indice siempre este dentro del tamaño de la tabla.

---

## Metodo `insert`

Este metodo permite insertar un nuevo registro en la tabla.

```python
def insert(self, key: Any, value: Any) -> None:
```

Funcionamiento:

1. Se calcula el indice usando la funcion hash.
2. Se revisa si la clave ya existe en la lista.
3. Si existe, se actualiza el valor.
4. Si no existe, se agrega el nuevo par `(key, value)`.

---

## Metodo `get`

Este metodo permite obtener un valor asociado a una clave.

```python
def get(self, key: Any) -> Any:
```

Funcionamiento:

1. Se calcula el indice mediante la funcion hash.
2. Se recorre la lista en esa posicion.
3. Si se encuentra la clave, se devuelve su valor.

---

## Metodo `delete`

Este metodo elimina un registro de la tabla hash.

```python
def delete(self, key: Any) -> bool:
```

Si la clave existe, el elemento se elimina de la lista correspondiente.

---

# Manejo de colisiones

Una **colision** ocurre cuando dos claves diferentes producen el mismo indice en la tabla hash.

Para resolver esto se utiliza la tecnica de **encadenamiento (chaining)**.

Esto significa que cada posicion de la tabla contiene una lista de elementos.

Ejemplo conceptual:

```
Indice 0 -> []
Indice 1 -> [(101, "Juan"), (201, "Maria")]
Indice 2 -> []
Indice 3 -> [(301, "Carlos")]
```

Si dos claves producen el mismo indice, ambas se almacenan en la misma lista.

---

# Metodo magico `__setitem__`

El ejercicio requiere implementar el metodo magico:

```python
def __setitem__(self, key, value)
```

Esto permite usar la sintaxis de Python:

```python
tabla[id] = estudiante
```

Ejemplo:

```python
tabla = HashTable()

tabla[1001] = "Juan"
tabla[1002] = "Maria"
```

Internamente, este metodo llama al metodo `insert`.

---

# Metodo magico `__getitem__` (Bonus)

Tambien se implemento el metodo:

```python
def __getitem__(self, key)
```

Esto permite acceder a los valores usando:

```python
print(tabla[1001])
```

---

# Como ejecutar el programa

1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

2. Entrar a la carpeta del ejercicio

```bash
cd ejercicio3_hash_table
```

3. Ejecutar las pruebas

```bash
python -m unittest tests/test_hash_table.py
```

Si las pruebas pasan correctamente, significa que la implementacion funciona de manera adecuada.

---

# Analisis de complejidad Big-O

## Insercion

Complejidad promedio:

```
O(1)
```

La funcion hash permite acceder directamente a una posicion de la tabla.

En el peor caso (muchas colisiones):

```
O(n)
```

---

## Busqueda

Complejidad promedio:

```
O(1)
```

Se accede directamente al indice calculado.

Peor caso:

```
O(n)
```

Si todos los elementos estan en la misma lista debido a colisiones.

---

## Eliminacion

Complejidad promedio:

```
O(1)
```

Peor caso:

```
O(n)
```

Cuando se debe recorrer toda la lista en una posicion de la tabla.

---

# Conclusion

Las **tablas hash** son una de las estructuras de datos mas eficientes para almacenar y recuperar informacion.

Su rendimiento promedio es **O(1)** para insercion, busqueda y eliminacion.

El manejo de **colisiones mediante encadenamiento** permite que la estructura funcione correctamente incluso cuando varias claves generan el mismo indice.
