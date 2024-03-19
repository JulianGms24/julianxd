# 
class Bebida:
    
    def __init__(self, name):
        self.__name = name
    
    def getNombreBebida(self):
        return f"la bebida es:{self.__name}"
    
class Producto:
    
    def __init__(self, costo, precio):
        self.__costo = costo
        self.__precio = precio
        
    def getGanancias(self):
        return f"las ganacia es : {self.__precio - self.__costo}"
        
        
    #felipoe es gay indio setentra 
class Cerveza(Bebida, Producto):
    
    __contador = 0
    
    def __init__(self, name, marca, alcohol, precio , costo):
        Bebida.__init__(self,name)
        Producto.__init__(self,precio, costo)
        self.__marca = marca
        self.__alcohol = alcohol
        Cerveza.__contador +=1
    
    #def getNombreBebida(self):
    #    return f"{super().getNombreBebida()} de la marca {self.__marca} con un grado de alcohol de  {self.__alcohol}"
    def getdetallecerveza(self):
         return f"{super().getNombreBebida()} de la marca {self.__marca} con un grado de alcohol de  {self.__alcohol}"
    
    @staticmethod
    def getContadorCerveza():
        return f"se han creado {Cerveza.__contador} cervezas"
    
cerveza = Cerveza("Poker", "Bavaria", 4.0, 2000 , 2500)
cerveza2 = Cerveza("Aguila", "Bavaria", 4.0, 2500 , 2000)
cerveza3 = Cerveza("Corona", "Mexicana", 4.0 , 5000 , 4000)
print(cerveza.getNombreBebida())
print(cerveza.getdetallecerveza())
print(Cerveza.getContadorCerveza())
print(cerveza.getGanancias())
