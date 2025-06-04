class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split()       # Dividir la cadena en palabras y eliminar espacios al inicio y al final
        reversed_words = words[::-1]    # Invertir el orden de las palabras
                
        return ' '.join(reversed_words) # Unir las palabras invertidas con un espacio
    
solucion = Solution()
# Ejemplo de uso
s = "the sky is blue"
print(solucion.reverseWords(s))