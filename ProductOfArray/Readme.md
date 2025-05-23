# Producto Excepto Uno Mismo

Este repositorio contiene una solución en Python para el problema "Producto Excepto Uno Mismo". Dada una matriz de enteros `nums`, la tarea es devolver una matriz `output` tal que `output[i]` sea igual al producto de todos los elementos de `nums` excepto `nums[i]`.

## Descripción del Problema

El desafío consiste en calcular el producto de todos los elementos en una matriz *excepto* el elemento en el índice actual. Esto debe hacerse sin usar el operador de división y con una complejidad de tiempo de O(n).

Por ejemplo:
* Si `nums = [1, 2, 3, 4]`, la salida debería ser `[24, 12, 8, 6]`.
    * `output[0]` (para `1`) es `2 * 3 * 4 = 24`
    * `output[1]` (para `2`) es `1 * 3 * 4 = 12`
    * `output[2]` (para `3`) es `1 * 2 * 4 = 8`
    * `output[3]` (para `4`) es `1 * 2 * 3 = 6`

## Enfoque de la Solución

La solución emplea un enfoque de dos pasadas para lograr el resultado deseado sin usar la división.

1.  **Inicializar la Matriz de Salida:** Se crea una matriz `output` del mismo tamaño que la matriz de entrada `array`, inicializada con unos. Esta matriz almacenará nuestros productos finales.

2.  **Primera Pasada (Productos Izquierdos):**
    * Se itera a través de la `array` de izquierda a derecha.
    * Se mantiene una variable `prodIzquierda` (producto desde la izquierda), inicializada en 1.
    * Para cada elemento en el índice `i`, `output[i]` se establece con el `prodIzquierda` actual. Esto significa que `output[i]` contendrá el producto de todos los elementos *a la izquierda* de `array[i]`.
    * Luego, `prodIzquierda` se actualiza multiplicándolo por `array[i]` para la siguiente iteración.

3.  **Segunda Pasada (Productos Derechos):**
    * Se itera a través de la `array` de derecha a izquierda.
    * Se mantiene una variable `prodDerecha` (producto desde la derecha), inicializada en 1.
    * Para cada elemento en el índice `i`, se multiplica el valor actual en `output[i]` (que contiene el producto izquierdo) por `prodDerecha`. Esto incorpora el producto de todos los elementos *a la derecha* de `array[i]`.
    * Luego, `prodDerecha` se actualiza multiplicándolo por `array[i]` para la siguiente iteración.

Después de estas dos pasadas, `output[i]` contendrá el producto de todos los elementos excepto `array[i]`.