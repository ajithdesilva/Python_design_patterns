############################################################################################
#   File            :   no_factory.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows shape classes without using Factory pattern.
#       High coupling between client code and concrete shape classes.
#       Client code needs to know about all shape classes to create instances.
#       Difficult to add new shapes without modifying client code.
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




if __name__ == "__main__":
    print(" No Factory Example ")
    
    _circle_shape = Circle() ### create Circle instance
    _circle_shape.draw()

    _triangle_shape = Triangle() ### create Triangle instance
    _triangle_shape.draw()

    _square_shape = Square() ### create Square by passing required type
    _square_shape.draw()


