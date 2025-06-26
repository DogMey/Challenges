from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])                  # Longitud de cada palabra
        word_count = len(words)                   # Cuántas palabras hay
        window_len = word_len * word_count        # Longitud total de la ventana
        word_freq = Counter(words)                # Frecuencia de palabras esperadas

        result = []

        # Solo necesitamos revisar cada posición inicial dentro del primer bloque de word_len
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    current_count[word] += 1

                    # Si se excede la cantidad esperada, movemos left para equilibrar
                    while current_count[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    # Si el tamaño de ventana actual coincide, guardamos el índice
                    if right - left == window_len:
                        result.append(left)
                else:
                    current_count.clear()
                    left = right

        return result

solution = Solution()
print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))