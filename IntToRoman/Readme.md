# Conversión de Entero a Número Romano

Este proyecto contiene una solución para el problema clásico de convertir un número entero dado a su representación en números romanos.

## 📝 Problema

El sistema de numeración romano utiliza siete símbolos principales:

* **I**: 1
* **V**: 5
* **X**: 10
* **L**: 50
* **C**: 100
* **D**: 500
* **M**: 1000

Una particularidad fundamental de este sistema son las **combinaciones sustractivas**. Esto significa que ciertos números se forman restando un valor más pequeño de uno más grande. Por ejemplo:

* **IV** (4): 5 - 1
* **IX** (9): 10 - 1
* **XL** (40): 50 - 10
* **XC** (90): 100 - 10
* **CD** (400): 500 - 100
* **CM** (900): 1000 - 100

El objetivo es desarrollar un algoritmo que, dado un número entero (por ejemplo, `3749`), pueda convertirlo correctamente a su equivalente en números romanos (`MMMDCCXLIX`), respetando todas estas reglas y combinaciones.

## 💡 Solución

La solución implementada utiliza un enfoque **"greedy" (codicioso)**. Este método se basa en la idea de que, en cada paso, se busca restar el valor romano más grande posible del número entero de entrada, de forma repetitiva, hasta que el número se reduzca a cero.

### ¿Cómo funciona?

1.  **Tablas de Correspondencia**: Se definen dos listas paralelas:
    * `val`: Contiene los valores enteros correspondientes a los números romanos, ordenados de **mayor a menor** (ej., `[1000, 900, 500, 400, ..., 1]`). Es crucial que los valores especiales como `900 (CM)` o `40 (XL)` estén incluidos y en el orden correcto.
    * `syms`: Contiene los símbolos romanos asociados a los valores de `val`, manteniendo la misma correspondencia posicional (ej., `["M", "CM", "D", "CD", ..., "I"]`).

2.  **Iteración Codiciosa**: El algoritmo itera a través de estas listas de valores y símbolos. Para cada par `(valor, simbolo)`:
    * Comprueba si el número entero actual es mayor o igual al `valor` en la lista `val`.
    * Si lo es, significa que podemos usar ese símbolo romano. Se añade el `simbolo` a una cadena que construirá el resultado final y se resta el `valor` del número entero.
    * Este proceso se repite (bucle `while`) para el mismo `valor` y `simbolo` hasta que el número entero sea menor que dicho `valor`.
    * Una vez que el número es menor, el algoritmo pasa al siguiente par `(valor, simbolo)` en las listas y continúa el proceso hasta que el número entero se convierta en cero.