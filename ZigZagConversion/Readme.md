# Conversión de Cadena en Zigzag

## Descripción del Problema

Dada una cadena `s` y un número entero `numRows`, el objetivo es reordenar los caracteres de la cadena siguiendo un patrón en forma de "zigzag" sobre un número de filas determinado, y luego leer línea por línea para construir una nueva cadena. Esta transformación es útil en ciertos formatos de visualización y se ha vuelto popular en desafíos de programación.

## Solución Propuesta

La solución recorre cada carácter de la cadena original y lo coloca en la fila correspondiente según el patrón de zigzag. Se utiliza una dirección de recorrido (hacia abajo o hacia arriba) que se ajusta dinámicamente. Finalmente, las filas se concatenan para formar la cadena transformada.

## Complejidad de la Solución

- **Complejidad Temporal:** `O(n)`  
  Donde `n` es la longitud de la cadena de entrada. Cada carácter se procesa una única vez.

- **Complejidad Espacial:** `O(n)`  
  Se utiliza espacio adicional para almacenar los caracteres distribuidos por fila antes de combinarlos en la salida final.
