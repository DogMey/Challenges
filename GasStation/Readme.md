# Problema de la Gasolinera

Este repositorio contiene una solución en Python para el problema de la "Gasolinera".

## Descripción del Problema

Imagina una ruta circular con `n` gasolineras. En cada gasolinera `i`, recibes `gas[i]` unidades de combustible, y viajar de la gasolinera `i` a la `i+1` cuesta `cost[i]` unidades de combustible. Empezando con el tanque vacío en una de las estaciones, tu objetivo es encontrar el **índice único de la estación de inicio** que te permita completar un círculo completo en sentido horario. Si no existe tal estación, devuelve `-1`.

## Solución

La solución para este problema es ingeniosa y eficiente, basándose en la idea de que si la cantidad total de gasolina disponible en todas las estaciones es suficiente para cubrir el costo total de viajar por todo el circuito, entonces **siempre hay una solución única**. Si no es así, no hay manera de completar el circuito.

Nuestro algoritmo trabaja en una sola pasada, con un enfoque "codicioso" (greedy) para encontrar la estación de inicio. Mantenemos dos variables clave durante la iteración:

1.  **`tanque_actual`**: Esta variable simula la cantidad de gasolina que tenemos en el tanque **asumiendo que empezamos en nuestra `estacion_inicio_candidata` actual**. A medida que avanzamos de una estación a la siguiente, sumamos la gasolina que obtenemos (`gas[i]`) y restamos el costo de viajar (`cost[i]`).

2.  **`total_deficit`**: Esta variable acumula la **diferencia neta entre la gasolina disponible y la gasolina necesaria** a lo largo de *todo* el circuito. Suma `(gas[i] - cost[i])` en cada paso. Al final del recorrido, si `total_deficit` es **menor que cero**, significa que no hay suficiente gasolina en todo el sistema para completar el circuito, y debemos devolver `-1`. Si es **mayor o igual a cero**, sabemos que existe una solución.

### ¿Por qué reiniciar `tanque_actual` y avanzar `estacion_inicio_candidata`?

La parte más crucial del algoritmo ocurre cuando `tanque_actual` se vuelve **negativo**.

* **`if tanque_actual < 0:`**: Si nuestro `tanque_actual` cae por debajo de cero en la estación `i`, significa que **no podemos llegar a la siguiente estación (i+1) si hubiéramos comenzado en la `estacion_inicio_candidata` actual**. Nos quedamos sin combustible en el camino.

* **`tanque_actual = 0`**: Como esa `estacion_inicio_candidata` ya no es válida, la "descartamos" y volvemos a empezar con un tanque vacío para la próxima posible estación de inicio.

* **`estacion_inicio_candidata = i + 1`**: Esta es la clave de la eficiencia. Si fallamos en la estación `i` (es decir, no pudimos llegar a `i+1`), entonces **cualquier estación desde nuestra `estacion_inicio_candidata` anterior hasta la estación `i` (inclusive) tampoco puede ser el punto de partida**. Si hubiéramos iniciado en cualquiera de esas estaciones, el resultado habría sido el mismo: nos habríamos quedado sin gasolina antes o en la estación `i`. Por lo tanto, la próxima posible estación de inicio debe ser **`i + 1`**. Al hacer esto, evitamos verificar puntos de partida que sabemos de antemano que no funcionarán.