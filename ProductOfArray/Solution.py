class Solution(object):
    def productExceptSelf(self, array):

        if len(array) == 0:
            return []
        
        output = [1] * len(array)

        print(array)
        prodIzquierda = 1
        for i in range(len(array)):
            output[i] = prodIzquierda
            prodIzquierda *= array[i]
            print(output, "Estamos en", array[i], "posicion", i)
        
        print(array)
        
        prodDerecha = 1
        for i in range(len(array) - 1, -1, -1):
            output[i] *= prodDerecha
            prodDerecha *= array[i]
            print(output, "Estamos en", array[i], "posicion", i)

        return output
    
solucion = Solution()

nums=[-1,1,0,-3,3]
print(solucion.productExceptSelf(nums))