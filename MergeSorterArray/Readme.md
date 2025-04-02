# Problema:

Se le proporcionan dos matrices de enteros, `nums1` y `nums2`, ordenadas de forma no decreciente, y dos enteros, `m` y `n`, que representan el número de elementos en `nums1` y `nums2`, respectivamente.

Fusione `nums1` y `nums2` en una única matriz ordenada de forma no decreciente.

La función no debe devolver la matriz ordenada final, sino que debe almacenarse dentro de la matriz `nums1`. Para ello, nums1 tiene una longitud de `m` + `n`, donde los primeros `m` elementos representan los elementos que deben fusionarse y los últimos `n` elementos se establecen en 0 y deben ignorarse. nums2 tiene una longitud de `n`.

# Solución:

Para abstraer mejor el problema se cambio el nombre de los indices, siendo entonces `m=tamañoNums1` y `n=tamañoNums2`. Posterior a esto vamos a realizar el analisis del problema.

Notamos que no debemos crear un nuevo arreglo y que nos simplifican el caso dejando el espacio del segundo arreglo inicializado en 0. Podemos entonces ahcer 2 cosas, fusionar los 2 arreglos y luego simplemente usar un metodo para ordenar de menor a mayor, o podemos tambien implementar una logica mas profunda.

Esta solución implementa 3 indices, uno que es para el primer arreglo (Sin contar con el espacio extra que se nos proporciona para el segundo arreglo), otro para el segundo arreglo y un tercero para el tamaño completo de los 2 arreglos "fusionados".

Luego, vamos a trabajar sobre el primer arreglo pero comparandolo desde su ultima posicion con el segundo arreglo.

- Realizamos un while, cuya condicion cierra cuando `indiceNum2 >= 0`, de esta manera aseguramos que solo vamos a comparar respecto al segundo arreglo, que es el que agregamos.

- Comparamos si aun estamos dentro del primer arreglo y si la posicion en la que apuntan nuestros indices individuales nos indican que `nums1[indiceNum1]>nums2[indiceNum2]`; de ser así guardamos el valor que apuntamos en `nums1` en la ultima posición del mismo y restamos 1 a `indiceNum1`, pues este valor ya lo hemos procesado.

- De lo contrario, seguimos la misma logica pero para el otro arreglo; entonces guardamos el valor del segundo arreglo y restamos 1 a su indice.

- Cuando terminamos la comparacion le restamos 1 al indice del arreglo completo para continuar con la posición anterior; y así sucesivamente.

Como podemos notar, la gracia de este algoritmo es comparar en las posiciones y jugar con los indices para pasar una sola vez por el segundo arreglo.