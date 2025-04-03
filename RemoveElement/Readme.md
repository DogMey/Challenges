# Problema:

Dado un array de enteros `nums` y un entero `val`, elimine todas las ocurrencias de `val` en `nums` in situ. El orden de los elementos puede modificarse. Luego, devuelva el número de elementos en `nums` que no sean iguales a `val`.

Considere `k` como el número de elementos en `nums` que no sean iguales a `val`. Para que se acepte, debe hacer lo siguiente:

- Modifique el array `nums` de modo que los primeros `k` elementos de `nums` contengan los elementos que no sean iguales a `val`. Los elementos restantes de `nums`, así como el tamaño de `nums`, no sean importantes.
- Devuelva `k`.

# Solución:

Dado que no necesitamos cambiar el tamaño del array ni eliminar elementos podemos dar una solución sencilla; esta solución consiste en recorrer el arreglo y guardar el valor unicamente cuando en esa posición el valor es distinto a `val`, además de que se aumenta un contador `k` que nos indicara entonces cuantos valores tienen `nums`.