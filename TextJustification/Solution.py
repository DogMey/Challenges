class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []        # Inicializa la lista de resultados
        cur_words = []  # Lista para almacenar las palabras de la línea actual
        cur_length = 0  # Longitud actual de las palabras en la línea

        for word in words:  # Itera sobre cada palabra en la lista de palabras
            if cur_length + len(word) + len(cur_words) > maxWidth:  # Verifica si agregar la palabra excede el ancho máximo
                for i in range(maxWidth - cur_length):              # Distribuye los espacios en la línea actual
                    cur_words[i % (len(cur_words) - 1 or 1)] += ' ' # Agrega los espacios necesarios
                res.append(''.join(cur_words))                      # Agrega la línea justificada a los resultados
                cur_words = []                                      # Reinicia las variables para la siguiente línea
                cur_length = 0                                      # Reinicia la longitud actual            
            cur_words.append(word)      # Agrega la palabra actual a la línea
            cur_length += len(word)     # Actualiza la longitud actual

        res.append(' '.join(cur_words).ljust(maxWidth)) # Agrega la última línea justificada, rellenando con espacios a la derecha
        return res
    
solucion = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."] 
maxWidth = 16

print(solucion.fullJustify(words, maxWidth))