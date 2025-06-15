class Solution(object):
    def isSubsequence(self, s, t):
        if not s:   # Si s es una cadena vacía, siempre es subsecuencia de t
            return True
        if not t:   # Si t es una cadena vacía y s no lo es, s no puede ser subsecuencia de t
            return False
        s_index, t_index = 0, 0 # Inicializamos los índices para s y t
        while s_index < len(s) and t_index < len(t):    # Recorremos ambas cadenas
            if s[s_index] == t[t_index]:    # Si los caracteres coinciden
                s_index += 1                # Avanzamos en s
            t_index += 1                    # Siempre avanzamos en t, ya que queremos encontrar todos los caracteres de s en t
        return s_index == len(s)            # Si hemos recorrido todos los caracteres de s, es subsecuencia de t
solution = Solution()
s = "abc"
t = "ahbgdc"
print(solution.isSubsequence(s, t))