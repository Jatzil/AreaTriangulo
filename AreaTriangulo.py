#Pruebas unitarias, que se realizan en dicho programa para constatar que éste esté bien.
"""
>>> Area = AreaTriangulo(3,4,145)
>>> Area.CalcularArea()
>>> Area.getAreadelTriangulo()
3.4414586181062754
"""
#Librería math, la cual se utiliza posteriormente en el método donde se realizan todas las operaciones, y conversiones.
import math

#Nombre de la clase, y atributos que se generan en dicho programa, los cuales forman parte de éste mismo.
class AreaTriangulo:
    __lado1 = float(0)
    __lado2 = float(0)
    __angulo = float(0)
    __area = float(0)

#Método constructor, donde se colocan los parámetros ya en conversión, ubicados anteriormente como atributos.
    def __init__(self, lado1, lado2, angulo):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__angulo = angulo

#Método CalcularArea, cuyo nombre pertenece al nombre del programa, el cual se utiliza para poder realizar todas las operaciones, así como también las conversiones.
    def CalcularArea(self):
        if((self.__lado1 > 0) & (self.__lado2 > 0) & (self.__angulo > 0)):
            self.__area = (((0.5)*(self.__lado1 * self.__lado2))*(math.sin(math.radians(self.__angulo))))
        else:
            self.__area = 'Error'

#Método get, el cual contiene los datos de salida, para poder retornarlos, y dar un resultado, o un mensaje.
    def getAreadelTriangulo(self):
        return self.__area

#Estructura que manda a ejecutar las pruebas unitarias
if __name__ == '__main__':
    import doctest
    doctest.testmod()