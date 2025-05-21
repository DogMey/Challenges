# Descripción del Problema

El problema de `RandomizedSet` nos pide implementar una estructura de datos que se comporte como un conjunto (set), pero con la particularidad de que todas sus operaciones principales (`insertar`, `eliminar` y `obtener un elemento aleatorio`) deben ejecutarse en un **tiempo promedio de O(1)** (tiempo constante).

Las operaciones específicas son:

* **`insert(val)`**: Añade `val` al conjunto si no está presente. Retorna `True` si se añadió, `False` si ya existía.
* **`remove(val)`**: Elimina `val` del conjunto si está presente. Retorna `True` si se eliminó, `False` si no existía.
* **`getRandom()`**: Retorna un elemento aleatorio del conjunto. Se garantiza que siempre habrá al menos un elemento cuando se llama a esta función.

La dificultad radica en que una sola estructura de datos no suele satisfacer las necesidades de O(1) para todas estas operaciones simultáneamente. Por ejemplo, un *hash set* permite inserciones y eliminaciones rápidas, pero no un acceso aleatorio indexado. Una *lista* permite acceso aleatorio por índice, pero la eliminación en una posición arbitraria puede ser O(N).

## Solución y Enfoque

Para lograr la complejidad de tiempo promedio de O(1) en todas las operaciones, la solución emplea una combinación de **dos estructuras de datos**:

1.  **Un diccionario (hash map)**: En Python, esto es un `dict`. Lo usaremos para almacenar la relación entre el **valor** y su **índice** actual dentro de la lista.
    * **Propósito**: Permite verificar la existencia de un valor y encontrar su posición en la lista en O(1) promedio.
    * **Implementación**: `self.valIndex = {valor: indice_en_lista}`

2.  **Una lista (arreglo dinámico)**: En Python, esto es un `list`. Lo usaremos para almacenar los **valores** mismos.
    * **Propósito**: Permite añadir elementos al final en O(1) y acceder a cualquier elemento por su índice en O(1). Es crucial para la operación `getRandom()`.
    * **Implementación**: `self.elements = [valor1, valor2, ...]`

### Cómo funcionan juntas:

#### `insert(val)`

1.  Verificamos si `val` ya está en `self.valIndex`. Si lo está, retornamos `False`.
2.  Si no está, lo añadimos al final de `self.elements`.
3.  Registramos la posición de `val` en `self.valIndex` (su índice actual es `len(self.elements) - 1`).
4.  Retornamos `True`.

**Complejidad**: O(1) promedio, gracias a las propiedades del diccionario y la adición al final de la lista.

#### `remove(val)`

Esta es la operación más ingeniosa para mantener la complejidad O(1):

1.  Verificamos si `val` está en `self.valIndex`. Si no lo está, retornamos `False`.
2.  Obtenemos el `indexRemove` de `val` desde `self.valIndex`.
3.  Obtenemos el `lastElement` de `self.elements`.
4.  **Intercambiamos**: Movemos el `lastElement` a la posición de `indexRemove` en `self.elements`. Esto "llena" el hueco sin tener que desplazar todos los elementos subsiguientes, lo que sería O(N).
5.  **Actualizamos el diccionario**: Dado que `lastElement` ahora está en una nueva posición (`indexRemove`), actualizamos su entrada en `self.valIndex` para que apunte a `indexRemove`.
6.  **Eliminamos el último elemento**: Usamos `self.elements.pop()`. Esta operación es O(1) ya que siempre elimina el elemento al final de la lista.
7.  Finalmente, eliminamos `val` de `self.valIndex`.
8.  Retornamos `True`.

**Complejidad**: O(1) promedio, ya que todas las operaciones involucradas (acceso a diccionario, asignación de lista, `pop` al final) son de tiempo constante en promedio.

#### `getRandom()`

1.  Generamos un `random_index` utilizando `random.randint(0, len(self.elements) - 1)`.
2.  Retornamos el elemento en `self.elements[random_index]`.

**Complejidad**: O(1), ya que acceder a un elemento de una lista por su índice es una operación de tiempo constante.

### ¿Por qué `self.valIndex` es crucial?

En nuestra `RandomizedSet`, `self.valIndex` es un diccionario que mapea `valor -> índice`. Esta es la clave para la eficiencia:

* Cuando necesitamos eliminar un `val`, el diccionario nos dice inmediatamente **dónde** está ese `val` en `self.elements` (su índice). Si tuviéramos que buscar el `val` en la lista, sería O(N), lo que arruinaría nuestra meta de O(1).
* Al tener este mapeo directo, podemos realizar el "intercambio con el último elemento" en O(1) promedio y luego eliminarlo del final de la lista, manteniendo así la eficiencia requerida para todas las operaciones.