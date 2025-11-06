############################################################################################
#   File            :   factory.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Factory class that ensures
#       Only one instance of itself can exist throughout the program's lifecycle.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from abc import ABC, abstractmethod



class Shape(ABC):
    """base class for all shapes. """

    @abstractmethod
    def draw(self) -> None:
        """ implemented by subclasses."""
        pass


# Extend Shape & create concrete implementations
class Circle(Shape):
    def draw(self) -> None:
        print("Drawing a Circle 🔵")

# Extend Shape & create concrete implementations
class Square(Shape):
    def draw(self) -> None:
        print("Drawing a Square 🟥")

# Extend Shape & create concrete implementations
class Triangle(Shape):
    def draw(self) -> None:
        print("Drawing a Triangle 🔺")


# Factory class encapsulates all shapes instanciation
class ShapeFactory:

    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        """
        Factory method to create & return a Shape object.

        Args:
            shape_type (str): Type of shape ("circle", "square", "triangle").

        Returns:
            Shape: An instance of the requested shape class.
        """
        shape_type = shape_type.lower()
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")



if __name__ == "__main__":
    print(" Factory Example ")
    
    factory = ShapeFactory()    # Create factory instance

    _circle_shape = factory.get_shape("circle") ### create instance by passing required type
    _circle_shape.draw()

    _triangle_shape = factory.get_shape("triangle") ### create instance by passing required type
    _triangle_shape.draw()

    _square_shape = factory.get_shape("square") ### create instance by passing required type
    _square_shape.draw()


