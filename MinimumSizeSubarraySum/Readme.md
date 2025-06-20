# Minimum Size Subarray Sum

## Descripción del Problema

Dado un arreglo de enteros positivos `nums` y un entero `target`, se busca encontrar la **longitud mínima de una subarray continua** cuya suma sea mayor o igual a `target`. Si no existe tal subarray, se debe retornar `0`.

## ¿Cómo se soluciona?

La solución eficiente utiliza la técnica conocida como **ventana deslizante (sliding window)**, ideal para trabajar con subarreglos continuos dentro de un arreglo.

### Enfoque con Ventana Deslizante:

1. **Inicialización**:
   - Se define una variable `left` como el límite izquierdo de la ventana.
   - Se inicializan `current_sum` como la suma actual de la ventana y `min_length` como infinito (para ir registrando el mínimo encontrado).

2. **Expansión de la ventana**:
   - Se recorre el arreglo con un puntero `right` que representa el límite derecho de la ventana.
   - En cada iteración, se suma el elemento `nums[right]` al `current_sum`.

3. **Contracción de la ventana**:
   - Cuando `current_sum` es **mayor o igual al objetivo (`target`)**, significa que la ventana actual es una solución válida.
   - Se actualiza el valor mínimo de longitud `min_length`.
   - Luego, se intenta reducir el tamaño de la ventana desde la izquierda (incrementando `left`) mientras siga cumpliendo la condición, con el fin de encontrar una ventana más pequeña que aún sume al menos `target`.

4. **Resultado final**:
   - Si se ha encontrado al menos una subarray válida, se devuelve `min_length`.
   - Si no, se retorna `0`.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n)`  
  Cada elemento del arreglo se visita como máximo dos veces (una al expandir la ventana y otra al contraerla), lo que da una complejidad lineal.

- **Complejidad Espacial:** `O(1)`  
  No se utilizan estructuras auxiliares que dependan del tamaño del input, solo variables para punteros y sumas.

## Consideraciones

- La técnica de ventana deslizante es altamente eficiente para trabajar con secuencias continuas.
- Solo funciona correctamente cuando todos los elementos del arreglo son positivos, ya que garantiza que al mover el puntero izquierdo la suma total disminuirá.
- Este enfoque permite encontrar soluciones óptimas en tiempo lineal para problemas que involucran subarrays o secuencias contiguas bajo una condición específica.

