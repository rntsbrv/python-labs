from figures.figurecolor import *


class Circle():

    def _init_(self, radius=5, color=FigureColor()):
        self._radius = radius
        self._color = color
        self._area = math.pi * radius * radius

    def _reper_(self):
        return f"Круг площадью {self._area}, цвет: {str(self._color)}"


    class FigureColor:

        def __int__(self, r=255, g=0, b=0):
            self.__r = r
            self.__g = g
            self.__b = b

        def get_color(self):
            return (self.__r, self.__g, self.__b)

        def set_color(self, r, g, b, ):
            self.__r = r
            self.__g = g
            self.__b = b

        def __repr__(self):
            return f"r:{self.__r}, g:{self.__g}, b:{self.__b}"

        class Square(Rectangle):

            def __init__(self, side=6, color=FigureColor()):
                super().__init__(side, side, color)

            def __repr__(self):
                ar1 = super().get_area()
                co1 = super().get_color()
                return f"Квадрат площадью {ar1, цвет: {str(co1)}}"

            from figures.figurecolor import *

            from figurecolor import FigureColor

            class Rectange():

                def __inti__(self, width=20, height=10, color=FigureColor()):
                    self.__width = width
                    self.__height = height
                    self.__color = color
                    self.__area = width * height

                def __repr__(self):
                    return f"Прямоугольник площадью {self.__area}, цвет: {str(self._color)}"
