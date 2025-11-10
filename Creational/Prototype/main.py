

############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use the prototype pattern to clone a instance.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

import copy

# Prototype class that we need to clone
class Cake:
    def __init__(self, flavor, size, frosting, toppings):
        self.flavor = flavor
        self.size = size
        self.frosting = frosting
        self.toppings = toppings

    def __str__(self):
        return f"Cake(flavor={self.flavor}, size={self.size}, frosting={self.frosting}, toppings={self.toppings})"

    # Clone method this will return the new object based on all the values
    def clone(self):
        return copy.deepcopy(self)



if __name__ == "__main__":
    
    # Original cake
    chocolate_cake = Cake("Chocolate", "Medium", "Chocolate Ganache", ["Cherries", "Sprinkles"])
    print("Original Cake:\n", chocolate_cake)

    # Clone the cake and modifying it
    birthday_cake = chocolate_cake.clone()
    birthday_cake.toppings.append("Birthday Candle")
    birthday_cake.size = "Large"

    print("Cloned Cake:\n", birthday_cake)
    print("Original Cake remains unchanged:", chocolate_cake)
