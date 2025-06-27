class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Encuentra la ventana mínima de s que contiene todos los caracteres de t.
        
        Args:
            s: String principal
            t: String cuyos caracteres deben estar en la ventana
            
        Returns:
            La subcadena mínima que contiene todos los caracteres de t, o "" si no existe
        """
        if not s or not t:
            return ""
        
        # Diccionario para contar caracteres en t
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        
        # Variables para la ventana deslizante
        left = 0
        min_left = 0
        min_len = float('inf')
        required_chars = len(target_count)
        formed_chars = 0
        window_count = {}
        
        for right in range(len(s)):
            char = s[right]
            
            # Actualizar conteo en la ventana actual
            window_count[char] = window_count.get(char, 0) + 1
            
            # Verificar si este carácter completa un requerimiento
            if char in target_count and window_count[char] == target_count[char]:
                formed_chars += 1
            
            # Intentar contraer la ventana desde la izquierda
            while left <= right and formed_chars == required_chars:
                char_left = s[left]
                
                # Actualizar la ventana mínima si es necesario
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remover el carácter de la izquierda
                window_count[char_left] -= 1
                
                # Verificar si perdimos un carácter requerido
                if char_left in target_count and window_count[char_left] < target_count[char_left]:
                    formed_chars -= 1
                
                left += 1
        
        # Retornar la subcadena mínima o cadena vacía si no se encontró
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""


# Ejemplos de prueba
if __name__ == "__main__":
    solution = Solution()
    
    # Ejemplo 1
    print("Ejemplo 1:")
    print(f"Input: s = 'ADOBECODEBANC', t = 'ABC'")
    result = solution.minWindow("ADOBECODEBANC", "ABC")
    print(f"Output: '{result}'")
    print(f"Esperado: 'BANC'")
    print()
    
    # Ejemplo 2
    print("Ejemplo 2:")
    print(f"Input: s = 'a', t = 'a'")
    result = solution.minWindow("a", "a")
    print(f"Output: '{result}'")
    print(f"Esperado: 'a'")
    print()
    
    # Ejemplo 3
    print("Ejemplo 3:")
    print(f"Input: s = 'a', t = 'aa'")
    result = solution.minWindow("a", "aa")
    print(f"Output: '{result}'")
    print(f"Esperado: ''")
    print()
    
    # Casos adicionales de prueba
    print("Casos adicionales:")
    
    # Caso 4: Múltiples ocurrencias
    result = solution.minWindow("ADOBECODEBANC", "AABC")
    print(f"s='ADOBECODEBANC', t='AABC' -> '{result}'")
    
    # Caso 5: Caracteres repetidos en t
    result = solution.minWindow("aa", "aa")
    print(f"s='aa', t='aa' -> '{result}'")
    
    # Caso 6: String vacío
    result = solution.minWindow("", "ABC")
    print(f"s='', t='ABC' -> '{result}'")
        