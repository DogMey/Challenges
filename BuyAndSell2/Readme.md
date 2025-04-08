# Problema:

Se le proporciona una matriz de enteros `prices`, donde `prices[i]` representa el precio de una acción dada en el i-ésimo día.

Cada día, puede decidir comprar o vender la acción. Solo puede tener como máximo una acción a la vez. Sin embargo, puede comprarla y luego venderla inmediatamente ese mismo día.

Calcule y devuelva la máxima ganancia posible.

# Solución:

Esta solución a diferencia de la primera solución, cambia en que compra y vende siempre y cuando haya un beneficio. No buscamos el maximo dentro de todos ni el minimo para comprar.

Esto lo definimos con el condicional `prices[i]-buy)>0` que se acciona siempre y cuando haya un beneficio. Aquí reiniciamos el precio de compra para seguri analizando el arreglo y encontrar otro precio de compra bueno.

De esta manera sumamos todas las compras, logrando así encontrar la maxima ganancia posible.