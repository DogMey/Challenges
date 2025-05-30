# Conversión de Números Romanos a Enteros

Este proyecto resuelve el problema de convertir un número romano (representado como una cadena de caracteres) a su valor entero correspondiente. Utiliza una clase en Python llamada `Solution` que implementa la lógica mediante un diccionario de mapeo y una iteración inteligente sobre los caracteres de entrada.

## Problema

Dado un número romano, conviértelo a un número entero. Los números romanos se representan con las siguientes combinaciones de letras:

| Símbolo | Valor |
|---------|-------|
| I       | 1     |
| V       | 5     |
| X       | 10    |
| L       | 50    |
| C       | 100   |
| D       | 500   |
| M       | 1000  |

Los números romanos se leen de izquierda a derecha, y en algunos casos, se resta el valor si un número menor aparece antes que uno mayor (por ejemplo, `IV` es 4, porque `I` está antes que `V`).

## 💡 Solución

El algoritmo implementado sigue los siguientes pasos:

1. Se define un diccionario para mapear los caracteres romanos a sus valores enteros.
2. Se inicializa un contador (`total`) en 0 y una variable (`prev_value`) para almacenar el valor del carácter anterior.
3. Se recorre la cadena carácter por carácter:
   - Si el valor actual es mayor que el anterior, se resta dos veces el valor anterior (ya que se sumó antes y ahora se necesita restar su valor).
   - Si no, se suma el valor actual al total.
4. Se devuelve el total acumulado.