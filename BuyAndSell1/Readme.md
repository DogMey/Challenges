# Problema:

Se le proporciona una matriz de precios, donde `precios[i]` representa el precio de una acción dada en el i-ésimo día.

Desea maximizar sus ganancias eligiendo un solo día para comprar una acción y un día diferente en el futuro para venderla.

Devuelva el beneficio máximo que puede obtener de esta transacción. Si no obtiene ningún beneficio, devuelva 0.

# Solución:

Para este caso definimos 2 variables, `minPrecio` para guardar el valor al que se compra y que inicializamos con el primer valor del arreglo, tambien creamos `maxBeneficio` que será la diferencia entre el precio al que compramos y al que vendemos, este sera inicializado en 0.

Recorremos el arreglo y vamos guardando en `minPrecio` el menor valor que encontremos, mientras también comparamos si la diferencia entre el precio de la bolsa ese día y el precio de compra nos genera un beneficio mayor al que tenemos, de ser así lo guardamos.

De esta manera respetamos la logica de primero comprar para poder vender, y además retornamos 0 si no encontramos un beneficio; pues inicializamos `maxBeneficio=0`.