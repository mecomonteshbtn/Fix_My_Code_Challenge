#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:32:49 2020

@author: Robinson Montes
"""


class Square():
    """Square class for task

    Returns:
        Nothing.
    """

    width = 0
    height = 0

    def __init__(self, width, height):
        """Init method for square class
        """
        self.width = width
        self.height = height

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
            self.width = value

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
        return self.height * self.width

    def perimiter_of_my_square(self):
        """Calculate and return the perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation for square
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=9, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
