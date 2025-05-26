class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)  # Obtener el número de estaciones

        # Inicializamos las variables
        total_deficit = 0               # Almacena el déficit total de gasolina (gas - cost) en todo el circuito
        estacion_inicio_candidata = 0   # Índice de la estación desde la que estamos intentando iniciar el viaje
        tanque_actual = 0               # Almacena la cantidad de gasolina en el tanque si empezamos en la estacion_inicio_candidata actual

        # Iteramos a través de todas las estaciones
        for i in range(n):
            ganancia_neta = gas[i] - cost[i]    # Calculamos la ganancia o pérdida neta de gasolina en la estación actual
            tanque_actual += ganancia_neta      # Sumamos la ganancia neta al tanque actual
            total_deficit += ganancia_neta      # Sumamos la ganancia neta al déficit total. Esto nos ayuda a verificar al final

            if tanque_actual < 0:   # Si el tanque actual se vuelve negativo, significa que no podemos llegar a la estación (i+1)
                tanque_actual = 0   # Reiniciamos el tanque actual a 0, porque si empezamos en una nueva estación, comenzaremos con el tanque vacío.
                estacion_inicio_candidata = i + 1   # La nueva estación de inicio candidata será la siguiente estación (i + 1).

        # Después de recorrer todas las estaciones, verificamos el 'total_deficit'.
        if total_deficit >= 0:
            return estacion_inicio_candidata
        else:
            return -1
        
solucion = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(solucion.canCompleteCircuit(gas, cost))