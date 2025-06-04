# Invertir el Orden de Palabras en una Cadena

## Descripción del Problema

Dada una cadena que contiene palabras separadas por espacios, el objetivo es invertir el orden de las palabras sin alterar el contenido de cada palabra. Además, se deben eliminar los espacios innecesarios al principio, al final y entre las palabras (es decir, evitar múltiples espacios consecutivos).

Este problema es común en aplicaciones de procesamiento de texto, limpieza de datos y edición de contenido.

## Solución Propuesta

La solución se basa en los siguientes pasos:

1. Elimina los espacios en blanco al inicio y al final de la cadena.
2. Divide la cadena en una lista de palabras usando espacios como separador.
3. Invierte el orden de las palabras.
4. Une nuevamente las palabras con un único espacio entre cada una.

Esta técnica permite obtener una salida limpia y correctamente ordenada, sin espacios extra ni desalineaciones.

## Complejidad de la Solución

- **Complejidad Temporal:** `O(n)`  
  Donde `n` es la longitud de la cadena de entrada. Cada operación principal (eliminar espacios, dividir, invertir y unir) se realiza en tiempo lineal.

- **Complejidad Espacial:** `O(n)`  
  Se utiliza espacio adicional proporcional al número de caracteres, ya que se crea una lista intermedia de palabras y una nueva cadena como resultado final.