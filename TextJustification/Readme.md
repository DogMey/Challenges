# `fullJustify` Explicación de Conceptos Básicos

Este documento explica el funcionamiento del código `fullJustify`, una función diseñada para justificar texto, asegurando que cada línea tenga un ancho específico y que los espacios se distribuyan de manera uniforme.

## Variables Fundamentales

El corazón del algoritmo reside en unas pocas variables clave que rastrean el estado actual del proceso de justificación:

* **`res` (Resultado Final):** Una lista vacía al inicio, donde se almacenará cada línea de texto una vez que haya sido completamente justificada y formateada. Es el contenedor de la salida del programa.
* **`cur_words` (Palabras de la Línea Actual):** Una lista temporal que guarda las palabras que se están considerando para la línea que se está construyendo en un momento dado. A medida que se itera sobre las palabras de entrada, estas se añaden aquí hasta que la línea esté lista para ser justificada.
* **`cur_length` (Longitud de Palabras Actual):** Un contador que lleva la suma de las longitudes de todas las palabras actualmente en `cur_words`. Es importante destacar que esta variable solo cuenta la longitud de las palabras en sí, no los espacios que las separan.

## Proceso de Cálculo de Palabras por Línea

La lógica para determinar cuántas palabras entran en una línea se basa en una evaluación continua a medida que se procesa cada palabra de entrada:

1.  **Evaluación de Aptitud:** Para cada `word` individual de la lista de entrada, el algoritmo verifica si esta palabra puede ser añadida a la `cur_words` sin exceder el **`maxWidth`** (ancho máximo permitido para la línea).
2.  **Cálculo de Longitud Potencial:** Esta verificación se realiza sumando:
    * La **`cur_length`** actual (longitud de las palabras ya en `cur_words`).
    * La longitud de la `word` que se desea añadir (**`len(word)`**).
    * El **número mínimo de espacios requeridos** entre las palabras ya existentes en `cur_words` y la nueva palabra. Este número es simplemente la cantidad de palabras en `cur_words` (**`len(cur_words)`**), ya que se necesitará al menos un espacio entre cada par de palabras.
3.  **Decisión de Línea Completa:** Si la suma total excede el **`maxWidth`**, se considera que la `cur_words` actual contiene todas las palabras que pueden caber en esa línea. En ese momento, se procede a justificar y formatear esta línea. Después de la justificación, las variables `cur_words` y `cur_length` se reinician para comenzar a construir la siguiente línea.
4.  **Adición a la Línea Actual:** Si la palabra cabe, simplemente se añade a `cur_words` y `cur_length` se actualiza con su longitud.

## Agregando Espacios entre Palabras

La distribución de espacios es crucial para la justificación y se maneja de manera diferente para las líneas intermedias que para la última línea.

### Líneas Intermedias (Completamente Justificadas)

Para las líneas que no son la última, los espacios se distribuyen de la siguiente manera:

1.  **Cálculo de Espacios Necesarios:** Se determina cuántos espacios adicionales se necesitan para que la línea alcance exactamente **`maxWidth`**. Esto se calcula como `maxWidth - cur_length`.
2.  **Identificación de Huecos:** Se cuentan los "huecos" entre las palabras. Si hay `N` palabras en `cur_words`, hay `N - 1` huecos donde se pueden insertar espacios. Si solo hay una palabra, no hay huecos, y los espacios se añaden al final de esa palabra.
3.  **Distribución Equitativa:** Los espacios adicionales se distribuyen cíclicamente entre los huecos. Esto significa que si hay más espacios que huecos, los primeros huecos recibirán un espacio extra antes de que la distribución comience de nuevo desde el primer hueco. Este proceso asegura una apariencia lo más uniforme posible.

### Última Línea

La última línea de texto sigue una regla diferente para la justificación:

1.  **Espacio Simple:** Las palabras de la última línea se unen simplemente con un único espacio entre cada una.
2.  **Alineación a la Izquierda:** La línea resultante se alinea a la izquierda y se rellena con espacios en blanco al final hasta que su longitud total sea **`maxWidth`**. No se distribuyen espacios adicionales entre las palabras como en las líneas intermedias.

## Complejidad del Código

### Complejidad Temporal (Time Complexity):

La complejidad temporal del algoritmo es **O(N)**, donde **`N`** es el número total de caracteres en todas las palabras de entrada combinadas.

* El algoritmo itera a través de cada palabra una vez.
* Dentro del bucle, las operaciones como añadir palabras a `cur_words` o actualizar `cur_length` toman tiempo constante.
* La parte más "costosa" es la distribución de espacios. Sin embargo, el número total de espacios a distribuir a lo largo de todas las líneas es directamente proporcional al número total de caracteres y al **`maxWidth`**. Cada espacio se añade a una palabra una vez.
* Unir las palabras para formar una línea (`''.join(cur_words)`) toma un tiempo proporcional a la longitud de la línea, pero dado que cada carácter solo se procesa una vez a lo largo de todas las líneas, la complejidad general se mantiene lineal con respecto al número total de caracteres de entrada.

### Complejidad Espacial (Space Complexity):

La complejidad espacial del algoritmo es **O(M)**, donde **`M`** es el número total de caracteres en la salida justificada.

* Esto se debe a que `res` almacenará todas las líneas de texto justificadas. En el peor de los casos, la salida puede tener una longitud similar a la entrada si las palabras son muy pequeñas y se necesita mucho relleno, o incluso puede ser el número de caracteres de la entrada si no se requiere mucho relleno.
* `cur_words` y `cur_length` utilizan espacio que depende del **`maxWidth`**, es decir, la longitud de una sola línea, lo cual es constante en relación con la entrada total.

En resumen, el algoritmo es eficiente en términos de tiempo y espacio, procesando los datos de manera lineal con respecto a su tamaño.