#!/usr/bin/python3
"""
Author: Robinson Montes
"""


class Square():
    """Square class for task
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """init method for square class
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width public class attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width public class attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height public class attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for hight public class attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def area_of_my_square(self):
        """Area of the square
        """
        return self.__height * self.__width

    def perimiter_of_my_square(self):
        """Method to calculate and return the perimeter of the square
        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String representation for square
        """
        return "{}/{}".format(self.__width, self.__height)

if __name__ == "__main__":

    s = Square(width=9, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
