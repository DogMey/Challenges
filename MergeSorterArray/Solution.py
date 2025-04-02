class Solution(object):
    def merge(self, nums1, tamañoNums1, nums2, tamañoNums2):
        indiceNum1 = tamañoNums1 - 1 
        indiceNum2 = tamañoNums2 - 1
        indiceUltimo = tamañoNums1 + tamañoNums2 - 1
        while indiceNum2 >= 0:
            print(nums1)  
            print(nums2)
            print("indiceNum1:", indiceNum1, "valorNum1:", nums1[indiceNum1] , "indiceNum2:", indiceNum2, "valorNum2:", nums2[indiceNum2],"indiceUltimo:", indiceUltimo)
            if indiceNum1 >= 0 and nums1[indiceNum1] > nums2[indiceNum2]:    
                print("Primer caso")
                nums1[indiceUltimo] = nums1[indiceNum1]  
                indiceNum1 -= 1
            else:  
                print("Segundo caso")
                nums1[indiceUltimo] = nums2[indiceNum2]  
                indiceNum2 -= 1
            print("nums1 resultante:",nums1) # Imprime el resultado intermedio
            indiceUltimo -= 1
        
# Crear una instancia de la clase Solution
solucion = Solution()

# Definir los arreglos de entrada
nums1 = [1, 2, 3, 0, 0, 0]
tamañoNums1 = 3
nums2 = [2, 5, 6]
tamañoNums2 = 3

# Llamar a la función merge
solucion.merge(nums1, tamañoNums1, nums2, tamañoNums2)