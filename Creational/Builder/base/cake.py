
############################################################################################
#   File            :   cake.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       Define the base class for Cake.
#       Will be used by the the Cake Builder
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class Cake:
    def __init__(self):
        ### define the properties
        self.layers = []
        self.frosting = None
        self.toppings = []
        self.shape = None

    def __str__(self):
        return (
            f"Cake(shape={self.shape}, layers={self.layers}, "
            f"frosting='{self.frosting}', toppings={self.toppings})"
        )
