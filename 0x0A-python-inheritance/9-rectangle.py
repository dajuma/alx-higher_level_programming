#!/usr/bin/Python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
        width (int); The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__class__.__name__) + "] "
        return string
