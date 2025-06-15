class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())    # Convertimos la cadena a minúsculas y filtramos solo caracteres alfanuméricos
        return s == s[::-1]                                 # Comparamos la cadena con su reverso
    
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))