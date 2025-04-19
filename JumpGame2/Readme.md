# Problema:

Se le proporciona un array de enteros nums con índice 0 y longitud n. Inicialmente, se encuentra en `nums[0]`.

Cada elemento `nums[i]` representa la longitud máxima de un salto hacia adelante desde el índice i. En otras palabras, si se encuentra en `nums[i]`, puede saltar a cualquier `nums[i + j]` donde:

`0 <= j <= nums[i] e`
`i + j < n`

Devuelve el número mínimo de saltos para alcanzar `nums[n - 1]`. Los casos de prueba se generan de forma que pueda alcanzar `nums[n - 1]`.

# Solución:

Para solucionar este problema creamos 3 variables:

- jumps: Nos ayudara a contar la cantidad de saltos que se haran dentro del arreglo.
- current_end: Nos ayudara a definir el ultimo valor al que podemos llegar.
- farthest: Nos ayuda a definir el maximo valor al cual ir, de tal manera que escogemos el valor mayor para llegar mas rapido al final.

Inicializamos todas las variables en 0, y posteriormente empezamos a recorrer el arreglo, guardamos en `farthest` el valor maximo entre este y el valor en esa posición, de esta manera hallamos el valor maximo de pasos que podemos dar. Si la posicion en la que estamos es la ultima posición, osea `current_end` entonces sumamos 1 a `jump` y guardamos el valor maximo como la nueva ultima posición en la que estamos.

De esta manera seleccionamos el salto maximo siempre, esto asegura que lleguemos cada vez mas lejos en menos pasos. 