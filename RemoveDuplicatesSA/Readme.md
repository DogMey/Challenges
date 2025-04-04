# Problema:

Dado un array de enteros `nums` ordenado en orden no decreciente, elimine los duplicados de forma que cada elemento único aparezca solo una vez. El orden relativo de los elementos debe mantenerse igual. A continuación, devuelva el número de elementos únicos en `nums`.

Considere `k` como el número de elementos únicos de `nums`. Para que se acepte, debe hacer lo siguiente:

- Modifique el array `nums` de forma que los primeros `k` elementos de `nums` contengan los elementos únicos en el orden inicial en que estaban presentes. Los elementos restantes de `nums`, así como su tamaño, no sean tan importantes.
Devuelva `k`.
- Devuelva `k`.

# Solución:

Dado que no necesitamos cambiar el tamaño del array ni eliminar elementos, además de que nos entregan el arreglo en orden ascendente, podemos dar una solución sencilla; esta solución consiste en guardar valores dentro del arreglo siempre y cuando su número siguiente sea distinto, de ser igual entonces se avanza en el arreglo sin guardar datos.

Esto lo logramos usando 2 punteros dentro del arreglo, `i` se encarga de recorrer el arreglo, mientras que `k` se encarga de las posiciones en las que se guardara, aumentando unicamente cuando si se guarde un valor; de esta manera lo podemos usar igualmente como contador para lo que solicita el problema sumandole 1.