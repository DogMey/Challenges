class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {    # Se crea un diccionario para mapear los caracteres romanos a sus valores enteros
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0       # Inicializa el total a 0
        prev_value = 0  # Valor del carácter romano anterior, inicializado a 0
        
        for char in s:  # Itera sobre cada carácter en la cadena de entrada
            current_value = roman_to_int[char]              # Obtiene el valor entero del carácter romano actual
            if current_value > prev_value:                  # Si el valor actual es mayor que el anterior, significa que se está restando
                total += current_value - 2 * prev_value     # Se resta el valor anterior dos veces porque ya se sumó una vez antes
            else:
                total += current_value                      # Si no, simplemente se suma el valor actual al total   
            prev_value = current_value                      # Actualiza el valor del carácter anterior para la próxima iteración
            
        return total
    
solucion = Solution()

romanos = "MCMXCIV"
print(solucion.romanToInt(romanos))