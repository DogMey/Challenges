class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]    # Se inicia con el primer string como prefijo
        
        for s in strs[1:]:  # Comienza a comparar con los siguientes strings
            while not s.startswith(prefix): # Verifica si el string comienza con el prefijo actual
                prefix = prefix[:-1]        # Si no coincide, se acorta el prefijo 
                if not prefix:
                    return ""               # Si el prefijo se vuelve vacío, retorna vacío
        
        return prefix
    
solucion = Solution()
# Ejemplo de uso
cadenas = ["flower","flow","flight"]
print(solucion.longestCommonPrefix(cadenas))