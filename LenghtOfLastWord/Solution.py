class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()   # Elimina espacios al principio y al final de la cadena
        if not s:       # Si la cadena está vacía después de eliminar espacios, retorna 0
            return 0
        words = s.split(' ')    # Divide la cadena en palabras usando el espacio como separador
        last_word = words[-1]   # Obtiene la última palabra de la lista de palabras
        return len(last_word)   
solucion = Solution()
# Ejemplo de uso
cadena = "Hola mundo"
print(solucion.lengthOfLastWord(cadena))  # Debería imprimir 5, ya que "mundo" tiene 5 letras