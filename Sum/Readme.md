# 3Sum

## Descripción del Problema

Dado un arreglo de enteros `nums`, el objetivo es encontrar **todas las combinaciones únicas de tres números** cuya suma sea exactamente cero.

Cada combinación debe ser única, es decir, no se pueden incluir tuplas duplicadas en el resultado, aunque los mismos valores aparezcan en distintas posiciones del arreglo original.

## ¿Cómo se soluciona?

Este problema se resuelve eficientemente utilizando una combinación de ordenamiento y la técnica de **dos punteros**, lo cual reduce la complejidad respecto a una solución con triple bucle.

### Enfoque:

1. **Ordenar el arreglo**:
   - Se ordena el arreglo de menor a mayor para facilitar la búsqueda de combinaciones y evitar duplicados fácilmente.

2. **Recorrer el arreglo con un índice `i`**:
   - Se recorre el arreglo desde el índice `0` hasta `n-2` (donde `n` es la longitud del arreglo), ya que se necesitan al menos tres elementos para formar una tupla.

3. **Evitar duplicados en el primer número**:
   - Si el valor actual `nums[i]` es igual al anterior (`nums[i-1]`), se omite la iteración para evitar generar combinaciones repetidas.

4. **Inicializar dos punteros**:
   - Uno desde la posición siguiente a `i` (`left = i + 1`) y otro desde el final del arreglo (`right = n - 1`).

5. **Búsqueda con dos punteros**:
   - Se calcula la suma de los elementos en las posiciones `i`, `left` y `right`.
   - Si la suma es menor que cero, se incrementa `left` para aumentar la suma.
   - Si la suma es mayor que cero, se decrementa `right` para reducir la suma.
   - Si la suma es exactamente cero, se guarda la combinación como resultado válido.

6. **Evitar duplicados en `left` y `right`**:
   - Después de encontrar una tupla válida, se avanza `left` y se retrocede `right` mientras los valores siguientes sean iguales a los actuales, evitando así combinaciones repetidas.

7. **Continuar búsqueda**:
   - Después de manejar los duplicados, se continúa avanzando ambos punteros para seguir buscando otras combinaciones válidas con el mismo `i`.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n²)`  
  - El arreglo se ordena en `O(n log n)` y por cada elemento se realiza una búsqueda con dos punteros, lo cual toma `O(n)` en el peor caso. En total, la complejidad es `O(n²)`.

- **Complejidad Espacial:** `O(1)` adicional  
  - No se usan estructuras adicionales significativas aparte del arreglo de salida. El espacio usado para almacenar los resultados no cuenta como espacio adicional.