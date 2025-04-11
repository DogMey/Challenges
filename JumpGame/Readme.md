# Problema:

Se le proporciona un array de enteros `nums`. Inicialmente, se le posiciona en el primer índice del array, y cada elemento del array representa su longitud máxima de salto en esa posición.

Devuelve `True` si puede alcanzar el último índice, o `False` en caso contrario.

# Solución:

En este caso, la primera solución sería realizar los saltos que dice la posición hasta llegar a una inconsistencia. Sin embargo, esto desencadena muchas operaciones para evaluar los distintos casos. Por lo tanto necesitamos otra perspectiva diferente.

Para dar una solución mas completa, definimos un estilo de acumulaciones, en la que iremos cambiando el valor de la posicion en la que estamos con el valor maximo de movimientos que podemos hacer, esto guardando el maximo entre la posición actual con la anterior (restandole 1 para que tenga en cuenta el caso de haber llegado hasta el actual).

De esta manera acumulamos los valores maximos, lo que nos indica la maxima capacidad de saltos sin necesidad de usar una variable mas para gastar memoria. A su vez, comparamos el caso de si no tenemos mas acumulaciones para devolver `false`; si caso contrario llega hasta el final del arreglo logicamente retornamos `True`.