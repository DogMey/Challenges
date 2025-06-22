# Longest Substring Without Repeating Characters

## Descripción del Problema

Dada una cadena de caracteres `s`, se desea encontrar la **longitud de la subcadena más larga que no contenga caracteres repetidos**. La subcadena debe estar compuesta por caracteres **contiguos** y no puede haber duplicados.

## ¿Cómo se soluciona?

Para resolver este problema de forma eficiente, se utiliza la técnica de **ventana deslizante** (sliding window) en combinación con un **conjunto (set)** que ayuda a controlar los caracteres únicos dentro de la ventana.

### Enfoque con Ventana Deslizante y Conjunto:

1. **Inicialización**:
   - Se usa un conjunto `char_set` para almacenar los caracteres únicos que están actualmente en la ventana.
   - Se definen dos punteros: `left` (inicio de la ventana) y `right` (fin de la ventana, controlado por el ciclo).
   - Se define `max_length` para llevar el registro de la longitud máxima encontrada.

2. **Recorrido con puntero derecho (`right`)**:
   - Se recorre la cadena carácter por carácter.
   - Si el carácter actual `s[right]` ya está en el conjunto (es repetido), se elimina el carácter `s[left]` del conjunto y se incrementa `left` hasta que el duplicado se elimine de la ventana.

3. **Actualización del conjunto y longitud**:
   - Se agrega `s[right]` al conjunto ya que ahora es único dentro de la ventana.
   - Se calcula la longitud actual de la ventana (`right - left + 1`) y se actualiza `max_length` si es mayor que el valor actual.

4. **Resultado**:
   - Al finalizar el recorrido, se retorna el valor máximo encontrado, que representa la longitud de la subcadena más larga sin caracteres repetidos.

## Complejidad Computacional

- **Complejidad Temporal:** `O(n)`  
  Cada carácter se procesa como máximo dos veces (una al expandir la ventana y otra al contraerla), lo que garantiza eficiencia lineal.

- **Complejidad Espacial:** `O(k)`  
  Donde `k` es el tamaño del alfabeto (número de caracteres distintos). En el peor caso, el conjunto puede contener hasta todos los caracteres únicos de `s`.