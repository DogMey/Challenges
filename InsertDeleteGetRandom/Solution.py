import random

class RandomizedSet(object):

    def __init__(self):
        self.valIndex = {}  # {valor: indice_en_la_lista}
        self.elements = []  # [valor1, valor2, ..., valorN]

    def insert(self, val):
        if val in self.valIndex:
            return False  # El valor ya existe, no hacemos nada.
        else:
            # Si el valor no existe, lo añadimos al final de la lista.
            self.elements.append(val)
            # Y registramos su índice en el diccionario.
            self.valIndex[val] = len(self.elements) - 1
            return True
        

    def remove(self, val):
        if val not in self.valIndex:
            return False  # El valor no existe, no hacemos nada.
        else:
            # Obtenemos el índice del valor que queremos remover.
            indexRemove = self.valIndex[val]
            # Obtenemos el último elemento de la lista.
            lastElement = self.elements[-1]

            # Movemos el último elemento a la posición del elemento que queremos remover.
            self.elements[indexRemove] = lastElement
            # Actualizamos el índice del último elemento en el diccionario.
            self.valIndex[lastElement] = indexRemove

            # Eliminamos el último elemento de la lista (que ahora es el que queremos remover).
            self.elements.pop()
            # Eliminamos el valor del diccionario.
            del self.valIndex[val]

            return True

    def getRandom(self):
        # Seleccionamos un índice aleatorio de la lista de elementos.
        random_index = random.randint(0, len(self.elements) - 1)
        # Devolvemos el elemento en ese índice.
        return self.elements[random_index]
    
# Ejemplo de uso:
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom()) # Puede ser 1 o 2
print(randomizedSet.remove(1))  # True
print(randomizedSet.insert(2))  # False (2 ya está presente)
print(randomizedSet.getRandom()) # Siempre será 2 (porque 1 fue removido)