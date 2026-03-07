# Ejercicio 1 - Estructura Organizacional (Arbol N-ario)

## Descripcion

Este ejercicio implementa una estructura organizacional universitaria
utilizando un arbol N-ario en Python.

La jerarquia se representa de la siguiente forma:

Rectoria → Facultades → Programas

Cada nodo puede tener multiples hijos. Los hijos se almacenan en un
diccionario para permitir acceso rapido por nombre.

La clase principal utilizada es `OrganizacionNode`.

---

# Explicacion del codigo

## Clase OrganizacionNode

Esta clase representa un nodo dentro del arbol organizacional.

Cada nodo contiene dos atributos principales:

- `nombre`: nombre del nodo dentro de la organizacion.
- `hijos`: diccionario que almacena los nodos hijos.

Ejemplo en el codigo:

```python
self.nombre: str = nombre
self.hijos: Dict[str, OrganizacionNode] = {}
