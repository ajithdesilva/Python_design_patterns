############################################################################################
#   File            :   cake.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-07
#   Last Modified   :   2025-11-07
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines the base Cake class for the Factory design pattern example.
#       It provides a common interface for different types of cakes, including methods
#       for preparation, baking, and decoration.#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


from abc import ABC, abstractmethod

# --- Step 1: Define an abstract Cake interface ---
class Cake(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def decorate(self):
        pass