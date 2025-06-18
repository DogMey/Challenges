# Container With Most Water

## Descripción del Problema

Dado un arreglo de enteros `height`, donde cada elemento representa la altura de una línea vertical en el eje X, se desea encontrar dos líneas que, junto con el eje X, formen un **contenedor que almacene la mayor cantidad posible de agua**.

El área del agua almacenada se calcula como el mínimo entre las dos alturas multiplicado por la distancia entre sus posiciones.

El objetivo es devolver el **área máxima** que se puede obtener con dos de estas líneas.

## ¿Cómo se soluciona?

El problema se resuelve eficientemente utilizando la técnica de **dos punteros** (`two pointers`). Esta técnica permite evitar el uso de bucles anidados, lo que reduce considerablemente la complejidad temporal.

### Enfoque:

1. **Inicialización**:
   - Se colocan dos punteros: uno al inicio (`left = 0`) y otro al final del arreglo (`right = len(height) - 1`).
   - Se define una variable `max_area` para almacenar el valor máximo encontrado.

2. **Recorrido**:
   - Mientras los punteros no se crucen (`left < right`), se calcula el área formada entre las dos líneas actuales:
     - **Anchura**: la distancia entre los punteros (`right - left`).
     - **Altura**: el valor mínimo entre las dos alturas (`min(height[left], height[right])`).
     - **Área**: producto de anchura por altura.

3. **Actualización**:
   - Si el área calculada es mayor que el valor almacenado en `max_area`, se actualiza.

4. **Movimiento de punteros**:
   - Para intentar encontrar un contenedor más alto, se mueve el puntero que apunta a la **menor altura**:
     - Si `height[left] < height[right]`, se incrementa `left`.
     - De lo contrario, se decrementa `right`.

5. **Resultado**:
   - Al finalizar el bucle, `max_area` contendrá el valor del área máxima posible entre dos líneas.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n)`  
  Solo se recorre el arreglo una vez desde ambos extremos, moviendo los punteros en cada paso.

- **Complejidad Espacial:** `O(1)`  
  No se utilizan estructuras de datos adicionales, únicamente variables auxiliares.