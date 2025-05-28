# Reparto de Dulces

## Problema

Se nos presenta un problema donde $n$ niños están formados en una fila. A cada niño se le asigna una **calificación** numérica. Nuestro objetivo es distribuir la **cantidad mínima de dulces** posible, cumpliendo con dos reglas esenciales:

1.  Cada niño debe recibir **al menos un dulce**.
2.  Un niño con una **calificación superior** a la de su vecino (ya sea a la izquierda o a la derecha) debe recibir **más dulces** que ese vecino.

## Estrategia de Solución

La solución implementada aborda este problema mediante un proceso de dos pasadas, asegurando que ambas condiciones sean satisfechas de manera óptima:

1.  **Inicialización**: En el primer paso, a cada niño se le asigna **un dulce**. Esto cumple de inmediato con la regla de que todo niño debe tener al menos un dulce.

2.  **Primera Pasada (Izquierda a Derecha)**: Se recorre la fila de niños desde el segundo niño hasta el final. Si la **calificación actual** de un niño es mayor que la de su vecino izquierdo, el niño actual recibe **un dulce más** que su vecino izquierdo. Esta pasada garantiza que la condición de "más dulces que el vecino izquierdo" se mantenga a medida que avanzamos.

3.  **Segunda Pasada (Derecha a Izquierda)**: Luego, se realiza una segunda pasada, esta vez desde el penúltimo niño hacia el inicio de la fila. Si la **calificación actual** de un niño es mayor que la de su vecino derecho, se ajusta su cantidad de dulces. El número de dulces para el niño actual se establece como el **máximo** entre los dulces que ya posee (posiblemente asignados en la primera pasada) y la cantidad de dulces de su vecino derecho más uno. Este paso es crucial para satisfacer la condición de "más dulces que el vecino derecho" sin anular los ajustes previos.

4.  **Suma Final**: Finalmente, el total mínimo de dulces necesarios se obtiene sumando la cantidad de dulces asignados a cada niño después de ambas pasadas.

## Complejidad

* **Tiempo**: La solución tiene una **complejidad de tiempo de $O(N)$**, donde $N$ es el número de niños. Esto se debe a que realizamos dos recorridos lineales completos sobre la fila de niños.

* **Espacio**: La **complejidad de espacio es de $O(N)$**. Esto se debe al uso de un arreglo adicional para almacenar la cantidad de dulces de cada niño.