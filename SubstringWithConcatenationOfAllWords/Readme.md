# Substring with Concatenation of All Words

## Descripción del Problema

Se te da una cadena de caracteres `s` y una lista de palabras `words`, todas de la misma longitud. El objetivo es encontrar todos los **índices de inicio** en `s` donde una concatenación exacta de todas las palabras en `words` aparece **sin ningún carácter adicional entre ellas**.

Cada palabra en `words` debe aparecer **una sola vez** y en **cualquier orden**.

## ¿Cómo se soluciona?

Este problema se resuelve usando una combinación de técnicas de **ventana deslizante**, **hashmaps** y **particionamiento por bloques** basado en la longitud de las palabras.

### Enfoque paso a paso:

1. **Inicialización**:
   - `word_len`: longitud de cada palabra (todas tienen el mismo tamaño).
   - `word_count`: cantidad de palabras en la lista.
   - `window_len`: longitud total esperada de la subcadena válida (es decir, `word_len * word_count`).
   - `word_freq`: un diccionario que almacena la frecuencia esperada de cada palabra.

2. **Recorrido por desplazamiento (offset)**:
   - Se recorre la cadena desde distintos **desplazamientos iniciales** (`i` de `0` a `word_len - 1`) para capturar todas las posibles alineaciones válidas de palabras consecutivas.

3. **Ventana deslizante por bloques**:
   - Se utilizan dos punteros `left` y `right` para definir una ventana móvil.
   - En cada iteración, se toma un bloque de `word_len` caracteres y se verifica si pertenece a `word_freq`.

4. **Manejo de frecuencias**:
   - Si la palabra es válida, se actuala un `current_count` (contador actual de palabras vistas).
   - Si se supera la frecuencia esperada para alguna palabra, se mueve `left` para equilibrar la ventana, descartando palabras al inicio.

5. **Verificación de ventana completa**:
   - Si el tamaño de la ventana (`right - left`) coincide con `window_len` y las frecuencias están balanceadas, se guarda el índice `left` como resultado válido.

6. **Reinicio en caso de palabra inválida**:
   - Si se encuentra una palabra que no pertenece a `word_freq`, se reinicia el contador y se mueve el puntero `left` justo después de `right`.


## Complejidad Computacional

- **Complejidad Temporal:** `O(n * k)`  
  Donde `n` es la longitud de la cadena `s` y `k` es la longitud de cada palabra. Aunque hay múltiples bucles anidados, se procesan bloques de tamaño fijo por desplazamiento, lo que mantiene la eficiencia razonable.

- **Complejidad Espacial:** `O(m)`  
  Donde `m` es el número de palabras. Se requiere espacio adicional para los contadores (`word_freq` y `current_count`).

## Consideraciones

- Todas las palabras tienen la misma longitud, lo cual es clave para aplicar este enfoque de bloques.
- El algoritmo es robusto ante entradas grandes siempre que el número de palabras y su longitud no crezcan excesivamente.
- Este problema es una aplicación avanzada de la técnica de **ventana deslizante optimizada**, útil en casos donde hay múltiples coincidencias que deben respetar estructura y conteo