# Ejercicio 2 - Trie 

## Descripcion

Este ejercicio implementa un Trie para sugerir palabras a partir de un prefijo.

Cada nodo del Trie utiliza un diccionario para almacenar las aristas hacia los hijos.

## Como ejecutar

python -m unittest tests/test_trie.py

## Analisis de complejidad Big-O

Insertar palabra → O(m)

Buscar prefijo → O(m)

Generar sugerencias → O(n)
