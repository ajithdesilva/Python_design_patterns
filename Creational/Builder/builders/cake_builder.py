############################################################################################
#   File            :   director.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we have implemented the abstract Cake class
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from base.cake import Cake

# --- Abstract Builder ---
class CakeBuilder:
    def __init__(self):
        self.cake = Cake()

    def reset(self):
        self.cake = Cake()
        return self

    def add_layer(self, flavor):
        self.cake.layers.append(flavor)
        return self

    def set_shape(self, shape):
        self.cake.shape = shape
        return self

    def add_frosting(self, frosting):
        self.cake.frosting = frosting
        return self

    def add_topping(self, topping):
        self.cake.toppings.append(topping)
        return self

    def get_cake(self):
        cake = self.cake
        self.reset()  # ready for next build if required
        return cake


