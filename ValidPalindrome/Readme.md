# Verificación de Palíndromos

## Descripción del Problema

El objetivo es determinar si una cadena de texto es un palíndromo, considerando únicamente caracteres alfanuméricos y sin tener en cuenta las diferencias entre mayúsculas y minúsculas. Una cadena es un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda una vez normalizada.

Este tipo de validación es común en procesamiento de texto, validación de entradas y algoritmos clásicos de entrevistas técnicas.

## Solución Propuesta

La solución normaliza la cadena original aplicando dos transformaciones clave:
1. Se convierte cada carácter a minúscula.
2. Se eliminan todos los caracteres que no son letras ni números.

Luego, se compara la cadena resultante con su reverso. Si ambas coinciden, la cadena es un palíndromo y se retorna `True`; de lo contrario, se retorna `False`.

Esta solución es directa y aprovecha operaciones eficientes de manipulación de cadenas en Python.

## Complejidad de la Solución

- **Complejidad Temporal:** `O(n)`  
  Donde `n` es la longitud de la cadena de entrada. Cada carácter se recorre una sola vez para filtrar y transformar, y luego se hace una comparación de longitud lineal.

- **Complejidad Espacial:** `O(n)`  
  Se crea una nueva cadena filtrada y normalizada, además de su reverso para la comparación.