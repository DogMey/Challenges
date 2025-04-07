# Problema:

Dado un arreglo de enteros `nums`, se desea rotar el arreglo hacia la derecha `k` pasos. Esto significa que cada elemento se moverá `k` posiciones a la derecha, y los elementos al final del arreglo se moverán al inicio.

# Solución:

Para este caso podemos simplificar la solución implementado el metodo "slicing", que consiste en dividir el arreglo en partes y luego unirlos. Esto funciona de la siguiente manera:

- `nums[-k:]`: Este caso toma los `k` ultimos elementos de `nums`, esto pues al negar `k` en python apuntamos de derecha a izquierda.
- `nums[:-k]`: Esto toma todos los elementos excepto los últimos `k` elementos.

Con esta lógica, podemos entonces partir el arreglo y luego juntarlo, esto sobreescribiendolo con la instrucción `nums[:]` modificando la lista original en lugar de crear una nueva.

Otro caso a resaltar es que implementamos un modulo, esto con el fin de si `k > len(nums)` Entonces no hacer una rotación innecesaria.