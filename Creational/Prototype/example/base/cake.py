
############################################################################################
#   File            :   cake.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#        Prototype Cake class which we are going to clone.
#        MUST implement the cloning 
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


import copy

# Prototype class
class Cake:
    def __init__(self, flavor, size, frosting, toppings):
        self.flavor = flavor
        self.size = size
        self.frosting = frosting
        self.toppings = toppings

    def __str__(self):
        return f"Cake(flavor={self.flavor}, size={self.size}, frosting={self.frosting}, toppings={self.toppings})"

    # Clone method. perform the clonning and return the clonned object
    def clone(self):
        return copy.deepcopy(self)