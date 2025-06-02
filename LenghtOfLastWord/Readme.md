# Length of Last Word

## Descripción del Problema

Se te proporciona una cadena de caracteres `s` que contiene palabras y espacios. Una **palabra** se define como cualquier secuencia de caracteres no vacía que no contiene espacios.

Tu objetivo es devolver la **longitud de la última palabra** de la cadena. Si no existe ninguna palabra (es decir, si la cadena solo contiene espacios), el resultado debe ser `0`.

## ¿Cómo se soluciona?

La solución al problema sigue estos pasos:

1. **Eliminar espacios al inicio y final**  
   Primero, se eliminan los espacios en blanco que puedan estar al principio o al final de la cadena. Esto es importante para evitar considerar "palabras vacías" si hay espacios al final.

2. **Verificar si la cadena quedó vacía**  
   Si después de quitar los espacios la cadena resulta estar vacía, se retorna `0`, ya que no hay ninguna palabra válida.

3. **Dividir la cadena en palabras**  
   Luego, se divide la cadena en una lista de palabras utilizando el espacio como delimitador. Esta operación separa todas las palabras contenidas en la cadena.

4. **Obtener la última palabra**  
   Una vez que tenemos la lista de palabras, simplemente se toma la última de ellas.

5. **Contar la longitud de la última palabra**  
   Finalmente, se cuenta cuántos caracteres tiene la última palabra y se retorna ese valor como resultado.

## ⏱️ Complejidad Computacional

- **Complejidad Temporal:** `O(n)`  
  Donde `n` es la longitud de la cadena `s`. Esto se debe a que se recorren todos los caracteres de la cadena al hacer el `strip()` y el `split()`.

- **Complejidad Espacial:** `O(n)`  
  Ya que la operación `split()` puede crear una lista de palabras que ocupa memoria proporcional al número de caracteres en la cadena original.

## Consideraciones

- El problema incluye casos especiales como cadenas vacías o cadenas con múltiples espacios consecutivos.
- Es una excelente práctica para manipulación de strings y manejo de bordes en entradas.