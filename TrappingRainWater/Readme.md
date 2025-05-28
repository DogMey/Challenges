# Atrapando Agua de Lluvia

Este proyecto contiene una solución eficiente para el problema clásico de "atrapar agua de lluvia". Dada una elevación en forma de un array de números enteros no negativos representando las alturas de los bloques, el objetivo es calcular cuánta agua de lluvia puede quedar atrapada después de llover.

## Lógica del Algoritmo

La solución se basa en el principio de que la cantidad de agua que puede ser atrapada en una posición `i` depende de la altura del bloque más alto a su izquierda y del bloque más alto a su derecha. El agua atrapada en esa posición es la diferencia entre el nivel de agua más bajo posible (determinado por el mínimo entre la altura máxima izquierda y la altura máxima derecha) y la altura del bloque actual.

El algoritmo procede en los siguientes pasos:

1.  **Pre-cálculo de Máximos Izquierdos**: Se construye una lista `left_max` donde `left_max[i]` almacena la altura máxima de un bloque desde el inicio de la lista hasta la posición `i` (inclusive). Esto se logra iterando de izquierda a derecha:
    ```python
    left_max[i] = max(left_max[i - 1], height[i])
    ```

2.  **Pre-cálculo de Máximos Derechos**: Similarmente, se construye una lista `right_max` donde `right_max[i]` almacena la altura máxima de un bloque desde el final de la lista hasta la posición `i` (inclusive). Esto se hace iterando de derecha a izquierda:
    ```python
    right_max[i] = max(right_max[i + 1], height[i])
    ```

3.  **Cálculo del Agua Atrapada**: Una vez que se tienen `left_max` y `right_max`, se itera por cada posición `i` en la lista de alturas. Para cada `i`, la cantidad de agua atrapada se calcula como:
    ```python
    min(left_max[i], right_max[i]) - height[i]
    ```
    Este valor se suma a un acumulador total.

## Complejidad

* **Complejidad Temporal (Time Complexity)**: $O(n)$
    El algoritmo realiza tres pasadas lineales sobre la lista de alturas: una para calcular `left_max`, otra para `right_max` y una final para sumar el agua atrapada. Cada pasada es directamente proporcional a la longitud de la lista `n`.

* **Complejidad Espacial (Space Complexity)**: $O(n)$
    Se utilizan dos listas adicionales (`left_max` y `right_max`), cada una del mismo tamaño que la lista de entrada `height`. Esto resulta en una complejidad espacial lineal con respecto a la longitud de la entrada.