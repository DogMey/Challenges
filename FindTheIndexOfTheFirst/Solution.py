class Solution(object):
    def strStr(self, haystack, needle):
        # Si needle es una cadena vacía, retornamos 0
        if not needle:  
            return 0
        # Si haystack es vacío o needle es más largo que haystack, retornamos -1
        if not haystack or len(needle) > len(haystack): 
            return -1
        # Recorremos haystack y comparamos subcadenas de longitud len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            # Comparamos la subcadena de haystack con needle
            if haystack[i:i + len(needle)] == needle:   
                return i
        return -1
    
solucion = Solution()
haystack = "sadbutsad"
needle = "sad"
print(solucion.strStr(haystack, needle))