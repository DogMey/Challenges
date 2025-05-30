class Solution(object):
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]   # Lista de valores enteros correspondientes a los números romanos
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]   # Lista de símbolos romanos correspondientes a los valores enteros
        
        roman_numeral = ""  # Inicializa una cadena vacía para construir el número romano
        for i in range(len(val)):           # Itera sobre los índices de las listas val y syms
            while num >= val[i]:            # Mientras el número sea mayor o igual al valor actual
                roman_numeral += syms[i]    # Añade el símbolo romano correspondiente a la cadena
                num -= val[i]               # Resta el valor actual del número  
        
        return roman_numeral
    
solucion = Solution()

entero = 3749
print(solucion.romanToInt(entero))