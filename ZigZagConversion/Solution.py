class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):   # Si hay una sola fila o el número de filas es mayor o igual a la longitud de la cadena, no hay zigzag
            return s
        
        rows = [''] * numRows   # Crear una lista de cadenas para cada fila
        current_row = 0         # Fila actual
        going_down = False      # Indica si estamos bajando o subiendo en el zigzag
        
        for char in s:                              # Iterar sobre cada carácter en la cadena                                  
            rows[current_row] += char               # Añadir el carácter a la fila actual
            if current_row == 0:                    # Si estamos en la primera fila, cambiamos a bajar
                going_down = True           
            elif current_row == numRows - 1:        # Si estamos en la última fila, cambiamos a subir
                going_down = False
            current_row += 1 if going_down else -1  # Mover a la siguiente fila según la dirección
        
        return ''.join(rows)
    
solucion = Solution()
# Ejemplo de uso
s = "PAYPALISHIRING"
numRows = 3
print(solucion.convert(s, numRows))