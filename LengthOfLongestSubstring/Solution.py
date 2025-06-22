class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()    # Se inicializa un conjunto para almacenar caracteres únicos
        left = 0            # Puntero izquierdo para la ventana deslizante
        max_length = 0      # Longitud máxima de la subcadena sin repetir
        for right in range(len(s)):     # Puntero derecho para la ventana deslizante
            while s[right] in char_set: # Si el carácter ya está en el conjunto
                char_set.remove(s[left])    # Elimina el carácter del conjunto y mueve el puntero izquierdo
                left += 1
            char_set.add(s[right])   # Agrega el nuevo carácter al conjunto
            max_length = max(max_length, right - left + 1)  # Actualiza la longitud máxima si es necesario        
        return max_length
    
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))  # Debería imprimir 3, ya que "abc" es la subcadena más larga sin repetir caracteres