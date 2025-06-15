# Is Subsequence

## Descripción del Problema

Dadas dos cadenas de texto `s` y `t`, determinar si `s` es una **subsecuencia** de `t`.

Una **subsecuencia** de una cadena es una nueva cadena generada a partir de la original eliminando algunos (o ningún) carácter sin cambiar el orden relativo de los caracteres restantes.

## ¿Cómo se soluciona?

El enfoque para resolver este problema consiste en realizar un recorrido secuencial de ambas cadenas usando dos punteros o índices:

1. **Verificación inicial**:
   - Si `s` está vacía, se considera automáticamente una subsecuencia de cualquier cadena, incluso una vacía.
   - Si `t` está vacía y `s` no lo está, entonces `s` no puede ser una subsecuencia.

2. **Uso de dos índices**:
   - Se inicializan dos índices: uno para la cadena `s` (`s_index`) y otro para la cadena `t` (`t_index`).
   - Ambos comienzan en la posición cero.

3. **Recorrido controlado**:
   - Se recorre la cadena `t` mientras no se haya llegado al final de `s`.
   - Si el carácter actual de `s` coincide con el de `t`, se avanza el índice de `s`, indicando que se ha encontrado el siguiente carácter deseado.
   - Independientemente de si hubo coincidencia o no, se avanza el índice de `t`.

4. **Determinación del resultado**:
   - Al finalizar el recorrido, si `s_index` ha alcanzado la longitud de `s`, significa que todos los caracteres de `s` fueron encontrados en orden dentro de `t`.
   - En ese caso, se retorna `True`. De lo contrario, se retorna `False`.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n)`, donde `n` es la longitud de la cadena `t`.  
  Se recorre como máximo una vez la cadena `t`, comparando con caracteres de `s`.

- **Complejidad Espacial:** `O(1)`  
  No se utilizan estructuras auxiliares que crezcan con la entrada, solo variables para los índices.
