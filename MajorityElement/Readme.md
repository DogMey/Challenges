# Problema:

Dado un array nums de tamaño `n`, devuelve el elemento mayoritario.

El elemento mayoritario es el que aparece más de `⌊n/2⌋` veces. Se puede asumir que el elemento mayoritario siempre existe en el array.

# Solución

Por la naturaleza del problema podemos definir que si ordenamos el arreglo y nos ubicamos a la mitad del arreglo estaremos apúntando al elemento mayorista; esto pues, como la condicion es que exista este elemento y además que este esté en mas de la mitad del mismo nos facilita la solución.