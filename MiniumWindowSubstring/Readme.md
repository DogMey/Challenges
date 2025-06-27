# Minimum Window Substring

## Descripción del Problema

Dados dos strings `s` y `t` de longitudes `m` y `n` respectivamente, devuelve la ventana mínima de `s` tal que cada carácter en `t` (incluyendo duplicados) esté incluido en la ventana. Si no existe tal subcadena, devuelve la cadena vacía `""`.

Los casos de prueba se generarán de tal manera que la respuesta sea única.

## Ejemplos

### Ejemplo 1:
- **Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`
- **Output:** `"BANC"`
- **Explicación:** La subcadena de ventana mínima "BANC" incluye 'A', 'B', y 'C' del string `t`.

### Ejemplo 2:
- **Input:** `s = "a"`, `t = "a"`
- **Output:** `"a"`
- **Explicación:** Todo el string `s` es la ventana mínima.

### Ejemplo 3:
- **Input:** `s = "a"`, `t = "aa"`
- **Output:** `""`
- **Explicación:** Ambos 'a's de `t` deben estar incluidos en la ventana. Como la ventana más grande de `s` solo tiene una 'a', devuelve cadena vacía.

## Solución

### Algoritmo de Ventana Deslizante (Sliding Window)

La solución utiliza el patrón de ventana deslizante con las siguientes características:

1. **Dos punteros:** `left` y `right` que definen la ventana actual
2. **Contadores:** Para rastrear los caracteres requeridos y los caracteres en la ventana actual
3. **Expansión:** Expandir la ventana hacia la derecha hasta que contenga todos los caracteres de `t`
4. **Contracción:** Contraer la ventana desde la izquierda para encontrar la ventana mínima

### Complejidad

- **Tiempo:** O(n + m) donde n es la longitud de `s` y m es la longitud de `t`
- **Espacio:** O(k) donde k es el número de caracteres únicos en `t`

### Pasos del Algoritmo

1. **Inicialización:**
   - Crear un diccionario `target_count` con el conteo de cada carácter en `t`
   - Inicializar variables para la ventana deslizante

2. **Expansión de la ventana:**
   - Mover el puntero `right` hacia la derecha
   - Actualizar el conteo de caracteres en la ventana actual
   - Verificar si se han completado todos los requerimientos

3. **Contracción de la ventana:**
   - Mover el puntero `left` hacia la derecha mientras se mantengan todos los requerimientos
   - Actualizar la ventana mínima si es necesario

4. **Resultado:**
   - Retornar la subcadena mínima encontrada o cadena vacía si no existe

## Casos Especiales

- **Strings vacíos:** Si `s` o `t` están vacíos, retornar `""`
- **Caracteres duplicados:** El algoritmo maneja correctamente caracteres duplicados en `t`
- **Sin solución:** Si no se puede encontrar una ventana válida, retornar `""`

## Ejecución

Para ejecutar la solución:

```bash
python Solution.py
```

Esto ejecutará todos los ejemplos de prueba incluidos en el código. 