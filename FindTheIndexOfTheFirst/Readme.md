# Búsqueda de Subcadena (Implementación de strStr)

## Descripción del Problema

Dado un string `haystack` y otro string `needle`, el objetivo es encontrar la primera aparición del string `needle` dentro de `haystack`. Si `needle` no está presente, se debe retornar `-1`. Si `needle` está vacío, se retorna `0` por convención.

Este problema se asemeja a la función `strStr()` de muchos lenguajes de programación, incluyendo C y Java.

## Solución Propuesta

La solución implementa una búsqueda directa, sin usar funciones incorporadas como `.find()`. Primero se realizan comprobaciones rápidas para casos base: si `needle` es vacío o más largo que `haystack`. Luego se recorre el string `haystack` y se comparan subcadenas del mismo tamaño que `needle`.

Dentro del ciclo `for`, se recorta una subcadena de `haystack` de longitud igual a `needle`, comenzando en la posición actual `i`, y se compara con `needle`. Si son iguales, se ha encontrado la primera coincidencia, y se retorna el índice `i`. Si se recorre todo el string sin encontrar coincidencias, se retorna `-1`.

## Complejidad de la Solución

- **Complejidad Temporal:** `O(n * m)`  
  Donde `n` es la longitud de `haystack` y `m` es la longitud de `needle`. En el peor caso, cada subcadena de tamaño `m` en `haystack` se compara completamente con `needle`.

- **Complejidad Espacial:** `O(1)`  
  No se utilizan estructuras de datos adicionales; la comparación se hace en el mismo espacio.