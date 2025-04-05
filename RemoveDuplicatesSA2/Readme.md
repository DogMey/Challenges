# Problema:

Dado un array de enteros `nums` ordenado en orden no decreciente, elimine algunos duplicados in situ de modo que cada elemento único aparezca como máximo dos veces. El orden relativo de los elementos debe mantenerse igual.

Dado que es imposible cambiar la longitud del array en algunos lenguajes, el resultado debe colocarse en la primera parte del array `nums`. De forma más formal, si hay `k` elementos después de eliminar los duplicados, entonces los primeros `k` elementos de `nums` deben contener el resultado final. No importa qué elementos se dejen después de los primeros `k` elementos.

Devuelva `k` después de colocar el resultado final en las primeras `k` ranuras de `nums`.

No asigne espacio adicional para otro array. Debe hacerlo modificando el array de entrada in situ con `O(1)` memoria adicional.

# Solución:

Para este caso, podemos implementar una solución distinta a la anterior; pues anteriormente trabajamos con el arreglo revisando hacia adelante si el valor era igual. Para este caso en cambio, trabajaremos con las posiciones dentro de `nums` revisando hacia atras, pues entonces guardaremos en `k`.

Por lo mismo, recorremos el arreglo apuntando en `i`, y guardando en `k`, aumentando en `k` unicamente cuando se repite un valor maximo 2 veces, esto lo logramos con el condicional `nums[k-2] != nums[i]`, ademas evitamos evaluar los valores en los 2 primeros espacios de memoria, pues no es necesario.