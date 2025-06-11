class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []        # Inicializa la lista de resultados
        cur_words = []  # Lista para almacenar las palabras de la línea actual
        cur_length = 0  # Longitud actual de las palabras en la línea

        for word in words:  # Itera sobre cada palabra en la lista de palabras
            if cur_length + len(word) + len(cur_words) > maxWidth:  # Verifica si agregar la palabra excede el ancho máximo
                for i in range(maxWidth - cur_length):
                    cur_words[i % (len(cur_words) - 1 or 1)] += ' '
                res.append(''.join(cur_words))
                cur_words = []
                cur_length = 0
            cur_words.append(word)
            cur_length += len(word)

        res.append(' '.join(cur_words).ljust(maxWidth))
        return res