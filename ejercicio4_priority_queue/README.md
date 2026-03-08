# Ejercicio 4 - Planificador de Tareas (Priority Queue)

## Descripcion

Este ejercicio implementa una **cola de prioridad** para simular el comportamiento de un planificador de tareas similar al que podria usar un **kernel de sistema operativo**.

Una cola de prioridad permite procesar elementos segun su nivel de prioridad. En lugar de seguir un orden de llegada como una cola normal (FIFO), los elementos con **mayor prioridad se procesan primero**.

Para implementar esta estructura se utiliza el modulo **heapq** de Python, que implementa un **monticulo minimo (min-heap)**.

---

# Explicacion del codigo

## Clase `Tarea`

La clase `Tarea` representa un proceso o trabajo que debe ser ejecutado por el planificador.

Cada tarea contiene los siguientes atributos:

- `prioridad`: nivel de prioridad de la tarea
- `timestamp`: momento en el que la tarea fue creada o agregada
- `descripcion`: texto que describe la tarea

Ejemplo de creacion de una tarea:

```python
t = Tarea(1, 10, "proceso_A")
```

---

## Metodo `__lt__` (less than)

El modulo **heapq** necesita comparar objetos para mantener el orden del monticulo.

Para permitir esto se sobrecarga el operador **menor que (`<`)** mediante el metodo magico `__lt__`.

```python
def __lt__(self, otra: "Tarea") -> bool:
```

La comparacion funciona asi:

1. Primero se compara la **prioridad**.
2. Si dos tareas tienen la misma prioridad, se usa el **timestamp**.

Esto garantiza que:

- las tareas con mayor prioridad se ejecuten primero
- si dos tareas tienen la misma prioridad, se ejecute primero la mas antigua

---

# Clase `Planificador`

La clase `Planificador` administra la cola de prioridad.

Internamente utiliza una lista que funciona como **heap**.

```python
self.cola = []
```

---

## Metodo `agregar`

Este metodo inserta una nueva tarea en la cola de prioridad.

```python
heapq.heappush(self.cola, tarea)
```

El heap reorganiza automaticamente los elementos para mantener el orden correcto.

---

## Metodo `ejecutar`

Este metodo obtiene y elimina la tarea con mayor prioridad.

```python
heapq.heappop(self.cola)
```

El elemento extraido sera siempre el de mayor prioridad segun la logica definida en `__lt__`.

---

## Metodo `vacio`

Este metodo permite verificar si la cola esta vacia.

```python
len(self.cola) == 0
```

---

# Como ejecutar el programa

1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

2. Entrar a la carpeta del ejercicio

```bash
cd ej4_planificador
```

3. Ejecutar las pruebas

```bash
python -m unittest tests/test_planificador.py
```

Si las pruebas pasan correctamente, significa que el planificador funciona de manera adecuada.

---

# Analisis de complejidad Big-O

Las operaciones del heap tienen las siguientes complejidades:

## Insercion de tarea

```
O(log n)
```

Esto ocurre porque el heap debe reorganizar sus elementos para mantener la propiedad del monticulo.

---

## Extraccion de tarea

```
O(log n)
```

Cuando se elimina el elemento de mayor prioridad, el heap debe reordenarse.

---

## Acceso al elemento minimo

```
O(1)
```

El elemento con mayor prioridad siempre se encuentra en la raiz del heap.

---

# Conclusion

Las colas de prioridad son una estructura fundamental en sistemas operativos y algoritmos de planificacion.

El uso de **heaps** permite manejar prioridades de manera eficiente con complejidad logaritmica para inserciones y eliminaciones.

La sobrecarga del operador `__lt__` permite que el modulo `heapq` ordene automaticamente objetos personalizados como las instancias de la clase `Tarea`.
