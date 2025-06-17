# Two Sum II - Input Array Is Sorted

## Descripción del Problema

Se te da una lista ordenada de números enteros llamada `numbers` y un valor entero llamado `target`. Tu tarea es encontrar dos números en la lista cuya suma sea exactamente igual al valor `target`.

Debes devolver los **índices (1-indexed)** de los dos números que suman `target`. Se garantiza que **existe una única solución**, y no se puede usar el mismo elemento dos veces.

## ¿Cómo se soluciona?

Dado que el arreglo está ordenado de forma ascendente, se puede aplicar una técnica eficiente conocida como **two pointers** (dos punteros), evitando el uso de estructuras adicionales o bucles anidados.

### Enfoque:

1. **Inicializar dos punteros**:
   - Uno al inicio del arreglo (`left = 0`).
   - Otro al final del arreglo (`right = len(numbers) - 1`).

2. **Recorrer el arreglo**:
   - Mientras `left` sea menor que `right`, se calcula la suma de `numbers[left] + numbers[right]`.

3. **Comparar con el objetivo (`target`)**:
   - Si la suma es igual al objetivo, se retorna la pareja de índices `[left + 1, right + 1]` (ajustados a 1-indexed).
   - Si la suma es menor que el objetivo, se incrementa el puntero izquierdo (`left += 1`) para aumentar la suma.
   - Si la suma es mayor, se decrementa el puntero derecho (`right -= 1`) para reducir la suma.

4. **Garantía de solución única**:
   - Como está garantizado que existe una única solución válida, el ciclo siempre encontrará una respuesta sin necesidad de comprobar todas las combinaciones posibles.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n)`  
  Donde `n` es la longitud del arreglo `numbers`. Solo se realiza un recorrido desde ambos extremos hacia el centro, comparando sumas.

- **Complejidad Espacial:** `O(1)`  
  No se utilizan estructuras de datos adicionales; solo se emplean dos punteros.