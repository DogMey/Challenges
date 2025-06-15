class Solution(object):
    def isPalindrome(self, s):
        caracteres_validos = []

        for c in s:
            if c.isalnum():                             # Verifica si es una letra o número
                minuscula = c.lower()                   # Convierte a minúscula
                caracteres_validos.append(minuscula)    # Lo agrega a la lista

        s = ''.join(caracteres_validos) # Une todos los caracteres en una sola cadena
        return s == s[::-1]             # Comparamos la cadena con su reverso
    
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))